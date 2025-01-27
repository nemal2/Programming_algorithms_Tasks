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
    
    # Recursive function to find maximum element in a binary tree
    def findMax(root):
        if root == None:
            return -1
        leftMax = BinaryTreeNode.findMax(root.left)
        rightMax = BinaryTreeNode.findMax(root.right)
        return max(root.data,max(leftMax,rightMax))
    
if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(34)
    root.right = BinaryTreeNode(3)    
    print(BinaryTreeNode.findMax(root))
