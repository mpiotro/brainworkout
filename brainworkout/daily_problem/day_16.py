# You run an e-commerce website and want to record the last N order ids in a log.

# Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class OrderLog(object):
    def __init__(self, n: int):
        self.n = n
        self._log = []
        self.current = 0

    def record(self, order_id):
        self._log.insert(self.current, order_id)
        self.increment_current()

    def get_last(self, i: int):
        return self._log[self.current - i]

    def increment_current(self):
        if self.current < self.n:
            self.current += 1
        else:
            self.current = 0


if __name__ == "__main__":
    order_log = OrderLog(5)
    order_log.record("ID-1")
    order_log.record("ID-2")
    order_log.record("ID-3")
    order_log.record("ID-4")
    order_log.record("ID-5")
    order_log.record("ID-6")
    order_log.record("ID-7")
    order_log.record("ID-8")

    print(order_log.get_last(1))
