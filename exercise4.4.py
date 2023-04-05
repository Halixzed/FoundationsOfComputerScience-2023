from collections import deque

class Shop:

    def __init__(self):
        self.line1 = deque()
        self.line2 = deque()

    def __str__(self):

        output = ["Shop\n------"]

        line1 = ["\nline 1: "]
        if self.line1_empty():
            line1.append("Is Empty")
        else:
            for person in self.line1:
                line1.append(person)
        output.append(" | ".join(line1))

        line2 = ["\nLine 2: "]
        if self.line2_empty():
            line2.append("Is Empty")
        else:
            for person in self.line2:
                line2.append(person)
        output.append(" | ".join(line2))
        
        return "".join(output)

    def line1_empty(self):
        """ Returns True if line1 is empty """
        return len(self.line1) == 0

    def line2_empty(self):
        """ Returns True if line2 is empty """
        return len(self.line2) == 0       

    def join_line1(self, person):
        """ Add the person parameter to the back of line 1 """
        self.line1.append(person)

    def join_line2(self, person):
        """ Add the person parameter to the back of line 2 """
        self.line2.append(person)

    def serve_line1(self):
        """ Serves the person at the front of line 1 """
        if self.line1_empty():
            return None
        else:
            served_person = self.line1.popleft()
            if self.line1_empty() and len(self.line2) > 1:
                self._move_person(self.line2, self.line1)
            return served_person

    def serve_line2(self):
        """ Serves the person at the front of line 2 """
        if self.line2_empty():
            return None
        else:
            served_person = self.line2.popleft()
            if self.line2_empty() and len(self.line1) > 1:
                self._move_person(self.line1, self.line2)
            return served_person 
    
    def _move_person(self, current_line, new_line):
        """ Moves the person at the back of current_line
            to the front of new_line"""
        person_to_move = current_line.pop()
        new_line.appendleft(person_to_move)      


if __name__ == "__main__":

    shop = Shop()

    print(shop)
    print()

    shop.join_line1("Carolyn")
    shop.join_line2("Arthur")

    shop.join_line1("Douglas")
    shop.join_line1("Theresa")

    shop.join_line2("Martin")
    shop.join_line2("Hester")

    shop.join_line2("Yves")
    shop.join_line2("Helena")

    print(shop)
    # Line 1: Carolyn, Douglas, and Theresa
    # Line 2: Arthuer, Martin, Hester, Yves, and Helena
    print()
    print(shop.line1_empty()) # False
    print(shop.line2_empty()) # False
    print()

    for i in range(5):
        served = shop.serve_line2()
        print(f"{served} got served...")
        print()


    print()
    
    print(shop)
    print()
    # Line 1: Carolyn, Douglas
    # Line 2: Theresa

    shop.join_line2("Karl")
    print("karl joins line 2...")
    print()

    served = shop.serve_line1()    
    print(f"{served} (finally) got served...")
    print()

    print(shop)
    print()
    # Line 1: Douglas
    # Line 2: Theresa, Karl

    served = shop.serve_line1()    
    print(f"{served} (finally) got served...")
    print()

    print(shop)
    print()
    # Line 1: Karl
    # Line 2: Theresa

    served = shop.serve_line2()
    print(f"{served} got served...")
    print()
    print(shop)
    print()
    # Line 1: Karl
    # Line 2: 

    served = shop.serve_line1()
    print(f"{served} got served...")
    print()
    print(shop)
    print()
    # Line 1: 
    # Line 2:
