import sys
from collections import Counter

lower_cnt = Counter()
any_cnt = Counter()
dict = {}
for word in sys.stdin:
    lower_cnt[word[:-1].lower()] += 1
    any_cnt[word[:-1]] += 1

limit = int(sys.argv[1])
for word, count in lower_cnt.most_common(limit):
    # if more than half occurences are Title cased, preserve case.
    if any_cnt[word.title()] * 2 >= count:
        print(str(count) + "\t" + word.title())
    else:
        print(str(count) + "\t" + word)
