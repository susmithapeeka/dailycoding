import math
from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        floorval=math.floor(len(A)/2)
        x=Counter(A)
        output=[]
        for i in x.elements():
            if x[i]>floorval:
                output.append(i)
        output.sort(reverse=True)
        return output[0]
