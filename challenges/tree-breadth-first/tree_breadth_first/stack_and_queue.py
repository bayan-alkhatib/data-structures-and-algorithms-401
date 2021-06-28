class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        self.left=None
        self.right=None



class Stack():
    def __init__(self):
        self.top=None

    def push(self,value):
        temp=self.top
        self.top=Node(value)
        self.top.next=temp
        return self.top.value

    def pop(self):
        try:
            if self.top ==None:
               raise Exception
            
            temp=self.top
            self.top=self.top.next
            return temp.value
        
        except Exception:
            return 'Error!'    

    def peek(self):
        try:
            if self.top ==None:
               raise Exception

            return self.top.value

        except Exception:
            return 'Error!'

    def isEmpty(self):
         return self.top ==None



class Queue():
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue (self,value):
        node=Node(value)
        if self.rear==None:
            self.front=node
            self.rear=node
            # return self.rear.value
        else:
            self.rear.next=node
            self.rear=node
            # return self.rear.value

    def dequeue(self):
        try:
            if self.front == None:
                raise Exception

            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp


        except Exception:
            return 'Error!'

#    def dequeue(self):
#         """Method that removes the node from the front of the queue, and returns the node's value."""
#         if not self.is_empty():
#             temp = self.front
#             self.front = self.front.next
#             temp.next = None
#             return temp
#         else:
#             return None
    def peek (self):
        try:
            if self.front == None:
                raise Exception

            return self.front.value

        except Exception:
            return 'Error!'

    def isEmpty(self):
        return self.front==None


