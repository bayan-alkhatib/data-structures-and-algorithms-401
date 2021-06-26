class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    

class Binary_Tree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        """ node-left-right """
        try:

            self.values=[]
         
            if self.root == None:
                return "Tree is Empty"

            def tree(node):
               self.values+=[node.value]
               if node.left:
                tree(node.left)
               if node.right:
                tree(node.right)
               return self.values
            
            return tree(self.root)
        except:
            return "Error"

    def in_order(self):
        """ left-node-right"""
        try:

            self.values=[]
            
            if not self.root:
                return "Tree is Empty"

            def tree(node):
                if node.left:
                    tree(node.left)
                self.values+=[node.value]
                if node.right:
                    tree(node.right)
                return self.values
        
            return tree(self.root)
        except:
            return "Error"

        

    def post_order(self):
        """ left-right-node"""
        try:

            self.values=[]
            
            if not self.root:
                return "Tree is Empty"

            def tree(node):
                if not node:
                    return ' root is empty' 
                if node.left:
                    tree(node.left)
                if node.right:
                    tree(node.right)
                self.values+=[node.value]
                return self.values
        
            return tree(self.root)
        except:
            return "Error"


class Binary_Search_Tree(Binary_Tree):

    def add(self,value):

        '''add value to binery tree '''
        if self.root == None:
            self.root = Node(value)
        else:
        
            while self.root:
                if  value < self.root.value : 
                    if self.root.left == None: 
                        self.root.left = Node(value)
                        break
                    self.root = self.root.left
                else:
                    if self.root.right == None: 
                        self.root.right = Node(value)
                        break
                    self.root = self.root.right

    def Contains(self,value):
        if self.root==None:
            return 'Tree is Empty'

        elif value in self.post_order():
            return True

        else:
            return False

        





