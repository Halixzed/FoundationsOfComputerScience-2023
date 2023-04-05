class Score:
  """ Stores a player name and their score """

  def __init__(self, name, score):
    self.name = name
    self.score = score
    self.next = None  # Next (lower) score
    self.prev = None  # Previous (higher) score

  def __str__(self):
    return f"{self.name} : {self.score}"

class HighScores:
  """ Stores the top five high scores """

  # Initialise and manually set the capacity parameter to 5
  def __init__(self, capacity=5):
    """Initialise the class"""
    self._capacity = capacity
    self._no_scores = 0
    self.head = None
    self.tail = None 

  def __str__(self):
    current = self.head
    output = []
    while current != None:
      output.append(str(current))
      current = current.next

    return "\n".join(output)

  def _node_to_replace(self, new_score):
    """" Returns the node that
        the new score should replace, i.e. we shoul add the new score here and then link to this node"""
    current = self.head
    while current != None and current.score >= new_score.score:
      current = current.next

    return current

  def _delete_last(self):
    last_node = self.tail
    self.tail = last_node.prev
    self.tail.next = None

  def add_score(self, name, score):  
    """Add a new Score object to the list, with the name and score parameters, if the list is not full or the score parameter is higher than the lowest stored score. The newly added Score object should be added at the right place to keep the list in order of score."""
    new_score = Score(name, score)
    
    if self.head == None:
      # The list is empty
      self.head = new_score
      self.tail = new_score
      self._no_scores += 1
      return

    node_to_replace = self._node_to_replace(new_score)
    if self._no_scores < self._capacity or node_to_replace != None:
      # Add the new score to the list
      if node_to_replace == self.head:
        # The new score is the new highest score
        new_score.next = self.head
        self.head.prev = new_score
        self.head = new_score
      elif node_to_replace == None:
        # The new score is the new lowest score
        new_score.prev = self.tail
        self.tail.next = new_score
        self.tail = new_score
      else:
        # The new score is somewhere in the middle
        new_score.next = node_to_replace
        new_score.prev = node_to_replace.prev
        node_to_replace.prev.next = new_score
        node_to_replace.prev = new_score

      self._no_scores += 1
      
      if self._no_scores > self._capacity:
        # Remove the lowest score
        self._delete_last()
        
if __name__ == "__main__":
  
  score_board = HighScores(capacity=5)
  score_board.add_score("Carolyn", 250)
  score_board.add_score("Martin", 199)

  print("+++ High Scores +++")
  print(score_board)  # Order: Carolyn, Martin
  print()

  score_board.add_score("Douglas", 251)
  score_board.add_score("Arthur", 28)
  score_board.add_score("Theresa", 233)

  print("+++ High Scores +++")
  print(score_board)  # Order: Douglas, Carolyn, Theresa, Martin, Arthur
  print()

  score_board.add_score("Herc", 120)

  print("+++ High Scores +++")
  print(score_board)  # Order: Douglas, Carolyn, Theresa, Martin, Herc
  print()
  
  score_board.add_score("Matt", 300)

  print("+++ High Scores +++")
  print(score_board)  # Order: Matt Douglas, Carolyn, Theresa, Martin
  print()

  hs = HighScores()
  
  hs.add_score("test 10", 10)
  hs.add_score("test 20", 20)
  hs.add_score("test 30", 30)
  hs.add_score("test 40", 40)
  hs.add_score("test 50", 50)
  hs.add_score("test 60", 60)
  hs.add_score("test 70", 70)
  print("+++ High Scores +++")
  print(hs) # Order: test 70, test 60, test 50, test 40, test 30
  print()
  
  hs = HighScores(capacity=6)
  hs.add_score("test 10", 10)
  hs.add_score("test 20", 20)
  hs.add_score("test 30", 30)
  hs.add_score("test 40", 40)
  hs.add_score("test 50", 50)
  hs.add_score("test 60", 60)
  hs.add_score("test 70", 70)
  print("+++ High Scores +++")
  print(hs) # Order: test 70, test 60, test 50, test 40, test 30, test 20
  print()
  
  hs = HighScores(capacity=2)
  
  hs.add_score("test 10", 10)
  hs.add_score("test 20", 20)
  hs.add_score("test 30", 30)
  hs.add_score("test 40", 40)
  hs.add_score("test 50", 50)
  hs.add_score("test 60", 60)
  hs.add_score("test 70", 70)
  print("+++ High Scores +++")
  print(hs) # Order: test 70, test 60
