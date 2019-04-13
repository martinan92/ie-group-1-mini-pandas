def sum_numbers(a,b):
    return a + b

def tokenize(sentence, lower = False):
    if lower:
        return sentence.lower().split()
    else:
        return sentence.split()