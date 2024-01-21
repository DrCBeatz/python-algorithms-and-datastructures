# invert_binary_tree.py

class TreeNode:
    def __init__(self, value: int = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def invert_tree(node: TreeNode) -> TreeNode:
    if node is None:
        return None
    
    node.left, node.right = node.right, node.left

    invert_tree(node.left)
    invert_tree(node.right)

    return node

def main():
    # Create nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Invert Binary Tree
    inverted_root = invert_tree(root)

    # Print nodes of inverted tree:
    print("Root:", inverted_root.value if inverted_root else "None")
    print("Left Child:", inverted_root.left.value if inverted_root and inverted_root.left else "None")
    print("Right Child:", inverted_root.right.value if inverted_root and inverted_root.right else "None")
    print("Right Left Child:", inverted_root.right.left.value if inverted_root and inverted_root.right and inverted_root.right.left else "None")
    print("Right Right Child:", inverted_root.right.right.value if inverted_root and inverted_root.right and inverted_root.right.right else "None")


if __name__ == "__main__":
    main()

