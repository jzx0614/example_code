class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_depth = None
        def dfs(node, depth):
            if not node: return
            if self.min_depth and depth > self.min_depth:
                return

            if not node.left and not node.right:
                if not self.min_depth:
                    self.min_depth = depth
                elif self.min_depth - depth:
                    self.min_depth = depth
                return
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 1)
        return self.min_depth

            