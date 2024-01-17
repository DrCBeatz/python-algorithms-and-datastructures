# bfs_binary_tree.py

from collections import deque

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        visited.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
    
    return visited

def main():
    # Create nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Perform DFS
    print(bfs(root))

if __name__ == "__main__":
    main()
