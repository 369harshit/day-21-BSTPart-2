class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(root, min_val=float("-inf"), max_val=float("inf")):
    if root is None:
        return True

    if root.data <= min_val or root.data >= max_val:
        return False

    return (is_bst(root.left, min_val, root.data) and is_bst(root.right, root.data, max_val))


def size_of_bst(root):
    if root is None:
        return 0

    if is_bst(root):
        return count_nodes(root)

    return max(size_of_bst(root.left), size_of_bst(root.right))


def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Testing the program

# Create a Binary Tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(8)

# Expected output: 5 (Size of the largest BST: 10, 20, 30, 50, 60)
print("Size of the largest BST:", size_of_bst(root))


""" The is_bst function recursively checks if a given subtree is a Binary Search Tree by
validatingthe values against a minimum and maximum range. """