class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)

tree = Node(1, Node(3, Node(5), Node(7)), Node(4, Node(2), Node(8)))

#广度遍历
def lookup(root):
    stack = [root]
    while stack:
        print(stack)
        current = stack.pop(0)
        print(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

#深度遍历
def deep(root):
    if not root:
        return
    print(root.val)
    deep(root.left)
    deep(root.right)

lookup(tree)
deep(tree)
