class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def isBST(node):
    if node is None:
        return True

    if node.left is not None and node.left.value >= node.value:
        return False

    if node.right is not None and node.right.value <= node.value:
        return False

    return isBST(node.left) and isBST(node.right)


def sumBST(node):
    if node is None:
        return 0

    return sumBST(node.left) + node.value + sumBST(node.right)


def maxSumBST(root):
    if root is None:
        return 0

    max_sum = float('-inf')

    # Traverse each node in the tree
    stack = [root]
    while stack:
        node = stack.pop()

        if isBST(node):
            current_sum = sumBST(node)
            max_sum = max(max_sum, current_sum)

        if node.left is not None:
            stack.append(node.left)

        if node.right is not None:
            stack.append(node.right)

    return max_sum


# Example usage
# Creating the binary tree
root = TreeNode(4)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)


# Finding the maximum sum BST
max_sum = maxSumBST(root)
print("Maximum Sum BST:", max_sum)
