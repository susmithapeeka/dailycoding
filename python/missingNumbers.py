from collections import Counter
def missingNumbers(arr, brr):
    # Write your code here
    a,b=Counter(arr),Counter(brr)
    missing=sorted(list(b-a))
    print(a,b)
    return missing
    
arr=[203,204,205,206,207,208,203,204,205,206]
brr=[203,204,204,205,206,207,205,208,203,206,205,206,204]
print(missingNumbers(arr,brr))
