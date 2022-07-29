class graph:
  def __init__(self,gdict=None):
    if gdict==None:
      gdict={}
    self.gdict=gdict
  def edges(self):
    return self.findedges()
  def findedges(self):
    edgename=[]
    for vtx in self.gdict:
      for nextvtx in self.gdict[vtx]:
        if({nextvtx,vtx}) not in edgename:
          edgename.append({nextvtx,vtx})
    return edgename
    

graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
print(g.edges())
