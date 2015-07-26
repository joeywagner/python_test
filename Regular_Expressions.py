# coding=utf-8
__author__ = 'Joe'
# Using the er function
import re
count = 0

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        count = count + 1
        print line
        #print line
print "THIS IS THE TOTAL:", count


#import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        count = count + 1
        print line
print "THIS IS THE TOTAL:", count

#the caret used in regular expresions will only pull lines that the match the begining of the line
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        count = count + 1
        print line
print "THIS IS THE TOTAL:", count


#Charater matching in regular expressions
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line) :
        count = count + 1
        print line
print "THIS IS THE TOTAL:", count

#Extracting data using regualar expressions

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@',line):
        count = count + 1
        print line
print "THIS IS THE TOTAL:", count















