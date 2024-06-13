# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance_depth(root):
            if not root: 
                return [True, 0]
            left_dep = balance_depth(root.left)
            right_dep = balance_depth(root.right)
            if not (left_dep[0] and right_dep[0]) or abs(left_dep[1] - right_dep[1]) > 1:
                return [False, 0]

            return [True, max(left_dep[1], right_dep[1]) + 1]

        return balance_depth(root)[0]