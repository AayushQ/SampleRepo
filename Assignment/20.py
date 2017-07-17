"""
20.Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
"""
from collections import Counter
word_count = Counter()
with open('txt.txt', 'r') as f:
    for line in f:
        for word in line.split(" "):
            word_count[word.strip().lower()] += 1

for word, count in word_count.iteritems():
    print "word: {}, count: {}".format(word, count)

