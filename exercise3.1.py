""" A singly linked list using classes"""

class Node:
  """ Stores some data and a reference to the next node."""

  def __init__(self, data):
    self.data = data
    self.next = None  # The next node

  def __str__(self):
    return "Node : {0}".format(self.data)

class LinkedList:
  "A singly linked list"

  def __init__(self):
    self.head = None
    self._size = 0

  def size(self):
    return self._size

  def add_first(self, data):
    """ Add a new node, with the given data, as the first node in the list"""

    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self._size += 1

  def remove_first(self):
    """Remove the first node from the list"""

    if self.head is None:
      return None
    self.head = self.head.next
    self._size -= 1

    

  def insert_at(self, index, data):
    """ Add new node with the given data at the given index """
    
    if index < 0 or index > self._size:
      raise Exception("Index out of range")
  

    if index == 0:
      self.add_first(data)
    else:
      new_node = Node(data)
      current_node = self.head
      for i in range(index-1):
        current_node = current_node.next
      next_node = current_node.next
      current_node.next = new_node
      new_node.next = next_node
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
  print(linked_list1)           # Should print Node : A

  linked_list1.add_first("B")
  linked_list1.add_first("C")
  print(linked_list1)           # Should print Node : C -> Node : B -> Node : A
  print(linked_list1.size())    # Should print 3


  linked_list2 = LinkedList()
  linked_list2.remove_first()   
  print(linked_list2)           # Should print Empty List
  print(linked_list2.size())    # Should print 0

  linked_list2.add_first("B")
  linked_list2.remove_first()

  print(linked_list2)           # Should print Empty List

  print(linked_list2.size())    # Should print 0

  linked_list3 = LinkedList()

  linked_list3.add_first("R")
  linked_list3.add_first("E")
  linked_list3.add_first("D")

  linked_list3.insert_at(3, "B")
  linked_list3.insert_at(4, "Y")

  print(linked_list3)            # Should print Node : D -> Node : E -> Node : R -> Node : B -> Node : Y
  print(linked_list3.size())     # Should print 5
  

  linked_list3.remove_first()
  linked_list3.remove_first()
  linked_list3.remove_first()

  linked_list3.add_first("A")

  print(linked_list3)            # Should print Node : A -> Node : B -> Node : Y
  
  print(linked_list3.size())     # Should print 3

  linked_list4 = LinkedList()
  linked_list4.insert_at(0,"S")
  linked_list4.insert_at(1,"T")
  print(linked_list4)            # Should print Node : S -> Node : T
