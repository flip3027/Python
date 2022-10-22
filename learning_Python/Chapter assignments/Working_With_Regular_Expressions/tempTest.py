#! python3

import re

text = 'The soaucey quick astro barbara brown sfox blue quit qlit stick jumps over the loverazy dog'
text2 = 'The-quick-brown-fox-jumps-over-the-lazy-dog'
text3 = 'The?quick?broqwn?fox?jumps?over?the?lazy?dog?'
spaceRegex = re.compile(r'''(
\s      #find all spaces

)''',re.VERBOSE)

wordRegex = re.compile(r'''(
\w+     # find all words up to space or tab
)''',re.VERBOSE)


firstLetterRegex = re.compile(r'''(
^.
)''',re.VERBOSE)


wholeStringRegex = re.compile(r'''(
^.*
)''',re.VERBOSE)


greedyStringRegex = re.compile(r'''(
^.*
)''', re.VERBOSE)

nongreedyStringRegex = re.compile(r'''(
^.*
)''',re.VERBOSE)

startStringRegex = re.compile(r'''(
\A\w+
)''', re.VERBOSE)

endStringRegex = re.compile(r'''(
\w+\Z
)''', re.VERBOSE)

wordBoundary = re.compile(r'''(
\B\w+a|\w+a\B     #any word that has that the letter "A" in the string
)''', re.VERBOSE)

findwordBoundary = re.compile(r'''(
  #any word that start or ends that the letter in a lowercase A
\ba\w+|\w+a\b
)''', re.VERBOSE)

spaces = len(spaceRegex.findall(text))


print('there are ' + str(spaces) + ' spaces in the sentence')
print(wordRegex.findall(text),'\n')
print(firstLetterRegex.findall(text) , 'this is an first letter regex','\n')
print(wholeStringRegex.findall(text) , ' \t this is the whole string regex','\n')
print(startStringRegex.findall(text) , 'this is a start of string','\n')
print(endStringRegex.findall(text) , 'this is a end of string','\n')
print(wordBoundary.findall(text) , 'this is a word reverse boundary','\n')
print(findwordBoundary.findall(text) , 'this is a word boundary','\n')