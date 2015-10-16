class RingBuffer:

  def __init__(self, size):
    self.oldest = 0
    self.newest = 0
    self.values = [x for x in range(size)]
    self.flag = 0  # empty

    def add(item):
      self.values[newest] = item
      if self.newest == self.values.size() - 1:
      self.newest = 0
      else:
      self.newest++

# check if already full, then want to update oldest
      if flag and self.oldest == self.values.size() - 1:
      self.oldest = 0
      elif flag:
      self.oldest += 1

#check if full
      if self.newest == self.oldest:
      self.flag = 1 # full

      def remove():
# nothing to return
        if not flag and self.oldest == self.newest:
        return None
        value = self.value[self.oldest]
# update oldest
        if self.oldest == self.values.size() - 1:
        self.oldest = 0
        else:
        self.oldest++ 
        self.flag = 0
        return value




        ringBuffer = RingBuffer(5) [1,2,3,4,5]
        ringBuffer.add(6)   [6,2,3,4,5]  # newest=1, oldest= 0
        ringBuffer.add(7)       [6,7,3,4,5]  # newest=2, oldest=0
        ringBuffer.remove()   # newest =2, oldest =1, return 6
  ringBuffer.remove()   # newest =2, oldest =2, return 7
ringBuffer.remove()
  ringBuffer.add(8)       [6,7,8,4,5]
  ringBuffer.add(9)       [6,7,8,9,5]
  ringBuffer.add(10)      [6,7,8,9,10]   # newest=0, oldest=0
  ringBuffer.add(11)      [11,7,8,9,10]
ringBuffer.remove()

