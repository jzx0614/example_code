# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = TreeNode(float("-inf"))
        self.first, self.second = None, None
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            if not self.first and self.prev.val > root.val:
                self.first, self.second = self.prev, root
            if self.first and self.prev.val > root.val:
                self.second = root
            self.prev = root
            traverse(root.right)

        traverse(root)
        self.second.val, self.first.val = self.first.val, self.second.val