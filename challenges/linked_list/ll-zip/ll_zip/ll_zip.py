from linked_list import LinkedList

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


def zip(l1,l2):
    zip_ll=LinkedList()
    current1=l1.head
    current2=l2.head

    while current1:
        zip_ll.append(current1.value)
        current1=current1.next

        if current2:
            zip_ll.append(current2.value)
            current2=current2.next

    while current2 and not current1:
        zip_ll.append(current2.value)
        current2=current2.next

    return zip_ll


l1=LinkedList()
l1.append(1)
l1.append(3)
l1.append(2)
l2=LinkedList()
l2.append(5)
l2.append(9)
# l2.append(4)
print(l1)
print(l2)
print(zipLists(l1,l2))
print(zip(l1,l2))
