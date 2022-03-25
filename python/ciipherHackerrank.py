import string
def caesarCipher(s, k):
    # Write your code here
    k=k%26
    alphabets=string.ascii_lowercase
    capalpha=string.ascii_uppercase
    ciipherup=capalpha[k:]+capalpha[:k]
    ciipher=alphabets[k:]+alphabets[:k]
    encrypted=""
    for x in s:
        if x.isalpha()==False:
            encrypted+=x
        else:
            if x.islower():
                k=alphabets.index(x)
                encrypted+=ciipher[k]
            else:
                k=capalpha.index(x)
                encrypted+=ciipherup[k]
    return encrypted
