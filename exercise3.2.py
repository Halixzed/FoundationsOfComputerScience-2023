""" A doubly linked list using classes"""

class Node:
  """ Stores some data and a reference to the next and previous nodes."""

  def __init__(self, data):
    self.data = data
    self.next = None  # The next node
    self.prev = None  # The previous node

  def __str__(self):
    return "Node : {0}".format(self.data)

class LinkedList:
  "A doubly linked list"

  def __init__(self):
    self._size = 0
    self.head = None
    self.tail = None

  def size(self):
    return self._size

  def add_first(self, data):
    """ Add a new node, with the given data, as the first node in the list"""
    new_node = Node(data)
    if self._size == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node
    self._size += 1

  def remove_first(self):
    """Remove the first node from the list"""
    if self.head is None:
      return None

    if self.head == self.tail:
        self.head = None
        self.tail = None
    else:
        
        new_head = self.head.next
        new_head.prev = None
        self.head = new_head
      
    self._size -= 1

  def add_last(self, data):
    """ Add a new node, with the given data, as the last node in the list"""
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self._size += 1

  def insert_at(self, index, data):
    """ Add new node with the given data at the given index """
    if index < 0 or index > self._size:
        raise Exception("Index out of range")

    if index == 0:
        self.add_first(data)
    elif index == self._size:
        self.add_last(data)
    else:
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            current = current.next
        next_node = current.next
        new_node.prev = current
        new_node.next = next_node
        current.next = new_node
        next_node.prev = new_node
        self._size += 1

  def __str__(self):
    current_node = self.head
    output = []
    while current_node != None:
      output.append(str(current_node))
      current_node = current_node.next

    if output:
      return " -> ".join(output)
    else:
      return "Empty List"

if __name__ == "__main__":

  linked_list1 = LinkedList()    
  linked_list1.add_first("A")
  linked_list1.add_first("B")
  print(linked_list1)          # Should print Node : B -> Node : A
  print(linked_list1.size())   # Should print 2
  
  linked_list1.remove_first()
  print(linked_list1)          # Should print Node : A
  print(linked_list1.size())   # Should print 1
  print(linked_list1.head)     # Should print Node : A
  print(linked_list1.tail)     # Should print Node : A

  linked_list1.remove_first()
  print(linked_list1)          # Should print Empty List
  print(linked_list1.size())   # Should print 0
  print(linked_list1.head)     # Should print None
  print(linked_list1.tail)     # Should print None

  linked_list1.add_last("B")
  linked_list1.remove_first()
  print(linked_list1)          # Should print Empty List 
  print(linked_list1.size())   # Should print 0

  linked_list1.add_first("R")
  linked_list1.add_first("E")
  linked_list1.add_first("D")
  linked_list1.add_last("Y")
  linked_list1.insert_at(3, "B")
  print(linked_list1)          # Should print Node : D -> Node : E -> Node : R -> Node : B -> Node : Y
  print(linked_list1.size())   # Should print 5
  
  linked_list1.remove_first()
  linked_list1.remove_first()
  linked_list1.remove_first()
  linked_list1.add_last("A")
  linked_list1.insert_at(1,"S")
  print(linked_list1)          # Node : B -> Node : S -> Node : Y -> Node : A
  print(linked_list1.size())   # Should print 4

  linked_list2 = LinkedList()

  linked_list2.insert_at(0,"R")
  linked_list2.insert_at(1,"O")
  linked_list2.insert_at(0,"P")
  linked_list2.insert_at(0,"U")

  print(linked_list2)                   # Should print Node : U -> Node : P -> Node : R -> Node : O
  print(linked_list2.size())            # Should print 4

  linked_list3 = LinkedList()
  linked_list3.add_last("W")
  linked_list3.add_last("E")
  print(linked_list3)                   # Should print Node : W -> Node : E
  print(linked_list3.size())            # Should print 2
