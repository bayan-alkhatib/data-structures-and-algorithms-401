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

    def append(self,value):
        current=self.head
        if self.head ==None:
            self.head=Node(value)
            return self.head.value
        else:
            while current.next:
                current=current.next
            current.next=Node(value)
            return current.next

    def insert_before(self,val,new_val):
        try:
            current=self.head
            if self.head ==None:
                self.head=Node(val)
                return self.head
            elif current.value == val:
                       self.insert(new_val)
            else:
                while current: 
                    if  current.next.value== val:
                        saved_current_val=current.next
                        current.next=Node(new_val)
                        current.next.next=saved_current_val 
                        return current.next
                    current=current.next
        except:
            raise Exception ('Error')


    def insert_after(self,val,new_val):
        try:
            current=self.head
            if self.head ==None:
                self.head=Node(val)
                return self.head
            else:
                while current: 
                    if  current.value== val:
                        saved_current_val=current.next
                        current.next=Node(new_val)
                        current.next.next=saved_current_val 
                        return current.next
                    current=current.next
        except:
            raise Exception ('Error')

    def kthFromEnd(self,k):
        current=self.head
        length=1
        while current.next:
            length+=1
            current=current.next
        current=self.head
        if k>= length:
            return 'Error! index out of range'
        elif k<0:
            return "Error! k can't be negative number"
        else:
            count =length-k-1
            for i in range(length):
                    if i == count:
                        return current.value
                    current =current.next    


def zipLists(list1, list2):
        temp='head -> '
        current1=list1.head
        current2=list2.head
        values=[]
        while current1:
            values+=[current1.value]
            current1 = current1.next
            if current2:
                values+=[current2.value]
                current2 = current2.next 

        if current1==None and current2 != None:
            while current2:
                values+=[current2.value]
                current2 = current2.next  

        for  i in range(len(values)):
            temp+='{'+f'{values[i]}'+'} '+'-> '
        temp+='NULL'
        return temp
