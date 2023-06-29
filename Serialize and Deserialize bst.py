class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return ""
    serialized = []
    serialize_helper(root, serialized)
    return ",".join(serialized)

def serialize_helper(node, serialized):
    if not node:
        serialized.append("#")
        return
    serialized.append(str(node.val))
    serialize_helper(node.left, serialized)
    serialize_helper(node.right, serialized)

def deserialize(data):
    if not data:
        return None
    serialized = data.split(",")
    return deserialize_helper(serialized)

def deserialize_helper(serialized):
    if not serialized:
        return None
    value = serialized.pop(0)
    if value == "#":
        return None
    node = TreeNode(value)
    node.left = deserialize_helper(serialized)
    node.right = deserialize_helper(serialized)
    return node

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Serialize the binary tree
serialized_tree = serialize(root)
print("Serialized tree:", serialized_tree)

# Deserialize the binary tree
deserialized_tree = deserialize(serialized_tree)

# Verify the deserialized tree by re-serializing and comparing with the original
re_serialized_tree = serialize(deserialized_tree)
print("De-serialized tree:", re_serialized_tree)
