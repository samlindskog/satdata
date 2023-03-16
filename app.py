import asyncio
import httpx
import time

import psutil

from userinput import async_input
from decorators import trampoline

current_process = psutil.Process()
children_process = current_process.children(recursive=True)

@trampoline
async def print_user_input(prompt):
	answer = await async_input(prompt)
	print(current_process)
	print(children_process)
	print(answer)

@trampoline
async def cooltime(interval):
	await asyncio.sleep(1)
	print(time.time())

async def app():
	await cooltime(1)
