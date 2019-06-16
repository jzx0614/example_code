class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        def dfs(node, value):
            if not node: 
                return False
            value = value - node.val
            
            if not node.left and not node.right and value == 0:
                return True

            return dfs(node.left, value) or dfs(node.right, value)
        return dfs(root, sum)