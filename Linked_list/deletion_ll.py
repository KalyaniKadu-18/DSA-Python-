class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
head.next = node2
node2.next = node3
node3.next = node4

# Delete from the start
# if head is not None:
#     head = head.next

#delete from the last
# current = head
# while current.next.next is not None:
#     current = current.next

# current.next = None

#delete at particular node
current = head
while current.next.data !=30:
    current = current.next
current.next = current.next.next    

# Print linked list
temp = head
while temp is not None:
    print(temp.data, end="->")
    temp = temp.next
print("None")
