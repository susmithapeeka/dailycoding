class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for i in num:
            while stack and i<stack[-1] and k:
                k-=1
                stack.pop()
            stack.append(i)
        while k:
            stack.pop()
            k-=1
        if not stack:
            return"0"
        return str(int(''.join(stack)))
