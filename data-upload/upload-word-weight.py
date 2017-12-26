import os
import sys
import redis


def upload_index(redis_db, index, word):
    redis_db.set('WORD:' + word, 10000 - index)
    print('WORD:' + word, 10000 - index)


if __name__ == '__main__':
    redis_db = redis.StrictRedis(host=os.environ['REDIS_HOST'],
                                 port=6379,
                                 db=0,
                                 password=os.environ['REDIS_PASS'])
    index = 0
    for line in sys.stdin:
        word = line[:-1].split("\t")[1]
        upload_index(redis_db, index, word)
        index += 1
