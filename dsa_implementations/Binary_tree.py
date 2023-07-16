from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

#     4
#    / \
#   2   7
#  / \ / \
#  1 3 6 9
def dfs_preorder(root):
    if root is None:
        return []

    result = []

    def dfs_helper(node):
        if node is None:
            return

        result.append(node.val)
        dfs_helper(node.left)
        dfs_helper(node.right)

    dfs_helper(root)
    return result

def dfs_inorder(root):
    if root is None:
        return []

    result = []

    def dfs_helper(node):
        if node is None:
            return

        dfs_helper(node.left)
        result.append(node.val)
        dfs_helper(node.right)

    dfs_helper(root)
    return result

def dfs_postorder(root):
    if root is None:
        return []

    result = []

    def dfs_helper(node):
        if node is None:
            return

        dfs_helper(node.left)
        dfs_helper(node.right)
        result.append(node.val)

    dfs_helper(root)
    return result


# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform BFS on the binary tree
bfs_result = bfs(root)
print("BFS:", bfs_result)

# Perform DFS (preorder) on the binary tree
dfs_preorder_result = dfs_preorder(root)
print("DFS (Preorder):", dfs_preorder_result)

# Perform DFS (inorder) on the binary tree
dfs_inorder_result = dfs_inorder(root)
print("DFS (Inorder):", dfs_inorder_result)

# Perform DFS (postorder) on the binary tree
dfs_postorder_result = dfs_postorder(root)
print("DFS (Postorder):", dfs_postorder_result)
