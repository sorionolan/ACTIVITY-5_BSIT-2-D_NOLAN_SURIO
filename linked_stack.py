class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow — Cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value

    def display(self):
        current = self.top
        items = []
        while current:
            items.append(current.value)
            current = current.next
        print("Stack:", items)


if __name__ == "__main__":
    print("=== LINKED STACK TEST ===")
    lstack = LinkedStack()
    lstack.push("A")
    lstack.push("B")
    lstack.push("C")
    lstack.display()
    print("Peek:", lstack.peek())
    print("Pop:", lstack.pop())
    lstack.display()
