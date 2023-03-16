import sys
import asyncio
import multiprocessing
import concurrent.futures

ui_executor = concurrent.futures.ProcessPoolExecutor(
	max_workers=1, #only 1 worker required for ui
	mp_context=multiprocessing.get_context('spawn')
)

#only one async_input task should be run at once

async def async_input(prompt):
	loop = asyncio.get_event_loop()
	return await loop.run_in_executor(ui_executor, input, prompt)
