import sys
from collections import Counter

cnt = Counter()
dict = {}
for word in sys.stdin:
    cnt[word[:-1].lower()] += 1

limit = int(sys.argv[1])
for w, c in cnt.most_common(limit):
    print(str(c) + "\t" + w)
