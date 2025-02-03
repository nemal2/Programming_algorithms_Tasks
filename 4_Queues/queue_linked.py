# node of a linked list

class Node:
    #constructor
    def __init__(self, data=None, next=None):
        self.data=data
        self.last=None
        self.next=next

    #method for setting the data to node
    def setData(self,data):
        self.data=data

    #method for getting the data field to node
    def getData(self):
        return self.data
    
    #method for setting the next field of the node
    def setNext(self,next):
        self.next=next
    #method for getting the next field of the node
    def getNext(self):
        return self.next

    #method for setting the last field of the node
    def setLast(self,last):
        self.last=last
    #method for getting the last field of the node
    def getLast(self):
        return self.last
    
    #return true if node points to another node
    def hasNext(self):
        return self.next != None
    
class Queue(object):
    def __init__(self, data=None):
        self.front=None
        self.rear = None
        self.size = 0
    
    def enqueue(self,data):
        self.lastNode = self.front
        self.front = Node(data,self.front)
        if self.lastNode:
            self.lastNode.setLast(self.front)
        if self.rear == None:
            self.rear = self.front
        self.size+=1
        for i in range(self.size-1):
            self.lastNode = self.lastNode.getNext()
        print('new queue ', self.front.data)

    def dequeue(self):
        if self.rear == None:
            print('Queue underflow')
            return 0
        else:
            result = self.rear.getData()
            self.rear = self.rear.last
            self.size-=1
            return result

    def size(self):
        return self.size
    

que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.dequeue()
que.enqueue(4)