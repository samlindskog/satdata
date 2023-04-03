import asyncio

def trampoline(coro):
	async def wrapper(*args, **kwargs):
		await coro(*args, **kwargs)
		asyncio.create_task(trampoline(coro)(*args, **kwargs))
	return wrapper
