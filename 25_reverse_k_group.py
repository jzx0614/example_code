# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        node_list = []
        for i in xrange(k):
            if not node: break
            node_list.append(node)
            node = node.next
        
        if not node:
            return head
        next_node = node.next

        node_list.reverse()
        for idx, n in enumerate(node_list):
            n.next = self.reverseKGroup(next_node, k) if idx == (k-1) else node_list[idx+1]

        return node_list[0]
        