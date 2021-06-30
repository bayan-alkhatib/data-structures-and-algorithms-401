# from stack_and_queue import Queue
from tree_fizz_buzz.stack_and_queue import Queue
class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]


class K_ary_tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root:
            arr=[self.root.value]
            arr+=[child.value for child in self.root.children]
            return str(arr)
        else:
            return  "Tree is Empty"
           





def tree_fizz_buzz(k_ary_tree):
    if not k_ary_tree.root:
        return "Tree is Empty"
    
    values=[]
    queue=Queue()
  
    if k_ary_tree:
        queue.enqueue(k_ary_tree.root)
   
    
    while not queue.isEmpty():
        
        tree_node=queue.dequeue()
        print(tree_node.value)

        if tree_node.value %3==0 and tree_node.value%5==0:
             values+=['FizzBuzz']
        elif tree_node.value %3==0:
            values+=['Fizz']
        elif tree_node.value %5==0:
            values+=['Buzz']
        else:
            values+=[str(tree_node.value)]

        
        for child in tree_node.children:
            queue.enqueue(child)

    return values




if __name__=='__main__':
    k_tree=K_ary_tree()
    print(k_tree)
    actual=tree_fizz_buzz(k_tree)
    print(actual)
    k_tree=K_ary_tree()
    k_tree.root=Node(2)
    k_tree.root.children+=[Node(7)]
    k_tree.root.children+=[Node(6)]
    k_tree.root.children+=[Node(2)]
    k_tree.root.children+=[Node(5)]
    k_tree.root.children+=[Node(15)]
    k_tree.root.children+=[Node(5)]
    k_tree.root.children+=[Node(9)]
    k_tree.root.children+=[Node(4)]
    print(tree_fizz_buzz(k_tree))
