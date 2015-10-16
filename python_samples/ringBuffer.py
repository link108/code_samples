class RingBuffer:

    def __init__(self, size):
        self.oldest = 0
        self.newest = 0
        self.values = [x for x in range(size)]
        self.flag = 0  # Not-full: 0, Full: 1

    def add(self, item):
        self.values[self.newest] = item

        # update newest, wrap if necessary
        if self.newest == self.values.size() - 1:
            self.newest = 0
        else:
            self.newest += 1

        # check if already full, then want to update oldest
        if self.flag and self.oldest == self.values.size() - 1:
            self.oldest = 0
        elif self.flag:
            self.oldest += 1

        # check if full
        if self.newest == self.oldest:
            self.flag = 1  # full


    def remove(self):
        # nothing to return
        if not self.flag and self.oldest == self.newest:
            return None
        value = self.value[self.oldest]
        # update oldest
        if self.oldest == self.values.size() - 1:
            self.oldest = 0
        else:
            self.oldest += 1
        self.flag = 0
        return value


ringBuffer = RingBuffer(5)
ringBuffer.add(6)
ringBuffer.add(7)
ringBuffer.remove()
ringBuffer.remove()
ringBuffer.remove()
ringBuffer.add(8)
ringBuffer.add(9)
ringBuffer.add(10)
ringBuffer.add(11)
ringBuffer.remove()
