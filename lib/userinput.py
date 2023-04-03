import asyncio

from . import lifetime_resources

#only one async_input task should be run at once


async def async_input(prompt):
	loop = asyncio.get_running_loop()
	return await loop.run_in_executor(
		lifetime_resources.ui_executor, 
		input, 
		prompt
	)
