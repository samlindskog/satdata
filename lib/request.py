import asyncio
import contextlib
import logging
import _collections_abc

import httpx
from collections import deque

class AsyncRequestAll(contextlib.AbstractAsyncContextManager):
	_request_tasks = deque()
	_async_client = None

	async def __init__(self, urls=list(), conc_downloads=0):
		self._urls = urls
		self._conc_downloads = conc_downloads

	async def __aenter__(self):
		self._async_client = httpx.AsyncClient()
		return self

	async def __aexit__(self, *_):
		assert self._async_client != None
		await self._async_client.aclose()

	async def get(self, *args, urls=None):
		return await self._request("get", *args, urls)

	async def request(self, method, *args, urls=None):
		return await self._request(method, *args, urls)

	async def _request(self, method, *args, urls=None):
		assert self._async_client != None

		if urls != None:
			self._urls.append(urls)

		for url in self._urls:
			task = asyncio.create_task(
				self._async_client.request(method, url, *args),
				name=url
			)
			self._request_tasks.append(task)
		return await self._return_all_responses()


	async def _return_all_responses(self, refresh_rate=1):
		results = deque()
		async for result in self._valid_taskresults_gen():
			results.append(result)
			await asyncio.sleep(refresh_rate)
		return results

	async def _valid_taskresults_gen(self):
		results = deque()
		rqtlength = len(self._request_tasks)
		while rqtlength > 0:
			for _ in range(rqtlength):
				task = self._request_tasks.pop()
				try:
					result = task.result()
				except asyncio.InvalidStateError:
					self._request_tasks.appendleft(task)
					continue
				except asyncio.CancelledError:
					logging.warning(f"Task \"{task.get_name()}\" has been cancelled.\n \
									It's result was not retreived")
					continue
				except Exception as exc:
					logging.warning(f"Task \"{task.get_name()}\" result throws exception \"{exc}\".\n \
									It's result was not retreived")
					continue
				results.append(result)
			yield results
			results.clear()
			rqtlength = len(self._request_tasks)
