class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self):
        head=Node()

    def insert(self,value):
        current=head
        if  current == None:
            return False

        while current.next != None:
           if current.next.value == value:
                return True
            current=current.next
        return False

    def includes(self):
        pass

    def __str__(self,value):
      return "{ a } -> { b } -> { c } -> NULL"

print(Node(4))

