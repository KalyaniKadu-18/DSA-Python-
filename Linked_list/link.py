# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Create nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# # Connect nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4

# # Print nodes
# current = node1
# while current is not None:
#     print( current.data, end=" -> ")
#     current = current.next

# print("None")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Take number of nodes
n = int(input("Enter number of nodes: "))

# Input for first node
data = int(input("Enter first element: "))
head = Node(data)
current = head

# Take remaining inputs
for i in range(2, n + 1):
    data = int(input(f"Enter element {i}: "))
    new_node = Node(data)
    current.next = new_node
    current = new_node

# Print linked list
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")
