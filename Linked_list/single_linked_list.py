# Node class represents a single element of the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store data in the node
        self.next = None      # Pointer to the next node (initially None)

# LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None      # Head points to the first node (initially empty)

    # Method to insert a node at the beginning (head)
    def insert_head(self, data):
        new_node = Node(data)     # Create a new node with given data
        new_node.next = self.head  # Link new node to current head
        self.head = new_node       # Update head to the new node

    # Method to display the linked list
    def display(self):
        temp = self.head          # Start from the head
        while temp:               # Traverse until the end
            print(temp.data, end=" -> ")
            temp = temp.next      # Move to next node
        print("None")              # End of linked list


# Creating a LinkedList object
ll = LinkedList()

# Inserting elements at the head
ll.insert_head(10)
ll.insert_head(20)
ll.insert_head(30)
ll.insert_head(40)

# Displaying the linked list
ll.display()


