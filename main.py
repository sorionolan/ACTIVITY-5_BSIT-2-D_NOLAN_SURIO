from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def is_balanced(expression):
    stack = LinkedStack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


class PrintJob:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"{self.name} ({self.pages} pages)"


class PrintQueueSim:
    def __init__(self):
        self.jobs = LinkedQueue()

    def add_job(self, name, pages):
        job = PrintJob(name, pages)
        self.jobs.enqueue(job)
        print(f"Added: {job}")

    def process_next(self):
        if self.jobs.is_empty():
            print("No jobs in queue")
            return
        job = self.jobs.dequeue()
        print(f"Printing: {job} — Done!")

    def show_queue(self):
        print("--- Print Queue ---")
        current = self.jobs.front
        position = 1
        while current:
            print(f"{position}. {current.value}")
            current = current.next
            position += 1
        print("-------------------")


def main():
    while True:
        print("\n===== STACKS AND QUEUES MENU =====")
        print("[1] Test Array Stack")
        print("[2] Test Linked Stack")
        print("[3] Test Array Queue")
        print("[4] Test Linked Queue")
        print("[5] Parentheses Balancing Checker")
        print("[6] Print Queue Simulation")
        print("[0] Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Array Stack ---")
            cap = int(input("Enter stack capacity: "))
            stack = ArrayStack(cap)
            while True:
                action = input("(p)ush, (po)p, (pe)ek, (d)isplay, (b)ack: ").lower()
                if action == "p":
                    val = input("Enter value: ")
                    try:
                        stack.push(val)
                    except Exception as e:
                        print(e)
                elif action == "po":
                    try:
                        print("Popped:", stack.pop())
                    except Exception as e:
                        print(e)
                elif action == "pe":
                    try:
                        print("Peek:", stack.peek())
                    except Exception as e:
                        print(e)
                elif action == "d":
                    stack.display()
                elif action == "b":
                    break

        elif choice == "2":
            print("\n--- Linked Stack ---")
            stack = LinkedStack()
            while True:
                action = input("(p)ush, (po)p, (pe)ek, (d)isplay, (b)ack: ").lower()
                if action == "p":
                    val = input("Enter value: ")
                    stack.push(val)
                elif action == "po":
                    try:
                        print("Popped:", stack.pop())
                    except Exception as e:
                        print(e)
                elif action == "pe":
                    try:
                        print("Peek:", stack.peek())
                    except Exception as e:
                        print(e)
                elif action == "d":
                    stack.display()
                elif action == "b":
                    break

        elif choice == "3":
            print("\n--- Array Queue ---")
            cap = int(input("Enter queue capacity: "))
            queue = ArrayQueue(cap)
            while True:
                action = input("(e)nqueue, (d)equeue, (pe)ek, (di)splay, (b)ack: ").lower()
                if action == "e":
                    val = input("Enter value: ")
                    try:
                        queue.enqueue(val)
                    except Exception as e:
                        print(e)
                elif action == "d":
                    try:
                        print("Dequeued:", queue.dequeue())
                    except Exception as e:
                        print(e)
                elif action == "pe":
                    try:
                        print("Front:", queue.peek_front())
                    except Exception as e:
                        print(e)
                elif action == "di":
                    queue.display()
                elif action == "b":
                    break

        elif choice == "4":
            print("\n--- Linked Queue ---")
            queue = LinkedQueue()
            while True:
                action = input("(e)nqueue, (d)equeue, (pe)ek, (di)splay, (b)ack: ").lower()
                if action == "e":
                    val = input("Enter value: ")
                    queue.enqueue(val)
                elif action == "d":
                    try:
                        print("Dequeued:", queue.dequeue())
                    except Exception as e:
                        print(e)
                elif action == "pe":
                    try:
                        print("Front:", queue.peek_front())
                    except Exception as e:
                        print(e)
                elif action == "di":
                    queue.display()
                elif action == "b":
                    break

        elif choice == "5":
            print("\n--- Parentheses Checker ---")
            expr = input("Enter expression: ")
            if is_balanced(expr):
                print("Balanced")
            else:
                print("Not balanced")

        elif choice == "6":
            print("\n--- Print Queue Simulation ---")
            printer = PrintQueueSim()
            while True:
                action = input("(a)dd job, (p)rocess next, (s)how queue, (b)ack: ").lower()
                if action == "a":
                    name = input("File name: ")
                    pages = int(input("Number of pages: "))
                    printer.add_job(name, pages)
                elif action == "p":
                    printer.process_next()
                elif action == "s":
                    printer.show_queue()
                elif action == "b":
                    break

        elif choice == "0":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()　


if __name__ == "__main__":
    main()
