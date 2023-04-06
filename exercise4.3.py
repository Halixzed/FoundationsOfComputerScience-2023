#main.py 
from queue import Queue
from stack import Stack


class Score:
  """ Stores a player name and their score """

  def __init__(self, name, score):
    self.name = name
    self.score = score

  def __str__(self):
    return f"{self.name} : {self.score}"


class ScoreDisplay:

  def __init__(self):
    self.scores = Queue()
    self.highest_first = True  # Is the queue sorted highest first? Defaults to True

  def __str__(self):

    return str(self.scores)

    oldScores = self.scores
    self.scores = Queue()
    current_node = oldScores.peek()

    if self.highest_first:
      output = ["Highest Score --   "]
    else:
      output = ["Lowest Score --   "]

    while current_node != None:
      item = oldScores.dequeue()
      output.append(str(item))
      self.scores.enqueue(item)
      current_node = oldScores.peek()

    return " | ".join(output) + f"    -- \n Size = {self.scores.size()} \n"


  def add_score(self, name, score):
    self.scores.enqueue(Score(name, score))
   
    """ Adds a score to the back of the scores queue """

    pass

  def _queue_to_stack(self):
    stack = Stack()
    while not self.scores.is_empty():
      stack.push(self.scores.dequeue())
    return stack
    """ dequeues each element of the scores queue onto a stack and returns the stack """

    pass

  def _stack_to_queue(self, stack):
    while not stack.is_empty():
      self.scores.enqueue(stack.pop())
    """ Enqueues each element of the stack parameter into the scores queue """
   
    pass

  def reverse(self):
    """ Reverses the scores queue and toggles the highest_first flag """
    temp_stack = self._queue_to_stack()
    self._stack_to_queue(temp_stack)
    self.highest_first = not self.highest_first

    # Read the scores queue into temp_stack ( should call _queue_to_stack() )

    # Read temp_stack back into the score queue ( should call _stack_to_queue() )

    # Toggle the highest_first flag
   
    pass

if __name__ == "__main__":

  display = ScoreDisplay()
  print(display)

  display.add_score("Douglas", 251)
  display.add_score("Carolyn", 250)
  display.add_score("Theresa", 233)
  display.add_score("Martin", 199)
  display.add_score("Arthur", 28)

  print(display)

  display.reverse()

  print(display)

  display.reverse()

  print(display)


#queue.py

class Queue:

 def __init__(self):
    self.items = []

 def __str__(self):
    return f"Queue Object: {self.items}"

 def enqueue(self, x):
    """ Add element x to the back of the queue """
    self.items.append(x)

 def dequeue(self):
    """ Remove and return the element at the front of the queue """
    if not self.is_empty():
        return self.items.pop(0)
    else:
        return None

 def is_empty(self):
    """ Returns True is the queue has no elements """
    return len(self.items) == 0
 
 def peek(self):
    """ Return the front element of the queue """
    if not self.is_empty():
        return self.items[0]
    else:
        return None

 def size(self):
    """ Returns the size of the queue """
    return len(self.items)

  
  #stack.py
  
  class Stack:

 def __init__(self):
    self.items = []

 def __str__(self):
    return f"Stack Object: {self.items}"

 def pop(self):
    """Returns and removes the top element of a non-empty stack"""
    if not self.is_empty():
        return self.items.pop()
    else:
        return None

 def push(self, x):
    """Adds `x` to the top of the stack """
    self.items.append(x)

 def is_empty(self):
    """ Returns True if the stack has no elements """
    return len(self.items) == 0

 def peek(self):
    """ Returns the data in the top element of the stack """
    if not self.is_empty():
        return self.items[-1]
    else:
        return None

 def size(self):
    """ Returns the size of the stack"""
    return len(self.items)
