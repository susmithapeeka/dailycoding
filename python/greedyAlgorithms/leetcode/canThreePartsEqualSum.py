class Solution(object):
    def canThreePartsEqualSum(self, arr):
        summation=sum(arr)
        if summation%3!=0:
            return False
        goal=summation//3
        partition=0
        currsum=0
        for i in arr:
            currsum+=i
            if currsum==goal:
                currsum=0
                partition+=1
        if partition>=3:
            return True
        return False
