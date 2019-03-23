#marked with comment(#) is the original value

#def word_count(phrase):
#    pass

from collections import Counter
import re

def word_count(phrase):
    words = re.findall(r"[a-zA-Z0-9\']+", phrase.lower())
    words = [x.strip("'") for x in words]
    words = dict(Counter(words))
    return words
