class Solution(object):
    def balancedStringSplit(self, s):
        countL=0
        countR=0
        total=0
        for i in s:
            if i=="R":
                countR+=1
            elif i=="L":
                countL+=1
            if countL==countR:
                total+=1
                countL=0
                countR=0
            
        return total
