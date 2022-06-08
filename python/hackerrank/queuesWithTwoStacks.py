class queue:
    def __init__(self):
        self.list1=[]
    def enqueue(self,value):
        self.list1.append(value)
    def dequeue(self):
        self.list1.pop(0)
    def peep(self):
        return self.list1[0]
    
n=int(input())
q=queue()
for x in range(n):
    j=list(map(int,input().split()))
    if j[0]==1:
        q.enqueue(j[1])
    elif j[0]==2:
        q.dequeue()
    else:
        k=q.peep()
        print(k)
        
