
string = "ouija"

def count_vowel(input):
    count = 0
    for i in range(len(input)):
        if input[i].lower() in ["a","e","i","o","u"]:
            count += 1
        else:
            continue
    return print(count)

count_vowel(string)