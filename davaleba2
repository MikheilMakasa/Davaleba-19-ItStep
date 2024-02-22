class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def remove_value(self, value):
        current_node = self.head

        # Checking if the value to be removed is in the head node
        if current_node and current_node.data == value:
            self.head = current_node.next
            return

        # Search for the node with the specified value and remove it
        while current_node and current_node.data != value:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            # Value not found in the linked list
            return

        prev_node.next = current_node.next

    def display_info(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


# Creating an instance of the LinkedList class
linked_list = LinkedList()

# Appending nodes with data 5, 10, 2, 10, 8 to the linked list
linked_list.append(5)
linked_list.append(10)
linked_list.append(2)
linked_list.append(10)
linked_list.append(8)

# Displaying the linked list: 5 -> 10 -> 2 -> 10 -> 8
linked_list.display_info()

# Removing the nodes with value 10
linked_list.remove_value(10)

# Displaying the updated linked list: 5 -> 2 -> 8
linked_list.display_info()
