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
    
    # Tend to left traversal
    def preorder(root,result):
        if root == None:
            return
        stack = []
        stack.append(root)
        while stack:
            current = stack.pop()
            result.append(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

    def inorder(root,result):
        if root == None:
            return
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right
        return result
    
    def postorder(root,result):
        if root == None:
            return
        visited = set()
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and node.right not in visited:
                    stack.append(node)
                    node = node.right
                else:
                    result.append(node.data)
                    visited.add(node)
                    node = None
        return result
        

if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    print(root.data)
    print(root.left.data)
    print(root.right.data)
    print(root.left.left.data)
    print(root.left.right.data)
    print(root.right.left.data)
    print(root.right.right.data)

    result = []
    BinaryTreeNode.preorder(root,result)
    print(result)

    result = []
    BinaryTreeNode.inorder(root,result)
    print(result)

    result = []
    BinaryTreeNode.postorder(root,result)
    print(result)