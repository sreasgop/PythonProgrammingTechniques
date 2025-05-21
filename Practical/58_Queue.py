# QUESTION: 
# Implement a Queue using a list.


# CODE:
class Queue:
    def __init__(self, *args):
        self.items = list(args) 

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        print(f"Enqueued: {item}")
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)


q = Queue(1, 2, 3)  
q.display()
q.enqueue(4)
q.enqueue(5)
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())
print("Front:", q.front())
q.display()



# OUTPUT:
# Queue: [1, 2, 3]
# Enqueued: 4
# Enqueued: 5
# Dequeued: 1
# Dequeued: 2
# Front: 3
# Queue: [3, 4, 5]
