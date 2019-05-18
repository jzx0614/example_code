# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def getMinNode(lists):
          if len(lists) == 0:
            return None
            
          min_value = lists[0]
          for idx, node in enumerate(lists):
            if node.val == 
        dummy = current = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            current.next = l1
            current = l1
            l1 = l1.next
        current.next = l1 or l2
            
        return dummy.next