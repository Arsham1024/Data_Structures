# LIFO
# To add append, to remove pop
# every operation happens on the right side

class Stack:
    # Class constructor
    def __init__(self):
        self.stack = []

        # checking for empty stack

    def is_empty(self):
        return len(self.stack) == 0

        # Push

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peak(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    # testing
    s = Stack()
    # Empty stack
    print(s)

    # populate the stack
    for i in range(20):
        s.push(i + 1)

    print(s)

    # peak an item notice how it doesn't delete.
    print(s.peak())
    print(s)

    # pop an item
    print("here we are poping:")
    print(s.pop())
    print(s)
