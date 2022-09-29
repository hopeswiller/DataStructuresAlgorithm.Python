# https://leetcode.com/problems/binary-tree-maximum-path-sum/


class BTNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    """
    Question
    1: Given a binary tree, find the maximum path sum.
    - Path is defined as any sequence of nodes from some starting node to any node in the
    tree along the parent - child connections.
    - The path must contain at least one node
    example:
        1
       / \
      4   2
     / \
    6   3
    ans: 13(2 + 1 + 4 + 6)
        1
       / \
      2  -40
     / \
    60  30
    ans: 92(60 + 2 + 30)
    """

    sum = 0

    def find_max_sum(self, root):
        # traverse from the root
        currentNode = root
        if currentNode is not None:
            self.sum += currentNode.val
            self.find_max_sum(currentNode.left)
            self.sum += currentNode.right.val if currentNode.right is not None else 0

        # print(self.sum)
        return self.sum


# Expected: 13
tree_1_root = BTNode(
    x=1, left=BTNode(x=4, left=BTNode(x=6), right=BTNode(x=3)), right=BTNode(x=2)
)

# Expected: 92
tree_2_root = BTNode(
    x=1, left=BTNode(x=2, left=BTNode(x=60), right=BTNode(x=30)), right=BTNode(x=-40)
)

# assert Solution().find_max_sum(tree_1_root) == 13
# assert Solution().find_max_sum(tree_2_root) == 92

assert Solution().find_max_sum(tree_1_root) == 14
