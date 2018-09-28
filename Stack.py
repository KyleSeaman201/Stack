#This Stack class adds items from the head of a list and removes items from the head.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,new_value):
        self.value = new_value

    def setNext(self,new_next):
        self.next = new_next

    def __str__(self):
        return ("{}".format(self.value)) 

    __repr__ = __str__
                          
  
class Stack:
    
    def __init__(self):
        self.top = None
    

    def isEmpty(self):
        if self.top== None:
            return True
        else:
            return False

    def size(self):
        count= 0
        temp= self.top
        while temp != None:
            count+=1
            temp= temp.next
        return count

    def push(self,item):
        new_node= Node(item)
        new_node.next=self.top
        self.top= new_node
     
    def pop(self):
        temp= self.top.value
        self.top= self.top.next
        return temp

    def peek(self):
        return self.top.value

    def printStack(self):
        temp=self.top
        while temp:
            print(temp.getValue())
            temp=temp.getNext()
