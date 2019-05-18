class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        current = head
        head = head.next
        previous = None
        while current and current.next:
            one = current
            two = current.next
            three = current.next.next

            if previous:
                previous.next = two
            two.next = previous = one
            one.next = current = three
            
        return head
            
