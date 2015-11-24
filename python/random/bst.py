__author__ = 'cmotevasselani'



class Node:

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


def insert(root, data):
    if root is None:
        root = Node(data)
    elif data < root.value:
        insert(root.left, data)
    elif data > root.value:
        insert(root.right, data)
    else:
        print "data is not accpetable"


r = Node(5)
print r.value
insert(None, 5)
print "hi"


