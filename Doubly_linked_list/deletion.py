class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


dll = DoublyLinkedList()

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input(f"Enter data {i+1}: "))
    dll.insert_at_start(data)

print("\nDoubly Linked List after insertion:")
dll.display()

choice = input("\nDo you want to delete from beginning? (y/n): ")

if choice.lower() == 'y':
    dll.delete_from_beginning()
    print("\nDoubly Linked List after deletion:")
    dll.display()