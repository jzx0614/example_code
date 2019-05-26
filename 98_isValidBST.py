class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, min_value, max_value):
            if not root: return True
            if not (min_value < root.val < max_value): return False
            
            return dfs(root.left, min_value, root.val) and dfs(root.right, root.val, max_value)

        return dfs(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    # root = TreeNode(5)
    # root.left = TreeNode(1)
    # root.right = TreeNode(4)
    # root.right.left = TreeNode(3)
    # root.right.right = TreeNode(6)

    root = TreeNode(1)
    root.left = TreeNode(1)

    print Solution().isValidBST(root)