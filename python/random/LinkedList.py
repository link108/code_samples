__author__ = 'cmotevasselani'


class Node:


    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self):
        return_node = self.tail
        new_tail = self.tail.prev
        self.tail = new_tail
        if self.tail:
          self.tail.next = None
        else:
          self.head = None
        print "returning: " + str(return_node.value)
        return return_node


    def __str__(self):
        if self.head:
            strings = []
            ptr = self.head
            while ptr is not None:
                strings.append(str(ptr.value))
                ptr = ptr.next
                if ptr:
                    strings.append("-> ")
            return ''.join(strings)
        else:
            return ""


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.pop()
print l
l.pop()
l.pop()
print l
