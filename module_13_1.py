import asyncio
from time import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        print(f'Силач {name} поднял {i}')
        await asyncio.sleep(i/power)
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Sasha', 5))
    task2 = asyncio.create_task(start_strongman('Rustic', 3))
    task3 = asyncio.create_task(start_strongman('Dania', 10))
    await task1
    await task2
    await task3

if __name__ == '__main__':
    start = time()
    asyncio.run(start_tournament())
    end = time()
    print(f'time run {end - start}')