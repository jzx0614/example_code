# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_value = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.get_diameter_depth(root)[0]


    def get_diameter_depth(self, root):
        if not root:
            return [0, 0]
        left_d = self.get_diameter_depth(root.left)
        right_d = self.get_diameter_depth(root.right)
        return [max(left_d[0], right_d[0], left_d[1]+right_d[1]), max(left_d[1], right_d[1])+1]