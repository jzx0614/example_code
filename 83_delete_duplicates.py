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
        current = no_duplicate = head
        while current:
            no_duplicate = current.next
            while no_duplicate and current.val == no_duplicate.val:
                no_duplicate = no_duplicate.next

            current.next = no_duplicate
            current = no_duplicate

        return head
        
if __name__ == "__main__":
    head = generate_list([1,1,2,3,3])
    print_list(Solution().deleteDuplicates(head))