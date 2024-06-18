#Node of a singly Linked List 
class Node:
    length = 0
    #constructer
    def __init__(self):
        self.data = None
        self.next = None

    #method for setting the data field of the node
    def setData(self,data):
        self.data=data

    #method for getting the data field of the node
    def getData(self):
        return self.data
    
    #method for setting the next field of the node
    def setNext(self,next):
        self.next = next

    #method for getting the next field of the node
    def getNext(self):
        return self.next
    
    #returns true if the node points to another node
    def hasNext(self):
        return self.next != None
    
    #Traverse
    def listLength(self):
        current = self.head
        count = 0

        while current != None:
            count +=1
            current = current.getNext()
        return count
    
    #Insertion at begining
    def insertAtBegining(self,data):
        newNode = Node()
        newNode.setData(data)

        if self.length == 0: #length or ....
            self.head = newNode

        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length +=1

    def insertAtEnd(self,data):
        newNode = Node()
        newNode.setData(data)

        if self.length == 0:
            self.insertAtBegining(data)
        else:
            current = self.head
            while current.getNext() != None :
                current = current.getNext()
            current.setNext(newNode)
            self.length+=1

    def insertAtPos(self,data,pos):
        if pos>self.length or pos<0 :
            return None
        elif pos==0:
            self.insertAtBegining(data)
        elif pos==self.length:
            self.insertAtEnd(data)
        else:
            newNode = Node()
            newNode.setData(data)
            count=0
            current=self.head
            while count<pos-1:
                count+=1
                current=current.getNext()
            newNode.setNext(current.getNext())
            current.setNext(newNode)
            self.length+=1

    #Deletion
    #Deleting at begining
    def deleteAtbegin(self):
        if self.length == 0:
            print("List is empty !")
        else:
            self.head = self.head.next
            self.length-=1

    #Deleting at end
    def deleteAtEnd(self):
        if self.length == 0:
            print("List is empty !")
        else:
            current = self.head
            prev = self.head
           
            while current.getNext()!=None:
                prev=current
                current=current.getNext()
            
            prev.setNext(None)
            self.length-=1

    #delete node using value
    def deleteData(self,val):
        current = self.head
        prev = self.head
    
        while current.next != None or current.data != val:
            if current.data == val:
                prev.next = current.next
                self.length-=1
                return
            else:
                if current.next!=None:
                    prev=current
                    current=current.next
                else:
                    print("value does not found")
                    return

        print("value does not found")
    
    def deletePos(self,pos):
        count=0
        current = self.head
        prev = self.head

        if pos > self.length or pos < 0 :
            print("Postion is invalid")

        else:
            while current.next != None or count<pos:
                count+=1
                if count == pos:
                    self.length-=1
                    prev.next=current.next
                    return
                else:
                    prev=current
                    current=current.next


    def display(self):
        tem = self.head
        while True :
            print (f"{tem.getData()} -> ",end="")
            if tem.getNext() == None :
                break
            tem = tem.next
        print("")
            
obj = Node()
obj.insertAtBegining(2)
obj.insertAtEnd(3)
obj.insertAtBegining(4)
obj.insertAtPos(5,1)
obj.insertAtPos(6,4)
obj.display()
obj.deleteAtbegin()
obj.deleteAtEnd()
obj.display()
obj.deleteData(2)
obj.display()
obj.deleteData(32)
obj.insertAtPos(5,2)
obj.insertAtPos(6,2)
obj.display()
obj.deletePos(2)
obj.display()
