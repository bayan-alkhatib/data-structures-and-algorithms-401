import sys
from typing import Hashable
sys.path.append("/home/bayan/code-401/data-structures-and-algorithms-401/data-structures/hashtable")
from hashtable.hashtable import Hashtable

sys.path.append("/home/bayan/code-401/data-structures-and-algorithms-401/data-structures/trees")
from trees.trees import Binary_Search_Tree


def tree_intersection(bt1,bt2):
    array=[]
    hashtable=Hashtable()

    if bt1.root== None or bt2.root==None:
        return 'input tree is empty'


    tree_arr1=bt1.pre_order()
    print(tree_arr1)
    tree_arr2=bt2.pre_order()
    print( tree_arr2)

    for item in tree_arr1:
        hashtable.add(item,item)

    print(hashtable)

    for element in tree_arr2:
        if hashtable.contains(element):
            array+=[element]
    
    if array==[]:
        return 'input Trees have No intersection'

    return array

if __name__=='__main__':
    bt1=Binary_Search_Tree()
    bt1.add(150)
    bt1.add(100)
    bt1.add(250)
    bt1.add(75)
    bt1.add(160)
    bt1.add(200)
    bt1.add(350)
    bt1.add(125)
    bt1.add(175)
    bt1.add(300)
    bt1.add(500)

    bt2=Binary_Search_Tree()
    bt2.add(42)
    bt2.add(105)
    bt2.add(600)
    bt2.add(15)
    bt2.add(161)
    bt2.add(201)
    bt2.add(351)
    bt2.add(126)
    bt2.add(176)
    bt2.add(4)
    bt2.add(501)

    print(tree_intersection(bt1,bt2))

