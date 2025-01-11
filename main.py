from random import randint
import asyncio


def main():
    broker = Broker()
    asyncio.run(random_printer_loop(broker))


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


if __name__ == "__main__":
    main()
