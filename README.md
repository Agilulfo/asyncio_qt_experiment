# Async + Qt

Just a little exepriment to see how to combine Async code to run with Qt.

Qt Application run on an event loop that basically notify events(signals) to listeners (slots).

Asyncio code also relies on a loop that takes care of resuming coroutines.

simply running the two loops idependetly would not work unless soem tricks are done to coordinates the work.

Fortunatelly Qt has a module that can handle both things without much overhead.

In this repo I've played a little with both asyncio and qt and manage to run some async code in the background and keep the UI running at the same time.
