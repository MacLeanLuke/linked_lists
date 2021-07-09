from typing import NoReturn
from slnode_class import SLNode


# Just as we would pass in a value to a Python list's append method, our add_to_front method should accept a value to be added to the list:
class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):    # added this line, takes a value
        new_node = SLNode(val) #create a new instance of our Node class using the given value
        current_head = self.head # save the current head in a variable
        new_node.next = current_head # SET the new node's next to the list
        self.head = new_node # SET teh list's head to the node we created in the last step
        return self # return self to allow for chaining

    # we cannot loop through the linked list like we can for the regular list
    def print_values(self): # this method wont require any input
        runner = self.head # a pointer to the list's first node
        while (runner != None): # iterating while runner is a node and not None
            print(runner.value) # prints the current node's value
            runner = runner.next # set the runner to its neighbor
        return self # once the loop is done return self to allow for chaining

    def add_to_back(self, val): # accepts a value
        if self.head == None: # if the list is empty
            self.add_to_front(val) # run the add_to_front method
            return self # let's make sure the rest fo this function doesn't happen if we add to the front
        new_node = SLNode(val) # create a new instance of our Node class with the given value
        runner = self.head # set an iterator to start at the front of the list
        while(runner.next != None): # iterate until the iterator doesn't have a neighbor
            runner = runner.next # increment the runner to the next node in the list
        runner.next = new_node # setting the "next" value of the current last runner to point to the new node
        return self # return self to allow for chaining
