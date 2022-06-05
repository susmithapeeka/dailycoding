def diagonalDifference(arr):
    # Write your code here
    n1=0
    n2=0
    n=len(arr)
    for i in range(0,n):
        n1+=arr[i][i]
        n2+=arr[i][n-i-1]
    return abs(n1-n2)
