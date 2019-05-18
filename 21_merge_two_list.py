# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def getMin(node1, node2):
            if not node1 and not node2: return None
            if not node2: return node1
            if not node1: return node2
            if node1.val < node2.val:
                r = node1
                node1 = node1.next
                return r
            else:
                r = node2
                node2 = node2.next
                return r

        head = node = getMin(l1, l2)
        while True:
            r = getMin(l1, l2)
            if r == None: break
                
            node.next = r
            r.next = None            

