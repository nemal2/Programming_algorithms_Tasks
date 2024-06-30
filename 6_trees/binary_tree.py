class BinaryTreeNode:
    def __init__(self,data):
        self.data = data    #root node
        self.left= None     #left child
        self.right=None     #right child

    #set data
    def setData(self,data):
        self.data= data

    #get data
    def getData(self):
        return self.data
    
    #left child of a node
    def getLeft(self):
        return self.left
    
    #right child of a node
    def getRight(self):
        return self.right
