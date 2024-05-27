from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next is None:
            return str(self.val)
        
        outstr = ""
        head_node = self
        while True:
            outstr += str(head_node.val)
            head_node = head_node.next
            if head_node is None: break
            outstr += '->'
        
        return outstr


def gen_list_node(list_node):
    head_node = current_node = ListNode(list_node.pop(0))
    for node_value in list_node:
        node = ListNode(node_value)
        current_node.next = node
        current_node = node
    return head_node

    
class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        
        rervers_p = reverse_head = node_list.pop()
        reverse_head.next = None

        while len(node_list) > 0:
            node = node_list.pop()
            rervers_p.next = node
            node.next = None
            rervers_p = node

        return reverse_head
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev = None
        next = curr = head

        while curr.next:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        next.next = prev
        return next

            


if __name__ == "__main__":
    node = gen_list_node([8,4,5,7,8,9])
    print(Solution().reverseList(node))

    