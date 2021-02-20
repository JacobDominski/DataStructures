
from LinkedList import LinkedList
from random import randint

linklist = LinkedList()

for i in range(10):
  linklist.push(randint(0, 20))



linklist.printList()
print('------')
print(linklist.getValue(1))
