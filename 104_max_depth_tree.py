class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0
        def recursive(root, depth):
            if not root:
                if depth - 1 > self.max_depth:
                    self.max_depth = depth - 1
                return

            recursive(root.left, depth + 1)
            recursive(root.right, depth + 1)

        recursive(root, 1)
        return self.max_depth