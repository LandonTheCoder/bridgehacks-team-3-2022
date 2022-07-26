#! /usr/bin/python3
mystr = ("Turtles are very cool.", "They come in all shapes and sizes.", "They have green shells that protect them from danger")

import re

tmp_remlist = ['that ', 'the ', 'what ', 'and ', 'them ', '[Tt]hey ', 'have ',
               'an ', 'to', 'I ', 'my ', 'has ', "\.", "  " ]
remlist = []
for x in tmp_remlist:
    remlist.append(re.compile(x))
##print(remlist)

tmp_sublist = [("I'm", "Am")]
sublist = {}
for x in tmp_sublist:
    sublist[re.compile(x[0])] = x[1]
##print(sublist)

def filter_sentence(sentence, rmlist=remlist):
    for word in rmlist:
        # Match.sub(replace_with_string, input_sentence)
        sentence = word.sub("", sentence)
    for x in sublist.keys():
        sentence = x.sub(sublist[x], sentence)
    return " - " + sentence.strip()
def main(rmlist):
    for x in mystr:
        print(filter_sentence(x))
