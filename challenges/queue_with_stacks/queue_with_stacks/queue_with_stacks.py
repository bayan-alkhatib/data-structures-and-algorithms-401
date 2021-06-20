class Node():
    def __init__(self,value):
        self.value=value
        self.next=None


class Stack:

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



class PseudoQueue:

    def __init__(self):
        self.first_stack=Stack()
        self.last_stack=Stack()

    def enqueue(self,value):
        self.first_stack.push(value)
        

    def dequeue(self):
       while self.first_stack.top:
            temp= self.first_stack.pop()
            self.last_stack.push(temp)
            if self.last_stack:
                back_to_first_stack=self.last_stack.pop()
                self.first_stack.push(back_to_first_stack)


    def __str__(self):
        if self.first_stack==None:
            return 'NULL'

        else:
            values=''
            temporary_value=self.first_stack.top
            while temporary_value:
                values+='['+ f'{temporary_value.value}' +'] ' + '-> ' 
            return f'{values}'
                








newq=PseudoQueue()
newq.enqueue(5)

print(newq.first_stack.top.value)

        



