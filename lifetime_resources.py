import sys
import multiprocessing
import concurrent.futures

#all resources that run for the lifetime of the application
#collected in one place for easy cleanup upon exit

#function to set stdin for subprocesses
def _set_stdin(fd):
	sys.stdin.close()
	sys.stdin = open(fd)

ui_executor = concurrent.futures.ProcessPoolExecutor(
	max_workers=1,
	mp_context=multiprocessing.get_context('spawn'),
	initializer=_set_stdin,
	initargs=(0,)
)


def cleanup():
	ui_executor.shutdown()
