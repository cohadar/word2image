import sys
from collections import Counter


# load the freq file
freq = sys.argv[1]
counts = {}
nline = 0
for line in open(freq, "r"):
    word = line[:-1].split("\t")[1]
    counts[word] = nline
    nline += 1

counter = Counter()
# go through a list of words from stdin
for line in sys.stdin:
    word = line[:-1]
    if word in counts:
        counter[word] = 10000 - counts[word]
    elif word.lower() in counts:
        counter[word] = 10000 - counts[word.lower()]
    elif word.title() in counts:
        counter[word] = 10000 - counts[word.title()]
    else:
        counter[word] = 0

for word, count in counter.most_common(10000):
    print(str(10000 - count) + "\t" + word)
