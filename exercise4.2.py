class QueueList:
    def __init__(self):
        self._queue = []
        self._size = 0

    def __str__(self):
        output = ["Front --   "]
        for current_node in self._queue:
            output.append(str(current_node))
            
        if output:
            return " | ".join(output) + f"    -- Back \n Size = {self._size}"
        else:
            return "Empty Queue"

    def enqueue(self, x):
        """ Add element x to the back of the queue """
        self._queue.append(x)
        self._size += 1

    def dequeue(self):
        """ Remove and return the element at the front of the queue """
        
        # if not self.is_empty():
        #   self._queue.pop(self._size - 1)
        #   return self._queue[self._size - 1]
        #   self._size += 1
        # else:
        #   return None

        if self.is_empty():
            return None
        self._size -= 1
        return self._queue.pop(0)

    def is_empty(self):
        """ Returns True is the queue has no elements """
        
        if self._size == 0:
          return True
        else:
          return False

    def peek(self):
        """ Return the front element of the queue """
        if not self.is_empty():         
          return self._queue[0]
        else:
          return None
          
        
        
    def size(self):
        pass

if __name__ == "__main__":
    
    bus_queue = QueueList()
    if bus_queue.is_empty():
        print("The bus queue is empty")
    else:
        print(bus_queue)
        
    bus_queue.enqueue("Arthur")
    print("Arthur joins the queue...")
    bus_queue.enqueue("Carolyn")
    print("Carolyn joins the queue...")
    bus_queue.enqueue("Douglas")
    print("Douglas joins the queue...")
    print()
    print(f"The person at the front of the queue is {bus_queue.peek()}")
    print()
    if bus_queue.is_empty():
        print("The bus queue is empty")
    else:
        print(bus_queue)
        
    person = bus_queue.dequeue()
    print(f"{person} is at the front of the queue and gets on the bus...")
    print()
    
    if bus_queue.is_empty():
        print("The bus queue is empty")
    else:
        print(bus_queue)
        
    person = bus_queue.dequeue()
    print(f"{person} is at the front of the queue and gets on the bus...")
    print()
    
    if bus_queue.is_empty():
        print("The bus queue is empty")
    else:
        print(bus_queue)

    bus_queue.enqueue("Martin")
    print("Martin joins the queue...")
    print()   

    if bus_queue.is_empty():
        print("The bus queue is empty")
    else:
        print(bus_queue)

    person = bus_queue.dequeue()
    print(f"{person} is at the front of the queue and gets on the bus...")
    print()

    person = bus_queue.dequeue()
    print(f"{person} is at the front of the queue and gets on the bus...")
    print()

    if bus_queue.is_empty():
        print("The bus queue is empty")
    else:
        print(bus_queue)
