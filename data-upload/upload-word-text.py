import os
import sys
import redis


def upload_text(redis_db, word, text):
    redis_db.set('TEXT:' + word, text)
    print('TEXT:' + word, text)


if __name__ == '__main__':
    redis_db = redis.StrictRedis(host=os.environ['REDIS_HOST'],
                                 port=6379,
                                 db=0,
                                 password=os.environ['REDIS_PASS'])
    index = 0
    for line in sys.stdin:
        word, text = line[:-1].split("\t")
        upload_text(redis_db, word, text)
        index += 1
