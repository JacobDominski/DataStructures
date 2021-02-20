# linked list class to store the methods and properties
class LinkedList:
  # constructor for LinkedList
  def __init__(self):
    # self.head is the starting point
    self.head = None
  
  # method that prints all the values in the list
  def printList(self):
    # sets the temp to the starting point
    temp = self.head
    # checks if temp is not none which is the end
    while temp:
      # prints the data of that node
      print(temp.data)
      # gets the next node
      temp = temp.next
  
  # method to get a specific value
  def getValue(self, index):
    # temp stores the starting position at the head
    temp = self.head
    # iterates through the list an `index` number of times
    for i in range(index):
      # gets the next node
      temp = temp.next
    # returns the data of the node at that position
    return temp.data
  # method that returns the number of nodes in the linked list
  def length(self):
    # gets the starting position
    temp = self.head
    # count property keeps track of the number of nodes
    count = 0
    # checks if the temp is not none
    while temp:
      # increases count
      count += 1
      # gets the next node
      temp = temp.next
    
    # returns the count property
    return count
  
  # method that links a value at the end of the linked list
  def push(self, data):
    # creates a new node the the data
    newNode = Node(data)
    # checks if the starting point has a value
    if self.head is None:
      # if it doesn't then it sets the head to the node
      self.head = newNode
      # exits the method
      return
    
    # gets the starting position and sets it as the last value in the list
    last = self.head
    # check if there is a next value
    while last.next:
      # go to that next value
      # this is iterating through the list until there is no next value
      last = last.next
    
    # sets the next value to a node
    last.next = newNode
  # method that inserts a node in the middle of the list
  def insert(self, prevNode, data):
    # checks if the node is not inside the linked list
    if prevNode is None:
      print("Error, the previous node is not inside the Linked List")
      return
    
    # creates the new node with the data
    newNode = Node(data)

    # sets the new node the desired position
    newNode.next = prevNode.next
    # links the previous node to that new node so everything is connected
    prevNode.next = newNode
    
  # method that deletes the data at the value
  def delete(self, data):
    # sets the beginning to the head of the list
    temp = self.head
    # if the position is not empty and the data of the node is the desired data
    if temp is not None and temp.data == data:
      # set the head to the next node
      # which unlinks the head from the list and makes it the new head
      self.head = temp.next
      # sets the value back to none
      temp = None
      # exits the method
      return
    
    # checks if the head has a value
    while temp is not None:
      # if that node's data is the same as the desired data
      if temp.data == data:
        # break out of the loop
        break
      
      # stores the previous node to the temp to later be interconnected with the list
      prevNode = temp
      # stores the temp as the next node
      temp = temp.next
    
    # if the node doesn't have a value
    if temp is None:
      # could not find the specific value
      print("Could not find '" + str(data) + "' in the Linked List")
      # exits the method
      return
    #sets the previous node to the next node
    prevNode.next = temp.next
    # and deletes that node
    del temp
  
  # method that deletes a value at a certain index
  def deleteAt(self, position):
    # check if the starting point holds a node
    if self.head == None:
      # the list is empty
      print("This list is empty!")
      # exits the method
      return
    # sets the temp to the starting point
    temp = self.head
    # if the position is 0, that's at the beginning
    if position == 0:
      #set the head to the next node
      self.head = temp.next
      # delete the current node
      del temp
      # exit the method
      return
    # loop that iterates through the linked list
    for i in range(position-1):
      # gets the next node
      temp = temp.next
      # check if that node is empty
      if temp is None:
        # at the end of the list and keeps the current node stored in temp
        break
    # if the node is none or the next node is none
    if temp is None or temp.next is None:
      # end of the list
      print("This position is out of range!")
      # exits the method
      return
    # stores the next node
    next = temp.next.next
    # deletes the node at an index
    del temp.next
    # links the two nodes back together
    temp.next = next

# class node stores the value and the memory location of the next node
class Node:
  # constructor for the node
  def __init__(self, data):
    # keeps two properties
    self.data = data
    self.next = None
