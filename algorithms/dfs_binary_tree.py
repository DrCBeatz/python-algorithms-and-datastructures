# dfs_binary_tree.py

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(node):
    if node is not None:
        print(node.value)

        dfs(node.left)
        dfs(node.right)

def main():
    # Create nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Perform DFS
    dfs(root)

if __name__ == "__main__":
    main()