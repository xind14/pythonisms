import time

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        def inorder_traversal(node):
            if node:
                yield from inorder_traversal(node.left)
                yield node.value
                yield from inorder_traversal(node.right)

        return inorder_traversal(self.root)

    def __str__(self):
        return str(list(self))

    def to_list(self):
        return list(self)

    def __repr__(self):
            return f"BinaryTree(Node({self.root.value}))" if self.root else "BinaryTree()"

    def __eq__(self, other):
        if not isinstance(other, BinaryTree):
            return False
        return list(self) == list(other)

    def __bool__(self):
        return bool(self.root)

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper