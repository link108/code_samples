__author__ = 'cmotevasselani'
from time import sleep
from TokenBucket import TokenBucket


class TokenBuckets:

    def __init__(self):
        self.buckets = {}

    def create_bucket(self, bucket_name, rate, max_count, start_filled=False):
        if bucket_name not in self.buckets:
            self.buckets[bucket_name] = TokenBucket(rate, max_count, start_filled)
            return True
        else:
            return False

    def get_from_bucket(self, bucket_name, tokens):
        print "bucket has: " + str(self.buckets[bucket_name].token_count)
        return self.buckets[bucket_name].get_tokens(tokens)


if __name__ == "__main__":

    tokenBuckets = TokenBuckets()
    print "creating buckets"
    tokenBuckets.create_bucket('first', 10, 10)
    tokenBuckets.create_bucket('second', 5, 10)

    print "sleeping for 1 second"
    sleep(1)
    print "(True) getting 10 from first: " + str(tokenBuckets.get_from_bucket('first', 10)) + "\n"
    print "(False) getting 10 from second: " + str(tokenBuckets.get_from_bucket('second', 10)) + "\n"


    sleep(50 / 1000)
    print "(False) getting 10 from first: " + str(tokenBuckets.get_from_bucket('first', 10)) + "\n"
    print "(False) getting 10 from second: " + str(tokenBuckets.get_from_bucket('second', 10)) + "\n"

