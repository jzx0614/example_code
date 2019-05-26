# Definition for a binary tree node.
def printTreeNode(root):
    print_stack = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if not node:
            print_stack.append(None)
        else:
            print_stack.append(node.val)
            if node.left or node.right:
                queue.append(node.left)
                queue.append(node.right)
    # print print_stack
    return print_stack

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def dfs(start, end):
            if start == end:
                return None
            node_list = []
            for idx in range(start, end):
                for left in dfs(start, idx) or [None]:
                    for right in dfs(idx+1, end) or [None]:
                        node = TreeNode(idx)
                        node.left, node.right = left, right
                        node_list.append(node)
                        # print printTreeNode(node)
            return node_list

        return dfs(1, n+1)

if __name__ == "__main__":
    result = Solution().generateTrees(2)
    for t in result:
        print printTreeNode(t) 
