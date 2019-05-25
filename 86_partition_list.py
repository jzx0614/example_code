class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def generate_list(num_list):
    previous = head = ListNode(num_list[0])
    for idx, v in enumerate(num_list):
        if idx == 0: continue
        node = ListNode(v)
        previous.next = node
        previous = node

    return head

def print_list(head):
    output_list = []
    while head:
        output_list.append(head.val)
        head = head.next
    print output_list

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head = less = ListNode(0)
        orig_head = prev = ListNode(0)
        prev.next = head
        while prev.next:
            if prev.next.val < x:
                less.next = prev.next
                less = less.next
                prev.next = prev.next.next
            else:
                prev = prev.next

        less.next = orig_head.next
        # print_list(less_head.next)
        return less_head.next
        
if __name__ == "__main__":
    head = generate_list([1,4,3,2,5,2])
    Solution().partition(head, 3)