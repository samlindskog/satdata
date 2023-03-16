import asyncio

import app

def main():
	loop = asyncio.get_event_loop()
	loop.create_task(app.app())
	loop.run_forever()

if __name__ == "__main__":
	main()