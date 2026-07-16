class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_start(self,data):
        new_node = Node(data)
        
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
            
        self.head = new_node
    
    #display reverse
    def Display_reverse(self):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        
        #Go to last node
        while temp.next is not None:
            temp = temp.next
            
        #Traverse backward
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.prev      
        print("None")    
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")    
        
    def display_specific_node(self,position):
        temp = self.head
        count = 1
        while temp is not None:
            if count == position:
                print("Node at position",position,"is : ", temp.data)
                return
            count += 1     
            temp = temp.next
        print("Node not found") 
               
dll = DoubleLinkedList()

n = int(input("Enter number of nodes: "))
for i in range(n):
    value = int(input(f"Enter data for node : "))
    dll.insert_at_start(value)
    
dll.display()
dll.Display_reverse()
dll.display_specific_node(3)    