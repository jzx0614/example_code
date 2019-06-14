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
        self.max_depth = 0
        def update_depth(depth):
            print depth, self.max_depth
            if self.max_depth == 0:
                self.max_depth = depth
                return True

            if abs(depth - self.max_depth) > 1:  
                return False
            return True

        def dfs(node, depth):
            if not node: 
                return update_depth(depth)

            return dfs(node.left, depth+1) and dfs(node.right, depth+1))
        return dfs(root, 1)
