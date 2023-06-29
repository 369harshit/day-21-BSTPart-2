class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.sorted_nodes = self.inorder_traversal(root)
        self.index = 0

    def inorder_traversal(self, node):
        if node is None:
            return []
        return self.inorder_traversal(node.left) + [node.val] + self.inorder_traversal(node.right)

    def next(self):
        if self.hasNext():
            val = self.sorted_nodes[self.index]
            self.index += 1
            return val
        return None

    def hasNext(self):
        return self.index < len(self.sorted_nodes)


# Example usage
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

bst_iterator = BSTIterator(root)

op = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
val = [[root], [], [], [], [], [], [], [], [], []]

output = []

for op, val in zip(op, val):
    if op == "BSTIterator":
        bst_iterator = BSTIterator(root)
        output.append(None)
    elif op == "next":
        output.append(bst_iterator.next())
    elif op == "hasNext":
        output.append(bst_iterator.hasNext())

print(output)