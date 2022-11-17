class Node(object):
    def __init__(self, data, right = None, left = None):
        self.left = left
        self.right = right
        self.data = data

def countNode(root):
    print(root)
    if root == None:
        return 0
    return countNode(root.left) + countNode(root.right) + 1

if __name__ == '__main__':
    rootl = Node(1, None, None)
    rootr = Node(3, None, None)
    root = Node(2, rootl, rootr)
    print(root.left)
    print(countNode)

