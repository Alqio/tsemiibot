# Author falarikae

from string import ascii_lowercase as asl

asl = ''.join((' ', asl, 'åäö'))


def fromPlus(str):
    arr = [asl[len(i) - 1] for i in str.split()]
    out = ''.join(arr)
    return out


def toPlus(str):
    arr = ['+' * (asl.find(i.lower()) + 1) for i in str]
    out = ' '.join(arr)
    return out
