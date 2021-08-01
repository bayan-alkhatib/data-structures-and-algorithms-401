import sys
sys.path.append("/home/bayan/code-401/data-structures-and-algorithms-401/data-structures/hashtable")
from hashtable.hashtable import Hashtable

def left_join(ht1,ht2):
    
    array =[]

    for item in ht1.buckets:
        if item  != None:
            element =item.head
            current= element.value

            while current:
                key = list(current.keys())[0]

                if ht2.contains(key):
                    array+=[[key,current[key],ht2.get(key)]]
                else:
                    array+=[[key,current[key],None]]

                if element.next:
                    element=element.next
                    current=element.value
                else:
                    break

    if array== []:
        return 'cant joint left table is empty'

    return array

            


