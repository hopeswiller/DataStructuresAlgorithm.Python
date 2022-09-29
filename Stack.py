class Stack:
    def __init__(self):
        self.top = -1
        self.mem = []

    def push(self, value):
        self.top += 1
        self.mem.append(value)
        print("Value pushed to stack")

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        self.mem.pop(self.top)
        self.top -= 1

    def isEmpty(self):
        res = True if self.top == -1 else False
        return res

    def top(self):
        return self.top

    def size(self):
        return self.top + 1

    def __repr__(self):
        return f"<Stack Items: {self.mem}>"


s = Stack()
print(s.isEmpty())
for i in range(1, 11):
    s.push(i)
print(s)

for i in range(4):
    s.pop()
print(s)
