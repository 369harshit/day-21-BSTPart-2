class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def floor(root, value):
    if root is None:
        return None
    
    if root.key == value:
        return root.key
    
    if root.key > value:
        return floor(root.left, value)
    
    right_floor = floor(root.right, value)
    if right_floor is not None and right_floor <= value:
        return right_floor
    
    return root.key

# Example usage
# Constructing the BST
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(6)

value = 7
result = floor(root, value)
print("Floor value of", value, "in the BST is:", result)
