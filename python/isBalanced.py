def isBalanced(s):
    # Write your code here
    while "[]" in s or "{}" in s or "()" in s:
        s = s.replace('{}', '' )
        s = s.replace('[]', '')
        s = s.replace('()', '')
    if len(s) == 0:
        return("YES")
    else:
        return("NO")
