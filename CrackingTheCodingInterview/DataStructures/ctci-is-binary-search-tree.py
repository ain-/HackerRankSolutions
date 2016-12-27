""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    if root.left is None and root.right is None:
        return True
    elif root.left is None:
        return check(root.right, root.data, True)
    elif root.right is None:
        return check(root.left, root.data, False)
    return check(root.left, root.data, False) and check(root.right, root.data, True)


def check(root, parentData, isRight):
    if root.left is None and root.right is None:
        if isRight:
            return root.data > parentData
        return root.data < parentData
    elif root.left is None:
        return check(root.right, root.data, True)
    elif root.right is None:
        return check(root.left, root.data, False)
    return check(root.left, root.data, False) and check(root.right, root.data, True)