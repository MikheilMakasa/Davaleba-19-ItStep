class Node:
    def __init__(self, data):
        # Creating a new node with the data and setting next to None.
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # Creating a new stack with the top node set to None and length set to 0.
        self.top_node = None
        self.length = 0

    def empty(self):
        # Checking if the stack is empty.
        return self.length == 0

    def size(self):
        # Returning the current size (number of elements) in the stack.
        return self.length

    def top(self):
        # Returning the data of the top element in the stack.
        # Raising an IndexError if the stack is empty.
        if not self.empty():
            return self.top_node.data
        else:
            raise IndexError("Stack Is Empty")

    def push(self, data):
        # Pushing a new node with the given data onto the stack.
        new_node = Node(data)

        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1

    def pop(self):
        # Poping the top element from the stack and returning its data.
        # Raising an IndexError if the stack is empty.
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            raise IndexError("Stack Is Empty")

# Creating an instance of the Stack class
stack = Stack()

# Printing the initial size of the stack (0)
print(stack.size())

# Pushing elements (1, 5, 10) onto the stack
stack.push(1)
stack.push(5)
stack.push(10)

# Printing the current size of the stack (3)
print(stack.size())

# Popping the top element from the stack and printing it (10)
print(stack.pop())

# Printing the data of the new top element in the stack (5)
print(stack.top())
