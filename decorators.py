import asyncio

def trampoline(func):
	async def wrapper(*args, **kwargs):
		await func(*args, **kwargs)
		task = asyncio.create_task(trampoline(func)(*args, **kwargs))
	return wrapper
