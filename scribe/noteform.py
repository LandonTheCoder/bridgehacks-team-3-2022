#! /usr/bin/python3
mystr = ("Turtles are very cool.", "They come in all shapes and sizes.", "They have green shells that protect them from danger")

import re

tmp_remlist = ['that ', 'the ', 'what ', 'and ', 'them ', '[Tt]hey ', 'have ',
               'an ', 'to', 'I ', 'my ', 'has ', "\.", "  " ]
remlist = []
for x in tmp_remlist:
    remlist.append(re.compile(x))
print(remlist)


'''
for i in range(len(splist)):
    for word in remlist:
        splist[i] = splist[i].replace(word, "")

for i in range(len(splist)):
    splist[i] = "-" + splist[i]

for i in splist:
    print(i)
'''

def filter_sentence(sentence, rmlist=remlist):
    for word in rmlist:
        # Match.sub(replace_with_string, input_sentence)
        sentence = word.sub("", sentence)
    sentence = re.compile("I'm").sub("Am", sentence)
    return " - " + sentence.strip()
def main(rmlist):
    for x in mystr:
        print(filter_sentence(x))
