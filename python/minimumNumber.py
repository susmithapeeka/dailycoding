def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    MIN_LENGTH = 6
    charsToChange = 0
    
    if not re.search('[0-9]', password): charsToChange += 1
    if not re.search('[A-Z]', password): charsToChange += 1
    if not re.search('[a-z]', password): charsToChange += 1 
    if not re.search(r'[!@#$%^&*()\-+]', password): charsToChange += 1
    
    return max(MIN_LENGTH - len(password), charsToChange) if n < 6 else charsToChange
