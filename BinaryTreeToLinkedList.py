# Convert a given Binary Tree to Doubly Linked List

# Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
# The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL.
# The order of nodes in DLL must be the same as in Inorder for the given Binary Tree.
# The first node of Inorder traversal (leftmost node in BT)

# [10,12,15,25,30,36]

#           10
#         /    \
#       12      15
#     /   \     /
#    25   30   36

from BinaryTree import Node


class BinaryTreeToDLL:
    def __init__(self):
        self.root = None
        self.head = None  # head for DLL

    def inOrderTraversal(self, root):
        if root is not None:
            # traverse left side, root  then right side
            self.inOrderTraversal(root.left)
            self.addtoLinkedList(root.key)
            self.inOrderTraversal(root.right)

    def addtoLinkedList(self, key):
        newNode = Node(key)
        current = self.head
        if self.head is None:
            self.head = newNode
        else:
            while current.right is not None:
                current = current.right
            current.right = newNode
            newNode.left = current

    def showLinkedList(self):
        current = self.head
        print(f"Coverted Double Linked List: ", end="")
        while current is not None:
            print(current.key, end=", ")
            current = current.right
        print()


tree = BinaryTreeToDLL()
tree.root = Node(
    key=10,
    left=Node(key=12, left=Node(25), right=Node(30)),
    right=Node(key=15, left=Node(36)),
)


tree.inOrderTraversal(tree.root)
tree.showLinkedList()
