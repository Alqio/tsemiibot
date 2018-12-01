# Author falarikae

def fromPlus(str):
    arr = [chr(len(i)) for i in str.split()]
    out = ''.join(arr)
    return out

def toPlus(str):
    arr = ['+' * ord(i) for i in str]
    out = ' '.join(arr)
    return out
