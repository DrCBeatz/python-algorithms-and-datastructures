# bfs_binary_tree.py

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = Optional[TreeNode]
        self.right = Optional[TreeNode]


def bfs(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    
    visited: List[int] = []
    queue: deque[TreeNode] = deque([root])

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

    # Perform BFS
    print(bfs(roott))

if __name__ == "__main__":
    main()
