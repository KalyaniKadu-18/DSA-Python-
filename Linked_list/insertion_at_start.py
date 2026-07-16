class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Add at the start
# head = node1
# new_node = Node(50)
# new_node.next = head
# head = new_node

#add at the end
# new_node = Node(60)
# head = node1
# current = head

# while current.next is not None:
#     current = current.next
    
# current.next = new_node 

#insert at given position
new_node = Node(70)
head = node1
current = head
while current.next is not None and current.data != 20:
    current = current.next
new_node.next = current.next
current.next = new_node
    
def print_LL(head):
    temp = head
    while temp is not None:
        print(temp.data , end= '->')
        temp = temp.next
    print("None")
    
print_LL(head)    
    
         
        