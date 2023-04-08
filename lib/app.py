import asyncio
import time
import logging

from . import userinput
from . import decorators
from . import request

logging.basicConfig(
	format="%(asctime)f|%(levelno)s|%(message)s"
)


async def getUrls():
	async with request.AsyncRequestAll(["google.com"]) as ar:
		responses = await ar.get()


@decorators.trampoline
async def print_user_input(prompt):
	answer = await userinput.async_input(prompt)
	print(answer)

@decorators.trampoline
async def cooltime(interval):
	await asyncio.sleep(1)
	print(time.time())

async def app():
	asyncio.gather(
		print_user_input("input da shit: "),
		cooltime(1)
)
