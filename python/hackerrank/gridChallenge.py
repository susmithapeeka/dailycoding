def gridChallenge(grid):
    # Write your code here
    grid = [sorted(element) for element in grid]
    for i in range(len(grid)):
        try:
            column = [string[i] for string in grid]
            
            if column != sorted(column):
                return 'NO'
        except:
            pass
    return 'YES'
