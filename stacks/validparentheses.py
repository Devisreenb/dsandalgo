"""
intput : "()[]{}"
output: true

"""

def validpare(s):
    stack = []
    open_ends = ['{',"[",'(']
    close_ends = ['}',']',')']
    for i in s:
        if i in open_ends:
            stack.append(i)
        if i in close_ends:
            if stack==[] or close_ends.index(i)!=open_ends.index(stack.pop()):
                return False
    return (True if stack ==[] else False)