import asyncio

from lib import lifetime_resources
from lib import app

def main():
	try:
		loop = asyncio.new_event_loop()
		loop.create_task(app.app())
		loop.run_forever()
	except KeyboardInterrupt:
		print("\nKeyboardInterrupt")
	except Exception as e:
		print(e)
	finally:
		lifetime_resources.cleanup()

if __name__ == "__main__":
	main()