class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    inestance=[]

    def __init__(self):
        self.head = None
     
    def insert(self, value):
       
        node = Node(value)
        if self.head == None:
            self.head = node
            return self.head.value
        else:
            current = self.head
            self.head = node
            self.head.next = current
            return self.head.value
 

    def include(self,value):
        if self.head == None:
            return False
        else:
            temporary_value=Node(value)
            while temporary_value:
                if temporary_value.value==value:
                    return True
                temporary_value=temporary_value.next
            return False


    def __str__(self):
    
        if self.head == None:
            return 'NULL'
        else :
            values=''
            temporary_value=self.head
            while temporary_value:
                values+='{'+ f'{temporary_value.value}' +'} ' + '-> ' 
                temporary_value=temporary_value.next
            values=values +'NULL'
            return f'{values}'

