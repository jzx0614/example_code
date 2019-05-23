# Definition for singly-linked list.
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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0: return head
        
        previous = ListNode(0)
        previous.next = head
        
        ans_head = current = head
        total_len = 0
        while total_len < k:
            if not current: break
            total_len += 1
            current = current.next
            

        if not current:
            if total_len == k or total_len == 0:
                return head
            k = k % total_len
            return self.rotateRight(head, k)

        while current:
            previous = previous.next
            ans_head = ans_head.next
            
            if current.next == None:
                previous.next = None
                current.next = head
                break
            current = current.next

        return ans_head
if __name__ == "__main__":
    # print_list(generate_list(range(1, 2)))
    print_list(Solution().rotateRight(generate_list(range(1, 2)), 0))
    # print_list(Solution().rotateRight(generate_list(range(1, 5+1)), 2))
    # print_list(Solution().rotateRight(generate_list(range(3)), 4))
