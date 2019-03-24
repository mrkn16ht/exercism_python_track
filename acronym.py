#marked with comment(#) is the original value

##def abbreviate(words):
##    pass

import re

def abbreviate(words):
    words = re.findall(r'[a-zA-Z\']+', words.upper())
##reminder    words = [a[0] for a in words]
##reminder    words = ''.join(words)
    words = ''.join([a[0] for a in words])
    return words
