class Queue(object):
    def __init__(self, limit=5):
        self.limit = limit
        self.queue = []
        self.size = 0
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.size <= 0
    
    def enQueue(self,item):
        if self.size >= self.limit:
            print('Queue overflow')
            return
        else:
            self.queue.append(item)

        if self.front is None:
            self.front = self.rear = 0
        
        else:
            self.rear = self.size
        
        self.size +=1
        print('new queue ', self.queue)

    def deQueue(self):
        if self.size <=0:
            print('Queue underflow')
            return 0
        
        else:
            self.queue.pop(0)
            self.size-=1
            if self.size ==0:
                self.front = self.rear = None
            else:
                self.rear = self.size-1
            print('new queue afer deQueue :', self.queue)
    
    def size(self):
        return self.size
    
que = Queue()
que.enQueue("first")
que.enQueue("sec")
que.enQueue("third")
que.deQueue()
que.enQueue("fourth")
