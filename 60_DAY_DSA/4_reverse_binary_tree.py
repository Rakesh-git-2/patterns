# To reverse a binary tree, you can swap the left and right child nodes of each node in the tree recursively.
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def reverse_binary_tree(root):
    if root is None:
        return

    # Swap the left and right child nodes
    root.left, root.right = root.right, root.left

    # Reverse the left and right subtrees recursively
    reverse_binary_tree(root.left)
    reverse_binary_tree(root.right)

# Example usage:
# Create a binary tree

#     4
#    / \
#   2   7
#  / \ / \
#  1 3 6 9
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Print the original tree
def print_tree_inorder(node):
    if node is None:
        return
    print_tree_inorder(node.left)
    print(node.val, end=" ")
    print_tree_inorder(node.right)

print("Original tree:")
print_tree_inorder(root)
print()

# Reverse the binary tree
reverse_binary_tree(root)

# Print the reversed tree
print("Reversed tree:")
print_tree_inorder(root)