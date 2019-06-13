# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = []
        next_queue = [root]
        while next_queue:
            level_list = [q.val for q in next_queue if q != None]
            if level_list == []: break
            result.append(level_list)
            queue, next_queue = next_queue, queue
            while queue:
                node = queue.pop(0)
                if not node: continue
                next_queue += [node.left, node.right]

        result.reverse()
        return result