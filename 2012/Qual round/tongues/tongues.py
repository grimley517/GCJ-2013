# -*- coding: utf-8 *-*
import sys
import os


def translateLetter(letter):
    letters = ('a b c d e f g h i j k l m n o p q r s t u v w x y z').split()
    translations = ['y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q']
    if letter in translations:
        ind = translations.index(letter)
        return (letters[ind])
    else:
        return (letter)


def translate(message):
    outMess = ''
    for letter in message:
        if letter.isalpha:
            outMess += (translateLetter(letter))
        else:
            outMess += (letter)
    return (outMess)


infile = "~//Desktop//a-small-practice.in"
outfile = "~//Desktop//outfile.txt"
inf = open(os.path.expanduser(infile), "r")
outf = open(os.path.expanduser(outfile), 'wt')
cases = int(inf.readline())
for i in range(cases):
    messa = translate(inf.readline())
    print ('Case #%(number)s:'%{"number":(i+1)}, messa, file = outf)
inf.close()
outf.close()
