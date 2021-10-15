class Node:
    def __init__(self, name, num):
        self.customerDetails = [name, num]
        self.nextNode = None

class Queue: 
      
    def __init__(self): 
        self.firstNode = self.LastNode = None
        self.size = 0
  
    def isEmpty(self): 
        return self.firstNode == None
      
    # Method to add an item to the queue 
    def enqueue(self, name, num): 
        newNode = Node(name, num) 
          
        if self.LastNode == None: 
            self.firstNode = self.LastNode = newNode
            self.size = self.size + 1
     
            return

        self.LastNode.nextNode = newNode
        self.LastNode = newNode 
        self.size = self.size + 1
  
    # Method to remove an item from queue 
    def dequeue(self): 
          
        if self.isEmpty(): 
            print("Nothing to dequeue.")
            return
        removeNode = self.firstNode
        self.firstNode = removeNode.nextNode
        self.size = self.size - 1

        if self.firstNode == None: 
            self.LastNode = None

    def traverse(self):
        currentNode = self.firstNode
        elements = []
        # while currentNode is not None:
        #     print (currentNode.customerDetails)
        #     currentNode = currentNode.nextNode
        while currentNode is not None:
            elements.append(currentNode.customerDetails)
            currentNode = currentNode.nextNode
        
        return elements
        
    def getFirstElement(self):
        
        if self.isEmpty(): 
            print("Empty Queue Now.")
            return
        
        return self.firstNode.customerDetails
