from tree_breadth_first.stack_and_queue import Queue 


def breadth_first(tree):
  
    if not tree:
        return "Tree is Empty"
    
    values=[]
    breadth=Queue()
  
    if tree :
        breadth.enqueue(tree.root)
   
    
    while not breadth.isEmpty():
        
        tree_node=breadth.dequeue()
        values+=[tree_node.value]
        
        if tree_node.left:
            breadth.enqueue(tree_node.left)
 
        if tree_node.right:
            breadth.enqueue(tree_node.right)

    return values

 


