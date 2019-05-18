# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre_node = node = head
        count = 0 
        while node and count <= n:
            node = node.next
            count += 1

        if not node:
            if count == n:
                return head.next
            return head

        while node:
            node = node.next
            pre_node = pre_node.next

        pre_node.next = pre_node.next.next
        
        return head
        
    