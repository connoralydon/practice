# asynchio.py

# asynchronous programming in python

import asyncio
"""
async def main():
    print("main func")
    # await foo("text") #running inline
    task = asyncio.create_task(foo("text")) # this prints foo before finished
        # can't run this task until the current function is completed
    await asyncio.sleep(2) # only pauses for 2 seconds not 1, allows task to run
    # await task # wait until this task is finished, if not it finishes after
    print("finished") # foo is blocking this print
    
# main() # wont work because it is an async function

async def foo(text):
    print(text)
    await asyncio.sleep(7) # need await to coroutine, awaiting for one second
    # need to be in async code to run await

asyncio.run(main()) # running async function
# it waits for 1 sec
"""

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2) # sent request to server
    print("done fetching")
    return {"data":1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25) # 0.25 seconds to run loop

async def main():
    # running both at the same time
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers()) # starting the tasks
        # these tasks are future's, value will come in future, need to await for task

    # future equivalent to a promise
    # returns 'future' value, placeholder for value that will exist in future
    # import time
    print("before sleep")
    await asyncio.sleep(1) # time.sleep(2) is blocking
    print("after sleep")
    # need to await or it will print the promise
    value = await task1 # await that task to complete before we move further down in the program
    # if delay in task 1, then we start second task in event loop
    
    print(value)
    
    # only prints first 8 values, need to await other task to finish
    # it starts running in await
    
    await task2
    
    
# asyncio.run(main())

async def main2():
    task2 = asyncio.create_task(print_numbers()) # starts running
    
    print(await fetch_data()) # waits for this to complete, then other task
    
    await task2 # finishes task 2

asyncio.run(main2())