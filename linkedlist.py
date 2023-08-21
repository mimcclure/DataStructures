class Node:
    def __init__(self, data):
        self.data = data #initialize the node w/ the data passed as an argument
        self.next = None #reference with None if we only have one node (nothing to reference)

    #create a new node and check if the head is an empty node or not. New node because the head if it is, if not we insert the head at the next new node, then equal head and the new node
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    #create new_node, current_node = head, and a counter position @ 0. If index equals 0 the node can be inserted and we call insertAtBegin, otherwise we run a while loop until our current node is None or pos + 1 is not equal to the index we have at the one position.
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position + 1 != index):
                position += 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    #method to add a node at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    #update the value of a node at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = val
            else:
                print("Index not present")

    #remove the first node by making it the second node head of the list
    def remove_first_node(self):
        if(self.head == None):
            return
        
        self.head = self.head.next

    #remove the last node by traversing to the second last node using a while loop, then making the next of that node None
    def remove_last_node(self):
        if(self.head == None):
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = None
            
    #remove a node at a given index. If head is None, we simply return else we initialize a current node with self.head and positoin w/ 0. If position equals index we call remove_first_node(), else we traverse to the one node before that we want to remove using a while loop.
    #after we're out of the while loop check that the current node is equal to None (make it current_node.next = current_node.next.next). If not print "Index not present"
    def remove_at_index(self, index):
        if(self.head == None):
            return
        
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present.")

    #removes the node with the given data from a linked list. 
    def remove_node(self, data):
        current_node = self.head

        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next


    #linked list traversal
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    #length of a linked list
    def sizeofLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0