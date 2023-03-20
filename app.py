import asyncio
import httpx
import time


from userinput import async_input
from decorators import trampoline

@trampoline
async def print_user_input(prompt):
	answer = await async_input(prompt)
	print(answer)

@trampoline
async def cooltime(interval):
	await asyncio.sleep(1)
	print(time.time())

async def app():
	asyncio.gather(
		print_user_input("input da shit: "),
		cooltime(1)
	)
