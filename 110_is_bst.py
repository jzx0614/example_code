# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = True
        def dfs(node):
            if not node: return 0
            if not self.ans: return None

            left = dfs(node.left)
            right = dfs(node.right)

            if left is None or right is None or abs(left-right) > 1:
                self.ans = False
            
            return max(left,right) + 1
        dfs(root)
        return self.ans
