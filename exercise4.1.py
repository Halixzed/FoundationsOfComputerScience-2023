from linked_list_full import LinkedList  # Imports the LinkedList class so that we can use it in this file

class StackLinkedList:
    def __init__(self):
        self._stack = LinkedList()

    def __str__(self):
        pointer = self._stack.head
        desc = ""
        while pointer != None:
            x = pointer.data
            desc += f"| {x} |\n"
            pointer = pointer.next
        desc += "-----"
        return desc

    def pop(self):
        """Returns and removes the top element of a non-empty stack"""
        if not self.is_empty():
          return self._stack.delete_first()
        else:
          return None
          
          
    
    def push(self, x):
        """Adds `x` to the top of the stack """
        return self._stack.insert_first(x)
      
      
        

    def is_empty(self):
        """ Returns True if the stack has no elements """
        if self._stack._size == 0:
          return True
        else:
          return False

    def peek(self):
        """ Returns the data in the top element of the stack """
        if not self.is_empty():        
          return self._stack.head.data
        else:
          return None
          

if __name__ == "__main__":


    stack = StackLinkedList()

    print(stack.is_empty())    # prints True

    stack.push(1)
    print(stack.peek())        # prints 1
    print(stack.is_empty())    # prints False
    stack.push(2)
    print(stack.peek())        # prints 2
    print(stack.is_empty())    # prints False
    stack.push(3)
    print(stack.peek())        # prints 3
    print(stack.is_empty())    # prints False

    stack.pop()  
    print(stack.peek())        # prints 2
    print(stack.is_empty())    # prints False
    stack.pop()  
    print(stack.peek())        # prints 1
    print(stack.is_empty())    # prints False
    stack.pop()
    print(stack.peek())        # prints None
    print(stack.is_empty())    # prints True

    print()
    
    string = "Derby"
    print(f"The string is {string} its length is {len(string)}")

    reverser_stack = StackLinkedList()
    print(reverser_stack.is_empty()) # Should print True
    print()

    for char in string:
        reverser_stack.push(char)
        
    print(reverser_stack)
    print(reverser_stack.is_empty()) # Should print False
    print(f"The top element is {reverser_stack.peek()}") # Top should be "y"
    print()

    reversed_string = ""
    while not reverser_stack.is_empty():  
        reversed_string += (reverser_stack.pop().data) # This is inefficient in Python

    print(f"The reversed string is {reversed_string} its length is {len(string)}")      # Should print The reversed string is ybreD its length is 5                      

    print(reverser_stack.is_empty()) # Should print True
