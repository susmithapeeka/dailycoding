class Solution(object):
    def minimumMoves(self, stri):
        """
        :type s: str
        :rtype: int
        """
        i,res=0,0
        n=len(stri)
        while i<n:
            if stri[i]=="X":
                res+=1 
                i+=3 
            else:
                i+=1 
        return res
        
