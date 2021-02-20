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


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
