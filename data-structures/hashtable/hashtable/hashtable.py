import sys
sys.path.append('/home/bayan/code-401/data-structures-and-algorithms-401/data-structures/linked_list')
from linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self,size=1024):
        self.size=size
        self.buckets=[None]*self.size

    def hash(self,key):
        if type(key)==int:
            sum_of_assci=key
        else:
            sum_of_assci=sum([ord(char) for char in key])
        temp_value=sum_of_assci*19
        hashed_key= temp_value % self.size
        return hashed_key


    def add(self,key,value):
        idx_hash=self.hash(key)

        if self.buckets[idx_hash]==None:
           self.buckets[idx_hash]=LinkedList()
       
        self.buckets[idx_hash].append({key:value})
           

    def get(self,key):
        idx_hash=self.hash(key)
        if self.buckets[idx_hash]==None:
            return 'Key is not in the hash table'
        else:
            if self.buckets[idx_hash].head ==None:
                return 'Bucket is empty'
            else:
                current=self.buckets[idx_hash].head
                while current:
                    if list(current.value.keys())[0]==key:
                        return current.value[key]
                    current=current.next
                return 'Key is not in the hash table!'


    def contains(self,key):
       idx_hash=self.hash(key)
       if self.buckets[idx_hash]==None:
           return False
       else:
            current=self.buckets[idx_hash].head
            if current==None:
                return False
            else:
                while current:
                    if list(current.value.keys())[0]==key:
                        return True
                    current=current.next
                return False
              

    def __str__(self):
       return  str([bucket.__str__() for bucket in self.buckets if bucket != None ])
        




