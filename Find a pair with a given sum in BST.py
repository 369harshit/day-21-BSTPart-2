class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

def find_target(root, k):
    inorder = inorder_traversal(root)
    for i in range(len(inorder)):
        for j in range(i+1, len(inorder)):
            if inorder[i] + inorder[j] == k:
                return True
    return False

# Example usage
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

k = 9
result = find_target(root, k)
print(result)
