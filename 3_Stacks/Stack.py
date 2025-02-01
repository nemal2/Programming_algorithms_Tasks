class Stack(object):
    def __init__(self, limit=10):
        self.limit = limit
        self.stack = []
    
    def push(self, item):
        if len(self.stack) < self.limit:
            print("Pushing ", item)
            self.stack.append(item)
            return True
        return False
    
    def pop(self):
        if len(self.stack) > 0:
            print("Popping out ", self.stack[-1])
            return self.stack.pop()
        return None
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    

my_stack = Stack(5)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)

print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())