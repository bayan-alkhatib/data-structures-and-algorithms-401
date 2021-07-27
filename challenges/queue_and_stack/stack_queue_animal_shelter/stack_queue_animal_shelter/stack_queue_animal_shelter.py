from stack_queue_animal_shelter.stack_and_queue import Queue

class AnimalShelter:
    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()

    def enqueue(self,animal,type):
        if type.lower() =='cat':
            return self.cat.enqueue(animal)

        elif type.lower() =='dog':
            return self.dog.enqueue(animal)

        else:
            return None


    def dequeue (self,pref):
        if pref.lower() == 'dog':
            return self.dog.dequeue()
       
        if pref.lower() =='cat':
               return self.cat.dequeue()
        else:
            return None


