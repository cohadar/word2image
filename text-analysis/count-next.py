import sys
from collections import Counter


# create Counter for each of 10k words
freq = sys.argv[1]
counters = {}
for line in open(freq, "r"):
    word = line[:-1].split("\t")[1]
    if word not in counters:
        counters[word] = Counter()


word = '-'
# go through a list of words from stdin
for line in sys.stdin:
    nekst = line[:-1]
    if word in counters:
        counters[word][nekst] += 1
    word = nekst


def printNext(word, counter, limit):
    l = []
    for nekst, count in counter.most_common(limit):
        l.append(word + " " + nekst)
    print("; ".join(l))


limit = int(sys.argv[2])
for line in open(freq, "r"):
    word = line[:-1].split("\t")[1]
    printNext(word, counters[word], limit)
