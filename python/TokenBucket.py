__author__ = 'cmotevasselani'


from datetime import datetime
from time import sleep



class TokenBucket:

    def __init__(self, rate, max_count, start_filled=False):
        self.rate = rate             # number of tokens per second
        self.max_count = max_count      # max size of bucket
        if start_filled is True:
            self.token_count = max_count
        else:
            self.token_count = 0
        self.timestamp = datetime.now()

    # Returns True if all tokens can be taken, False otherwise
    def get_tokens(self, tokens):
        print "entering with " + str(self.token_count) + " tokens"
        print "want " + str(tokens) + " tokens"
        # TODO: implement lock
        now = datetime.now()
        timediff = (now - self.timestamp).total_seconds()
        self.timestamp = now
        num_tokens_generated = timediff * self.rate
        print "generated " + str(num_tokens_generated) + " since last get"
        self.token_count = min((self.token_count + num_tokens_generated), self.max_count)
        print "new token count: " + str(self.token_count)
        if tokens <= self.token_count:
            self.token_count -= tokens
            print "exiting True with " + str(self.token_count) + " tokens"
            return True
        else:
            print "exiting False with " + str(self.token_count) + " tokens"
            return False


if __name__ == "__main__":

    tokenBucket = TokenBucket(10, 10)

    print "Sleeping for 1 seconds" + "\n"
    sleep(1)
    print "(True) getting 10 tokens: " + str(tokenBucket.get_tokens(10)) + "\n"
    print "(False) getting 11 tokens: " + str(tokenBucket.get_tokens(11)) + "\n"
    print "(True) getting 0 tokens: " + str(tokenBucket.get_tokens(0)) + "\n"
    print "(False) getting 5 tokens: " + str(tokenBucket.get_tokens(5)) + "\n"

    print "Sleeping for 0.5 seconds" + "\n"
    sleep(500/1000.0)
    print "(False) getting 10 tokens: " + str(tokenBucket.get_tokens(10)) + "\n"
    print "(True) getting 0 tokens: " + str(tokenBucket.get_tokens(0)) + "\n"
    print "(True) getting 5 tokens: " + str(tokenBucket.get_tokens(5)) + "\n"
    print "(False) getting 1 tokens: " + str(tokenBucket.get_tokens(1)) + "\n"

    print "Sleeping for 0.05 seconds" + "\n"
    sleep(50/1000.0)
    print "(False) getting 1 tokens: " + str(tokenBucket.get_tokens(1)) + "\n"

    print "Sleeping for 0.05 seconds" + "\n"
    sleep(50/1000.0)
    print "(True) getting 1 tokens: " + str(tokenBucket.get_tokens(1)) + "\n"

    print "Sleeping for 0.05 seconds" + "\n"
    sleep(50/1000.0)
    print "(False) getting 1 tokens: " + str(tokenBucket.get_tokens(1)) + "\n"

    print "Sleeping for 0.05 seconds" + "\n"
    sleep(50/1000.0)
    print "(True) getting 1 tokens: " + str(tokenBucket.get_tokens(1)) + "\n"
