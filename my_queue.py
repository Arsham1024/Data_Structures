# FIFO
# Left is head right is tail
# Using a deque ( double ended queue)
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        # popleft is from dequeue class just like pop but much faster.
        return self.queue.popleft()

    def size(self):
        return len(self.queue)

    def peak(self):
        # we want the first item at the head which is gonna be the left side.
        return self.queue[0]

    # This presents a human readable object
    def __str__(self):
        return str(self.queue)


if __name__ == "__main__":
    q = Queue()
    print(q)
    q.enqueue("a")
    print(q)

    for i in range(20):
        q.enqueue(i)

    print(q)

    for i in range(5):
        print(q.dequeue())
    print(q)
