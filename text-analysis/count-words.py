import sys, re
from collections import Counter

cnt = Counter()
dict = {}
for line in sys.stdin:
	words = [w.lower() for w in line.split() if len(w) > 1]
	for w in words:
		cnt[w] += 1

for w, c in cnt.most_common(10000):
	print(str(c) + " " + w)