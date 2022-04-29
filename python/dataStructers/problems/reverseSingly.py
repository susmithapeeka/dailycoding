class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
class SinglyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  def insertSLL(self,value,location):
    nn=Node(value)
    if self.head==None:
      self.head=nn
      self.tail=nn
    else:
      if location==0:
        nn.next=self.head
        self.head=nn
      elif location==-1:
        nn.next=None
        self.tail.next=nn
        self.tail=nn
      else:
        tempp=self.head
        index=0
        while(index<location-1):
          index+=1 
          tempp=tempp.next
        preserve=tempp.next
        tempp.next=nn
        nn.next=preserve
        if tempp==self.tail:
          self.tail=tempp
  def printLL(self):
    n=self.head
    if self.head==None:
      print("No elements")
    else:
      while(n is not None):
        print(n.value, end=" ")
        n=n.next
  def reverse(self):
    list1=[]
    n=self.head
    while(n is not None):
        list1.append(n.value)
        n=n.next
    while(list1):
      print(list1.pop(),end=" ")
    return "done"
        

singlyLinkedList=SinglyLinkedList()
singlyLinkedList.insertSLL(1,0)
singlyLinkedList.insertSLL(2, 0)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(5,-1)
singlyLinkedList.printLL()
print()
singlyLinkedList.reverse()
