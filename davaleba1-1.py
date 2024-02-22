class Node:
    def __init__(self, data):
        # Creating a new node with the data and setting next to None initially.
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Creating an empty linked list with the head set to None.
        self.head = None

    def append(self, data):
        # Appending a new node with the given data to the end of the linked list.
        new_node = Node(data)

        if self.head is None:
            # If the linked list is empty, set the new node as the head.
            self.head = new_node
            return

        # Traverse to the end of the linked list and add the new node.
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert(self, data, index):
        # Inserting a new node with the given data at the specified index
        new_node = Node(data)

        if index == 0:
            # If the index is 0, insert the new node at the beginning
            new_node.next = self.head
            self.head = new_node
            return

        # Navigating to the specified index and inserting the new node.
        current_node = self.head
        current_index = 0

        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, index):
        # Removing the node at the specified index from the linked list.
        if index == 0:
            # If the index is 0, remove the head by updating it to the next node.
            self.head = self.head.next
            return

        # Navigating to the specified index and removing the node.
        current_node = self.head
        current_index = 0

        while current_index < index - 1 and current_node.next:
            current_index += 1
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def display_info(self):
        # Displaying the data of all nodes in the linked list.
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()

# Creating an instance of the LinkedList class
linked_list = LinkedList()

# Appending nodes with data 5, 10, and 2 to the linked list
linked_list.append(5)
linked_list.append(10)
linked_list.append(2)

# Displaying the linked list: 5 -> 10 -> 2
linked_list.display_info()

# Inserting nodes with data 11 at index 1 and 15 at index 2
linked_list.insert(11, 1)
linked_list.insert(15, 2)

# Displaying the updated linked list: 5 -> 11 -> 15 -> 10 -> 2
linked_list.display_info()

# Removing the node at index 2
linked_list.remove(2)

# Displaying the final linked list: 5 -> 11 -> 10 -> 2
linked_list.display_info()
