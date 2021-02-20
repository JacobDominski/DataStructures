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

# talks about stacks and queues using built in python list
# create a stack as a list
# demonstration purposes list values aren't stored next to each other in memory
stack = []
# populates the list
for i in range(10):
  stack.append(randint(0, 20))

print('Initial stack') 
print(stack) 

print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 

print()
# factorial function for recursion representing stack
def factorial(n):
  print("Function is added to the stack when 'n' equals " + str(n))
  if n == 1:
    print("No more recursion!")
    return 1
  else:
    return n*factorial(n-1)

print('\nFactorial of 4 is ' + str(factorial(4)))


print('--------') 
# queue stored in a list
queue = []
# populates queue
for i in range(10):
  queue.append(randint(0, 20))

print('Initial queue')
print(queue)

print('\nElements poped from queue:') 
print(queue.pop(0)) 
print(queue.pop(0)) 
print(queue.pop(0)) 

#-------------------------
# import queue class
from queue import Queue 
from time import sleep

print("\n-new queue-\n")
# set the queue
queue = Queue(maxsize = 10) 

for i in range(1, 11):
  sleep(0.1)
  queue.put(i)
  print("Person " + str(i) + " in line")

print('\nInitial queue')
print(queue)
print("\nQueue is full: ", queue.full()) 

# Removing element from queue 
print("\nElements dequeued from the queue") 
for i in range(1, 11):
  sleep(0.1)
  print("Person " + str(queue.get()) + " is no longer in queue") 
  
  
print("\nQueue is Empty: ", queue.empty())  
print("Queue is Full: ", queue.full()) 

# --------------------------------

from collections import deque 

queueOrStack = deque()
print()

for i in range(1, 11):
  num = randint(1, 20)
  print(num)
  queueOrStack.append(num)

while queueOrStack:
  choice = input("type 'front' or 'back' to delete an item from the data structure :>")
  if choice == "front":
    queueOrStack.popleft()
  elif choice == "back":
    queueOrStack.pop()
  else:
    print('Not a valid choice')

  print(queueOrStack)

# EXCERCISE ---------------

string = ""
letter = ""
direction = ""

while True:

  while len(letter) != 1:
    letter = input('Enter a letter :>')
  
  if direction != 'front' or direction != 'back':
    direction = input("type 'front' or 'back' to add a letter to the beginning or end of the string:>")

  if direction == "back":
    string += letter
    letter = ""
    direction = ""
    print(string)
  elif direction == "front":
    string = letter + string
    letter = ""
    direction = ""
    print(string)
  else:
    print("type front or back")
