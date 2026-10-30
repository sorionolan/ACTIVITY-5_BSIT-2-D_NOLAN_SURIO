class ArrayQueue:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue Overflow — Cannot enqueue to a full queue")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow — Cannot dequeue from an empty queue")
        value = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.front]

    def display(self):
        items = []
        for i in range(self.size):
            index = (self.front + i) % len(self.data)
            items.append(self.data[index])
        print("Queue:", items)


if __name__ == "__main__":
    print("=== ARRAY QUEUE TEST ===")
    queue = ArrayQueue(5)
    queue.enqueue(100)
    queue.enqueue(200)
    queue.enqueue(300)
    queue.display()
    print("Front:", queue.peek_front())
    print("Dequeue:", queue.dequeue())
    queue.display()
