from io import StringIO
from os import curdir


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
            temporary_value=self.head
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
                values+=f'{temporary_value.value}'  + '-> ' 
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
            if self.head ==None:
                self.head=Node(val)
            if self.head.value == val:
                self.insert(new_val)
            else:
                try:
                    current=self.head
                    while current.next: 
                        if  current.next.value== val:
                            saved_current_val=current.next
                            current.next=Node(new_val)
                            current.next.next=saved_current_val 
                            return current.next
                        current=current.next
                except:
                    raise Exception (f'{val} is not in linked list')


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

    def kth(self,j):
        current=self.head
        val=[]
        while current:
            val+=[current.value]
            current=current.next
        val=val[::-1]

        for i in range(len(val)):
            if i==j:
                return val[j]

def funaddtwolists(l1, l2):
    l1_arr=[]
    l2_arr=[]
    int_l1=''
    int_l2=''

    output_list= LinkedList()

    current1=l1.head
    current2=l2.head

    while current1 or current2:
        if current1:
            l1_arr+=[str(current1.value)]
            current1=current1.next
        if current2:
            l2_arr+=[str(current2.value)]
            current2=current2.next
        
    l1_arr=l1_arr[::-1]
    l2_arr=l2_arr[::-1]
    
    int_l1=int(int_l1.join(l1_arr))
    int_l2=int(int_l2.join(l2_arr))

    sum_lists= str(int_l1+int_l2)

    for num in sum_lists:
        output_list.insert(num)

    return output_list



# algorithm:
# define array1 and array2

# push values of list1 and list2 into array1 and array2

# reverse array1 and array2

# convert array1 and array2 into string

# sum int array1 and array2

# define output linked list  as linked list instance 

# loop over string of sum 

#     insert sum values int output linked list



def link_odd_even(in_list):
    l_list=LinkedList()
    
    current=in_list.head
    count=1

    while current:
        if count%2==1:
            l_list.append(current.value)
        current=current.next
        count+=1

    current=in_list.head
    count =1
    
    while current:
        if count%2==0:
            l_list.append(current.value)
        current=current.next
        count+=1
    
    in_list=l_list

    return in_list 


##  swape_adjacent_nodes
# algorithm:
# 1. define a function called swape_adjacent with an argment linked_list
#         2. define current variable as linked_list.head
#         3. loop over current
#             4. if current.next == none:
#                 break
#             5. swape between current and current.next
#             6. update current to current.next.next (move 2 steps)
#         7. return linked list

# edge case:
# if we reach  a next node before non (len linked list is odd )

# input= linked list
# output= linked list with every adjecent nodes are swapped

def swape_adjacent(ll):
    current=ll.head
    while current:
        if current.next ==None:
            break
        print('*')
        temp= current
        prev=current.next
        prev.next=temp
        current=current.next.next
    return ll



lnk_lst=LinkedList()
lnk_lst.append(2)
lnk_lst.append(1)
lnk_lst.append(3)
lnk_lst.append(5)
lnk_lst.append(6)
lnk_lst.append(7)
print(lnk_lst)
print('1',swape_adjacent(lnk_lst))




