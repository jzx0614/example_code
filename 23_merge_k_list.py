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

            min_data = (lists[0].val, 0)
            for idx, node in enumerate(lists):
                if node.val < min_data[0]:
                    min_data = (node, node.val, idx)

            node, val, idx = min_data
            
            if (node.next == None):
                del lists[idx]
            else:
                lists[idx] = node.next

            node.next = self.getMinNode(lists)
            return node

        lists = [node for node in lists if node]
        head = getMinNode(lists)

        return head
