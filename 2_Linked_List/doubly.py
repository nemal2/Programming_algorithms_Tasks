class Node:
    size = 0
    #if data is not given by user its taken as none
    def __init__(self,data=None, next=None, prev=None) :
        self.data=data
        self.next=next
        self.prev=prev

    #method for setting the data field of the node
    def setData(self,data):
        self.data=data

    #method for setting the data field of the node
    def getData(self):
        return self.data

    #method for setting the next field of the node
    def setNext(self,next):
        self.next=next 

    #method for getting the next field of the node
    def getNext(self):
        return self.next  
    
    def hasNext(self):
        return self.next!=None
    
    #method for setting the next field of the node
    def setPrev(self,prev):
        self.prev=prev

    #method for getting the next field of the node
    def getPrev(self):
        return self.prev
    
    def hasPrev(self):
        return self.prev!=None
    
    def display(self):
        if self.size==0:
           print("No data") 
        else:
            tem = self.head
            while True :
                print (f"{tem.getData()} -> ",end="")
                if tem.getNext() == None :
                    break
                tem = tem.next
            print("")
    
    def insertbeg(self,data):
        newNode = Node(data,None,None)
        if self.size==0:
            self.head=self.tail=newNode

        else :
            newNode.setPrev(None)
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head=newNode
        
        self.size+=1
    
    def insertend(self,data):
        newNode = Node(data,None,None)
        if self.size==0:
            self.head=self.tail=newNode

        else:
            current = self.head
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(newNode)
            self.tail=current.next
        self.size+=1

    def insertPos(self,pos,data):
        newNode = Node(data,None,None)
        temp = self.head

        if self.size<pos:
            print("out of range")
            return
        elif self.head==None or self.size==0:
            self.insertbeg(data)
        
        else:
            while(temp.next!=None):
                temp=temp.next
            
            newNode.setPrev(temp.prev)
            
        self.size+=1

    def getNode(self, index):
        if index < 0 or index >= self.size:
            return None
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode.getNext()
        return currentNode

    def deletePos(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return

        temp = self.getNode(index)
        #print(temp.data)
        if temp:
            if temp == self.head:
                self.head = temp.getNext()
                if self.head:
                    self.head.setPrev(None)
            elif temp == self.tail:
                self.tail = temp.getPrev()
                if self.tail:
                    self.tail.setNext(None)
            else:
                temp.getPrev().setNext(temp.getNext())
                temp.getNext().setPrev(temp.getPrev())

            temp.setPrev(None)
            temp.setNext(None)
            temp.setData(None)
            self.size -= 1

obj = Node()
obj.insertbeg(1)
obj.insertbeg(5)
obj.insertend(9)
obj.display()
obj.deletePos(1)
obj.display()

    
    
    