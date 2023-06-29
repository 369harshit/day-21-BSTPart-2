class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

def kth_smallest_element(root, k):
    inorder = inorder_traversal(root)
    if k >= 1 and k <= len(inorder):
        return inorder[k - 1]
    return None

# Example usage
root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)

k = 3
result = kth_smallest_element(root, k)
if result is not None:
    print(f"The {k}th smallest element is: {result}")
else:
    print("Invalid value of k.")
