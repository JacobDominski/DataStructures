class LinkedList:
  def __init__(self):
    self.head = None
  
  def printList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next
  
  def getValue(self, index):
    temp = self.head
    
    for i in range(index):
      temp = temp.next
    
    return temp.data
  
  def length(self):
    temp = self.head
    count = 0

    while temp:
      count += 1
      temp = temp.next
    
    return count
  
  def push(self, data):
    newNode = Node(data)

    if self.head is None:
      self.head = newNode
      return
    
    last = self.head
    while last.next:
      last = last.next
    
    last.next = newNode

  def insert(self, prevNode, data):
    if prevNode is None:
      print("Error, the previous node is not inside the Linked List")
      return
    
    newNode = Node(data)

    newNode.next = prevNode.next

    prevNode.next = newNode


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
