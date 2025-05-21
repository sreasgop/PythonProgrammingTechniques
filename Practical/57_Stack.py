# QUESTION: 
# Implement a Stack using a list.



# CODE:
class Stack:
    def __init__(self, *args):
        self.items = list(args)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        print(f"Pushed: {item}")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack :", self.items[::-1])


s = Stack(10, 20, 30)  
s.display()
s.push(40)
s.push(50)
print("Popped:", s.pop())
print("Peek:", s.peek())
print("Size:", s.size())
print("Is empty:", s.is_empty())
s.display()



# OUTPUT:
# Stack : [30, 20, 10]
# Pushed: 40
# Pushed: 50
# Popped: 50
# Peek: 40
# Size: 4
# Is empty: False
# Stack : [40, 30, 20, 10]
