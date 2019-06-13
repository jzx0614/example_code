# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root, root]
        while queue:
            left, right = queue.pop(0), queue.pop(0)
            if (not left and not right): continue
            if (not left or not right): return False
            if (left.val != right.val): return False

            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)
        return True

if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    print Solution().isSymmetric(root)
