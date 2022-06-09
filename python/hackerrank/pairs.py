def pairs(k, arr):
    # Write your code here
    a=set(arr)
    b=set(x+k for x in arr)
    return len(a&b)
