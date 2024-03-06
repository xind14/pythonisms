import pytest
import time
from main import BinaryTree, Node, timer

def test_iter():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    tree = BinaryTree(root)

    expected_values = [4, 2, 5, 1, 6, 3, 7]
    assert list(tree) == expected_values

def test_str():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    tree = BinaryTree(root)

    assert str(tree) == "[2, 1, 3]"

def test_to_list():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    tree = BinaryTree(root)

    assert tree.to_list() == [2, 1, 3]

def test_repr():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    tree = BinaryTree(root)

    assert repr(tree) == "BinaryTree(Node(1))"

def test_eq():
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)

    tree1 = BinaryTree(root1)
    tree2 = BinaryTree(root2)

    assert tree1 == tree2

def test_bool():
    empty_tree = BinaryTree()
    non_empty_tree = BinaryTree(Node(1))

    assert not bool(empty_tree)
    assert bool(non_empty_tree)

def test_timer():
    @timer
    def slow_function():
        time.sleep(2)
        return "Done"

    result = slow_function()
    assert result == "Done"

def test_node():
    node = Node(5)
    assert node.value == 5
    assert node.left is None
    assert node.right is None

if __name__ == "__main__":
    pytest.main()
