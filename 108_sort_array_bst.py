# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        idx = (len(nums) -1) // 2

        root = TreeNode(nums[idx])
        root.left = sortedArrayToBST(nums[0:idx])
        root.right = sortedArrayToBST(nums[idx+1:])

        return root