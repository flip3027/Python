#!python3
import re

def stripRegex(string, s=None):
    if s == None:
        s = '\s'
    return re.sub(r'\A[{0}]+|[{0}]+\Z'.format(s), '', string)


text1 = 'the quick brown fox jumped over the lazy dog'
text2 = '          hello today   '
string2 = 'SpamSpamBaconSpamEggsSpamSpam'

print(stripRegex(text2,))

