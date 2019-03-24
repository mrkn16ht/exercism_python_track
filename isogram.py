#marked with comment(#) is the original value

#def is_isogram(string):
#    pass

def is_isogram(string):
    string = string.lower()
    string = string.replace('-', '')
    string = string.replace(' ', '')
    return len(set(string)) == len(string)
