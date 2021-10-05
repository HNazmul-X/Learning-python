class Stack():
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        self.size = self.size + 1
        return self.stack.append(x)

    def pop(self):
        if self.size > 0:
            self.size = self.size - 1
            return self.stack.pop()
        else:
            return "self Already Empty"

    def top(self):
        return self.stack[-1]


x = Stack()
x.push(5)
x.push(3)
x.push(1)
print(x.stack)
print(x.size)

x.pop()



import pandas as pd
print(pd)
