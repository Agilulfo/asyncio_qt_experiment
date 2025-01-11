from random import randint
import asyncio


def run_loopy():
    broker = Broker()
    asyncio.run(run_as_tasks(broker))


async def run_as_tasks(broker):
    generator = asyncio.create_task(random_generator_loop(broker))
    printer = asyncio.create_task(random_printer_loop(broker))

    await generator
    await printer


class Broker:
    def __init__(self):
        self.value = 0

    def update(self, value):
        self.value = value

    def get(self):
        return self.value


async def random_generator_loop(broker):
    while True:
        sleep_duration = randint(1, 3)
        await asyncio.sleep(sleep_duration)
        random_value = randint(0, 99)
        broker.update(random_value)


async def random_printer_loop(broker):
    while True:
        sleep_duration = randint(1, 3)
        await asyncio.sleep(sleep_duration)
        print(broker.get())
