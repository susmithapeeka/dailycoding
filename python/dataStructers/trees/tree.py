class Tree:
  def __init__(self,value,children=[]):
    self.value=value
    self.children=children
  def __str__(self, level=0):
    ret = "  " * level + str(self.value)  + "\n"
    for child in self.children:
      ret += child.__str__(level + 1)
    return ret
  def addchild(self,Treenode):
    self.children.append(Treenode)

head=Tree("drinks",[])
cold=Tree("cold",[])
hot=Tree("hot",[])
head.addchild(cold)
head.addchild(hot)
fanta=Tree("fanta",[])
maza=Tree("maza",[])
cold.addchild(fanta)
cold.addchild(maza)
tea=Tree("Tea",[])
coffee=Tree("Coffee",[])
hot.addchild(tea)
hot.addchild(coffee)
print(head)
