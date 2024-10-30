class Stack(Exception):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty_stack(self):
        if len(self.items) == 0:
            return len(self.items)

    def pop(self):
        if not self.empty_stack():
            return self.items.pop()
        else:
            print("cannot pop in an empty stack")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
for i in range(len(stack.items)):
    print(stack.items[i])
for i in range(len(stack.items)):
    print(stack.pop())
print(len(stack.items))
stack.pop()
