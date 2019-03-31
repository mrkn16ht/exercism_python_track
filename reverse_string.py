# marked with comment(#) is the original value

# def reverse(text):
#     pass

# 1:
def reverse(text):
    revtext = text[::-1]
    return revtext

# 2:
# revtext=''.join(reversed(text))
# return revtext

# 3:
# revtext=list(text)
# revtext.reverse()
# revtext=''.join(revtext)
# return revtext