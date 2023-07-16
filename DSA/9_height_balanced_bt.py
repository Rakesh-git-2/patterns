class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def is_balanced(root):
    # Helper function to calculate the height of a tree
    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1

    # Helper function to check if a tree is height balanced
    def is_balanced_helper(node):
        if node is None:
            return True

        left_height = height(node.left)
        right_height = height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return is_balanced_helper(node.left) and is_balanced_helper(node.right)

    return is_balanced_helper(root)


# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Check if the binary tree is height balanced
if is_balanced(root):
    print("The binary tree is height balanced.")
else:
    print("The binary tree is not height balanced.")
