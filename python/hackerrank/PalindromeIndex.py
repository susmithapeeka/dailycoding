
def palindromeIndex(s):
    # Write your code here
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            newstr = s[:i] + s[i+1:] 
            if newstr[:] == newstr[::-1]:
                return i
            return -(i+1)+len(s)
    return -1
