import string

def caesar(cipher):
    cipher = cipher.lower()
    encrypted = []
    alphabet = list(string.ascii_lowercase)
    for i in cipher:
        for l in range(len(alphabet)):
            if i == alphabet[l]:
                encrypted.append(alphabet[l+1])
    return "".join(encrypted)

print(caesar("This is a test"))