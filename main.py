# imports random and the linked list we made
from LinkedList import LinkedList
from random import randint
# creates the linked list object
linklist = LinkedList()
# for loop to populate the linked list
for i in range(10):
  # uses the push method to add a random value 
  linklist.push(randint(0, 20))


# calls the linked list method to print out all the values in the list
linklist.printList()
# calls the get value method to print out that value.
print('------')
print(linklist.getValue(1))
