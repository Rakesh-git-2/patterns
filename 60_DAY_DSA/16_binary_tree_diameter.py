class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    max_diameter = 0  # Variable to track the maximum diameter

    def calculate_height_and_diameter(node):
        nonlocal max_diameter

        # Base case: an empty tree has height -1 and diameter 0
        if node is None:
            return -1, 0

        # Recursively calculate the height and diameter of the left and right subtrees
        left_height, left_diameter = calculate_height_and_diameter(node.left)
        right_height, right_diameter = calculate_height_and_diameter(node.right)

        # Calculate the height of the current node
        height = max(left_height, right_height) + 1

        # Calculate the diameter passing through the current node
        diameter = left_height + right_height + 2

        # Update the maximum diameter if necessary
        max_diameter = max(max_diameter, diameter)

        # Return the height and diameter of the current node
        return height, diameter

    calculate_height_and_diameter(root)  # Start the calculation from the root

    return max_diameter