# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import threading
from time import sleep, time


class Scheduler:
    def __init__(self):
        self.fns = []  # tuple of (fn, time)
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)

    def delay(self, function, n):
        self.fns.append((function, time() * 1000 + n))


if __name__ == "__main__":
    scheduler = Scheduler()

    def f():
        print("hello")

    def f2():
        print("world")

    scheduler.delay(f, 1000)
    scheduler.delay(f2, 3000)
