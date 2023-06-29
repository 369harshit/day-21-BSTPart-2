class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def ceil(root, value):
    if root is None:
        return None
    
    if root.key == value:
        return root.key
    
    if root.key < value:
        return ceil(root.right, value)
    
    left_ceil = ceil(root.left, value)
    if left_ceil is not None and left_ceil >= value:
        return left_ceil
    
    return root.key

# Example usage
# Constructing the BST
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(6)


value = 7
result = ceil(root, value)
print("Ceil value of", value, "in the BST is:", result)
