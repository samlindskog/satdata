import sys
import asyncio

from lifetime_resources import ui_executor

#only one async_input task should be run at once

async def async_input(prompt):
	loop = asyncio.get_running_loop()
	return await loop.run_in_executor(ui_executor, input, prompt)
