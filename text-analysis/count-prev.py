import sys
from collections import Counter


# create Counter for each of 10k words
freq = sys.argv[1]
counters = {}
for line in open(freq, "r"):
    word = line[:-1].split("\t")[1]
    if word not in counters:
        counters[word] = Counter()


prev = '-'
# go through a list of words from stdin
for line in sys.stdin:
    word = line[:-1]
    if word in counters:
        counters[word][prev] += 1
    prev = word


def printPrev(word, counter, limit):
    l = []
    for prev, count in counter.most_common(limit):
        l.append(prev + " " + word)
    print("; ".join(l))


limit = int(sys.argv[2])
for line in open(freq, "r"):
    word = line[:-1].split("\t")[1]
    printPrev(word, counters[word], limit)
