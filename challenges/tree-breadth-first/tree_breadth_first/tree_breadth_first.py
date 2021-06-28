from trees import  Binary_Tree 
# from stack_and_queue import Queue , Node

# import sys
# sys.path.append("/home/bayan/code-401/data-structures-and-algorithms-401/data-structures/trees")

# from trees.trees import Node, Binary_Tree

# class Node:
#     """Private class to create a nodes for the tree"""
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.next = None


# class Queue:
#     """class Queue which implements Queue data structure with its common methods"""
#     def __init__(self):
#         """Initiate class"""
#         self.front = None
#         self.rear = None
#     def is_empty(self):
#         """method to check if Queue is empty"""
#         if self.front == None:
#             return True
#         return False
#     def enqueue(self, node):
#         """Method that takes any value as an argument and adds a new node with that value to the back of the queue """
#         new_node = node
#         if self.is_empty():
#             self.front = new_node
#             self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#     def dequeue(self):
#         """Method that removes the node from the front of the queue, and returns the node's value."""
#         if not self.is_empty():
#             temp = self.front
#             self.front = self.front.next
#             temp.next = None
#             return temp
#         else:
#             return None
#     def peek(self):
#         """Method that returns the value of the node located in the front of the queue, without removing it from the queue."""
#         if not self.is_empty():
#             return self.front.value
#         return None

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.left=None
        self.right=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue (self,value):
        node=Node(value)
        if self.rear==None:
            self.front=node
            self.rear=node
            # return self.rear.value
        else:
            self.rear.next=node
            self.rear=node
            # return self.rear.value

    def dequeue(self):
        # try:
        #     if self.front == None:
        #         raise Exception

            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp


        # except Exception:
        #     return 'Error!'

#    def dequeue(self):
#         """Method that removes the node from the front of the queue, and returns the node's value."""
#         if not self.is_empty():
#             temp = self.front
#             self.front = self.front.next
#             temp.next = None
#             return temp
#         else:
#             return None
    def peek (self):
        try:
            if self.front == None:
                raise Exception

            return self.front.value

        except Exception:
            return 'Error!'

    def isEmpty(self):
        return self.front==None



def breadth_first(tree,node=None,arr=None):
    root=tree.root
    if not root:
        return "Tree is Empty"

    breadth=Queue()
    if arr is None:
        arr=[]
    if root :
        breadth.enqueue(root)

    while breadth.peek():
        # print(root.value)
        bb=breadth.dequeue()
        print(type(bb))
        arr.append(bb.value)

        if bb.left:
            breadth.enqueue(bb.left)
        if bb.right:
            breadth.enqueue(bb.right)

    return arr

        
     

    # arr=[tree.root.value]
    # arr_left=[]
    # arr_right=[]
    # node=tree.root
    # while node:
    #     if node.left:
    #         arr_left+=[node.left]
    #         node=node.left
    #     if node.right:
    #         arr_right+=[node.right]
    #         node=node.right

    


    



#[2,7,5,2,6,9,5,11,4]

b_tree=Binary_Tree()
b_tree.root=Node(2)
b_tree.root.left=Node(7)
b_tree.root.left.left=Node(2)
b_tree.root.left.right=Node(6)
b_tree.root.left.right.left=Node(5)
b_tree.root.left.right.right=Node(11)
b_tree.root.right=Node(5)
b_tree.root.right.right=Node(9)
b_tree.root.right.right.left=Node(4)
print(breadth_first(b_tree))

