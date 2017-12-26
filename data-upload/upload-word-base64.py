import os
import sys
import redis


def upload_base64(redis_db, word, base64):
    redis_db.rpush('IMGS:' + word, base64)
    print('IMGS:' + word, base64[0:50])


if __name__ == '__main__':
    redis_db = redis.StrictRedis(host=os.environ['REDIS_HOST'],
                                 port=6379,
                                 db=0,
                                 password=os.environ['REDIS_PASS'])
    fileName = sys.argv[1]
    word = os.path.splitext(fileName)[0]
    for line in open(fileName, 'r'):
        base64 = line[:-1]
        upload_base64(redis_db, word, base64)
    redis_db.ltrim('IMGS:' + word, 0, 3)
