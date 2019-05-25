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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        current = prev.next = head
        while current:
            next_node = current.next
            if next_node and next_node.val == current.val:
                while next_node and current.val == next_node.val:
                    next_node = next_node.next
                prev.next = next_node
                current = next_node
            else:
                prev = current
                current = next_node
        return dummy.next
        
if __name__ == "__main__":
    head = generate_list([1,1,2,2,3,3,4,4,5,5])
    print_list(Solution().deleteDuplicates(head))