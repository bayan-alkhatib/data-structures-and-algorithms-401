class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    inestance=[]

    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Adds a node of a value to the head of LL
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.inestance.append(self.head)
            return self.head
        else:
            current = self.head
            self.head = node
            node.next = current
            self.inestance.append(node.next.value)
            return node.next.value
        

    def append(self, value):
        """
        Adds a node of a value to the end of LL
        """
        node = Node(value) 
        if not self.head:
            self.head = node
            return self.head.value
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node 
            return current.next.value

    def include(self, value):
        """
        Return T/F if value is in the linked list or not
        """
        if value in self.inestance:
            return True
        else:
            return False
        

    def __str__(self):
        self.nodes=''
        for item in self.inestance:
          self.nodes=self.nodes+'{'+item+'}'+'->'
        self.nodes=self.nodes +'NULL'
        return self.nodes
        # "{ a } -> { b } -> { c } -> NULL"
        # Loop over all nodes
        # print all values in one line
    #   x=x+'{ '+f'{value}'+' }' + ' -> '
       




#     def __repr__(self):
#         # head -> node1 -> node2 -> node3 -> etc .... -> None
#         # val1 - val2 - val3
#         output = ""
#         current = self.head
#         while current:
#             value = current.value
#             if current.next is None:
#                 output += f"{value}"
#                 break
#             output = output + f"{value} - "
#             current=current.next
#         return output


# if __name__ == "__main__":
    # Instances of Node
    # n1 = Node(34)
    # n2 = Node('Suhaib')
    # n3 = Node(True)
    # print(n2.value)


    # ll = LinkedList()
    # # Value of first node on head
    # ll.append(4)
    # # next of head (next of Node(4)) is Null
    # ll.append(-1)
    # ll.append('s')
    # # I have ll: head - Node(4) -> Node(-1) -> Node('s') -> None
    # print(ll.head.value)
    # print(ll.head.next.value)
    # print(ll.head.next.next.value)
    # print(ll.__repr__())
    
ll =LinkedList()

print(ll.append('test'))
print(ll.append('h'))
print(ll.append('fdgdfgh'))
print(ll)

    
# """Insert
#     ll: head -> node(6) -> node('g') -> None
#     ll.insert(17):    head -> node(17) -> node(6) -> node('g') -> None
# """

# """Big-O
# Append: O(n)
# Insert: O(1)
# """




# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None


# class LinkedList:
#     def __init__(self):
#         head=Node()

#     def insert(self,value):
#         current=head
#         if  current == None:
#             return False

#         while current.next != None:
#            if current.next.value == value:
#                 return True
#             current=current.next
#         return False

#     def includes(self):
#         pass

#     def __str__(self,value):
#       return "{ a } -> { b } -> { c } -> NULL"

# print(Node(4))

