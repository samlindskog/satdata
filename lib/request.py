import httpx
import asyncio
import contextlib
from collections import deque


class AsyncRequestAll(contextlib.AbstractAsyncContextManager):
	_responses = deque()
	_tasks = deque()
	_async_client = None

	async def __init__(self, urls):
		self._urls = urls

	async def __aenter__(self):
		self._async_client = httpx.AsyncClient()
		return self

	async def __aexit__(self, __exc_type, __exc_value, __traceback):
		assert self._async_client != None
		await self._async_client.aclose()

	async def get(self, *args):
		await self._request("get", *args)

	async def request(self, method, *args):
		await self._request(method, *args)

	async def _request(self, method, *args):
		assert self._async_client != None
		for url in self._urls:
			coro = self._async_client.request(method, url, *args)
			task = asyncio.create_task(
				self._store_response(coro),
				name=url
			)
			self._register_task(task)

	async def _store_response(self, coro):
		response = await coro
		self._responses.append(response)		

	def _register_task(self, task):
		pass