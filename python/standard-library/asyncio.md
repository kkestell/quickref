```python
import asyncio

# Basic example
async def my_coroutine():
    print('Starting')
    await asyncio.sleep(1)
    print('Ending')

async def main():
    await asyncio.gather(my_coroutine(), my_coroutine())

asyncio.run(main())

# Run a coroutine in the event loop
async def my_coroutine():
    # Do some work
    pass

loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())

# Call a synchronous function from an async function
def my_sync_function():
    # Do some work
    pass

async def my_async_function():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, my_sync_function)
    # Do something with result

# Waiting for multiple coroutines to finish
async def coro1():
    await asyncio.sleep(1)
    return 'coro1'

async def coro2():
    await asyncio.sleep(2)
    return 'coro2'

async def main():
    results = await asyncio.gather(coro1(), coro2())
    print(results)

asyncio.run(main())

# Cancelling a coroutine
async def my_coroutine():
    try:
        while True:
            print('Working')
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('Cancelled')

async def main():
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(3)
    task.cancel()
    await task

asyncio.run(main())
```