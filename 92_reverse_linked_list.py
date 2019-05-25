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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        def reverse(prev, count):
            if count <= 1: return 0

            current = prev.next
            reverse = None
            while count > 0:
                next_node = current.next
                current.next = reverse
                reverse = current
                current = next_node
                count -= 1

            prev.next.next = current
            prev.next = reverse

        prev = dummy = ListNode(0)
        dummy.next = head

        for i in range(m - 1):
            prev = prev.next

        reverse(prev, n-m+1)

        return dummy.next

if __name__ == "__main__":
    head = generate_list([1,2,3,4,5])
    print_list(Solution().reverseBetween(head, 1, 5))