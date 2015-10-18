__author__ = 'cmotevasselani'

import Queue


class Node:

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


def insert(root, data):
    if root is None:
        root = Node(data)
        return root
    elif data < root.value:
        temp = insert(root.left, data)
        if root.left is None:
            root.left = temp
    elif data > root.value:
        temp = insert(root.right, data)
        if root.right is None:
            root.right = temp
    elif data == root.value:
        print "data is already present"
    else:
        print "data is not accpetable"


def print_inorder(root, values=None):
    if root.left:
        print_inorder(root.left, values)
    values.append(root.value)
    if root.right:
        print_inorder(root.right, values)
    return values


def print_preorder(root, values=None):
    values.append(root.value)
    if root.left:
        print_preorder(root.left, values)
    if root.right:
        print_preorder(root.right, values)
    return values


def print_postorder(root, values=None):
    if root.left:
        print_postorder(root.left, values)
    if root.right:
        print_postorder(root.right, values)
    values.append(root.value)
    return values

def print_levelorder(root):
    nodes_visited = []
    node_queue = Queue.Queue()
    node_queue.put(root)
    while not node_queue.empty():
        node = node_queue.get()
        nodes_visited.append(node.value)
        if node.left:
            node_queue.put(node.left)
        if node.right:
            node_queue.put(node.right)
    return nodes_visited




if __name__ == "__main__":

    print "create root node with value 5"
    r = Node(5)
    insert(r, 7)
    insert(r, 8)
    insert(r, 6)
    insert(r, 3)
    insert(r, 2)
    insert(r, 4)
    insert(r, 9)


    print "inorder print:"
    print ' '.join([str(x) for x in print_inorder(r, [])])

    print "preorder print:"
    print ' '.join([str(x) for x in print_preorder(r, [])])

    print "postorder print:"
    print ' '.join([str(x) for x in print_postorder(r, [])])

    print "levelorder print:"
    print ' '.join([str(x) for x in print_levelorder(r)])

