import string
from collections import deque

def caesarCipher(s, k):
    alpha=string.ascii_lowercase
    d=deque(string.ascii_lowercase)
    print(d)
    d.rotate(-k) 
    print(d)
    new=''
    for letter in s:
        if letter.lower() in alpha:
            if letter.isupper():
                new+=d[alpha.index(letter.lower())].upper()
            else: 
                new+=d[alpha.index(letter)]
        else:
            new+=letter
    return new
            


print(caesarCipher("middle-Outz",2))
