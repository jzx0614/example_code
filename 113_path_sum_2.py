class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        stack = []
        def dfs(node, value):
            if not node: return
            value -= node.val
            stack.append(node.val)
            if not node.left and not node.right:
                if not value:
                    result.append(stack[:])
                stack.pop()
                return

            dfs(node.left, value)
            dfs(node.right, value)
            stack.pop()
            
        dfs(root, sum)
        return result