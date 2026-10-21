class MyStack:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self):
        if not self.empty():
            return self.data.pop()
        return "Stack Underflow"

    def top(self):
        if not self.empty():
            return self.data[-1]
        return "Stack is Empty"

    def empty(self):
        return len(self.data) == 0

    def show(self):
        print(f"Current Stack (Top -> Bottom): {self.data[::-1]}")


# Simulation
my_stack = MyStack()
print("1. Pushing 5 items: 15, 25, 35, 45, 55")
for value in [15, 25, 35, 45, 55]:
    my_stack.add(value)

print(f"2. Peek top element: {my_stack.top()}")

print(f"3. Popped element: {my_stack.remove()}")
print(f"   Popped element: {my_stack.remove()}")

print("4. Display stack state:")
my_stack.show()
