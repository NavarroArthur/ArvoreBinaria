class Node:
    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None
    def __str__( self):
        return str(self.data)
    
class ArvoreBinaria:
    def __Init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data: 
            node= None(data)
            self.root=node
        else:
            self.root = None


    def postorder(self, node=None):

        if node is None:
            node = self.root
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node)