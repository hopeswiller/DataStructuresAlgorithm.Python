#           10
#         /    \
#       12      15
#     /   \     / \
#    25   30   36  40
#   / \     \   \  /
#  14 16    18  19 20

from __future__ import annotations

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinaryTree:

    (
        preorder,
        postorder, inorder, levelorder
    ) = [], [], [], []

    def __init__(self, root: Node):
        self.root = root

    def showTree(self, tree):
        pass

    def isTreeEmpty(self) -> bool:
        if not self.root:
            return True
        return False

    # traversal operations
    @classmethod
    def preOrderTraversal(cls, node: Node) -> list:
        """root -> left -> right"""
        if node is not None:
            cls.preorder.append(node.key)
            cls.preOrderTraversal(node.left)
            cls.preOrderTraversal(node.right)

        return cls.preorder

    @classmethod
    def postOrderTraversal(cls, node: Node):
        """left -> right -> root"""
        if node is not None:
            cls.postOrderTraversal(node.left)
            cls.postOrderTraversal(node.right)
            cls.postorder.append(node.key)

        return cls.postorder

    @classmethod
    def inOrderTraversal(cls, node: Node):
        """left -> root -> right"""
        if node is not None:
            cls.inOrderTraversal(node.left)
            cls.inorder.append(node.key)
            cls.inOrderTraversal(node.right)

        return cls.inorder

    @classmethod
    def levelOrderTraversal(cls, node: Node):
        pass


tree = BinaryTree(
    root=Node(
        key=10,
        left=Node(
            key=12,
            left=Node(25, left=Node(14), right=Node(16)),
            right=Node(30, right=Node(18)),
        ),
        right=Node(
            key=15,
            left=Node(36, right=Node(19)),
            right=Node(40, left=Node(20)),
        ),
    )
)


print(tree.isTreeEmpty())
print("preOrderTraversal: ", BinaryTree.preOrderTraversal(tree.root))
print("postOrderTraversal: ", BinaryTree.postOrderTraversal(tree.root))
print("inOrderTraversal: ", BinaryTree.inOrderTraversal(tree.root))
