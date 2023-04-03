import asyncio
import time

from . import userinput
from . import decorators

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
