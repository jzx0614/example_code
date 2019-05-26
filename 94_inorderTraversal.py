# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output, stack = [], []
        current = root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
                continue
            current = stack.pop()
            output.append(current.val)
            current = current.right

        return output

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print Solution().inorderTraversal(root)