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
        if self.head == None:
            self.head = node
            self.inestance.append(self.head.value)
        else:
            current = self.head
            self.head = node
            self.head.next = current
            self.inestance.append(self.head.value)
        return value


    def include(self,value):
        """
        Return T/F if value is in the linked list or not
        """
        if value in self.inestance:
            return True
        else:
            return False


    def __str__(self):
        self.values=''
        for item in self.inestance:
            self.values=self.values+'{'+ f'{item}' +'} '+'-> '
        self.values=self.values +'NULL'
        return f'{self.values}'