from queue_with_stacks.stack_and_queue import  Stack 


class PseudoQueue:

    def __init__(self):
        self.front=Stack()
        self.rear=Stack()

    def enqueue(self,value):
        if value!= None:
            self.front.push(value)
            return self.front.top.value
        else:
            return False

    def dequeue(self):
        try:
            if self.front == None:
                raise Exception

            while self.front.top:
                temp= self.front.pop()
                self.rear.push(temp)
            poped_value=self.rear.pop()
            while self.rear:
                back_to_front=self.rear.pop()
                self.front.push(back_to_front)
            return poped_value

        except Exception:
            return 'Error!'




        



