import sys
from collections import Counter

# load set of words
freq = sys.argv[1]
words = set()
for line in open(freq, "r"):
    word = line[:-1].split("\t")[1]
    words.add(word)

# we count upper and lower case occurences
upper = Counter()
lower = Counter()

# go through a list of words from stdin
for line in sys.stdin:
    word = line[:-1]
    if word in words:
        :q
