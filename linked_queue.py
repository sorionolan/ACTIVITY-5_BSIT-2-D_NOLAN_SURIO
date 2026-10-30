class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow — Cannot dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value

    def display(self):
        current = self.front
        items = []
        while current:
            items.append(current.value)
            current = current.next
        print("Queue:", items)


if __name__ == "__main__":
    print("=== LINKED QUEUE TEST ===")
    lqueue = LinkedQueue()
    lqueue.enqueue("Job 1")
    lqueue.enqueue("Job 2")
    lqueue.enqueue("Job 3")
    lqueue.display()
    print("Front:", lqueue.peek_front())
    print("Dequeue:", lqueue.dequeue())
    lqueue.display()
