import asyncio

#wraps coroutine, returns the task of itself

def trampoline(func):
	async def wrapper(*args, **kwargs):
		await func(*args, **kwargs)
		return asyncio.create_task(trampoline(func)(*args, **kwargs))
	return wrapper
