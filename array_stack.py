class ArrayStack:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack Overflow — Cannot push to a full stack")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow — Cannot pop from an empty stack")
        value = self.data[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[self.top]

    def display(self):
        print("Stack:", self.data[:self.top + 1])


if __name__ == "__main__":
    print("=== ARRAY STACK TEST ===")
    stack = ArrayStack(5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    stack.display()
