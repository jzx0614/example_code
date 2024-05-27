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

def create_head(list_node, head: ListNode):
    node = root = gen_list_node(list_node)
    while node.next:
        node = node.next
    node.next = head
    return root
    
class Solution:
    def len_list_node(self, head: ListNode):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        '''
            count listNode A, B, then let two list equal
            sequence compare two list 
        '''
        count1 = self.len_list_node(head1)
        count2 = self.len_list_node(head2)
        
        if count1 == 0 or count2 == 0:
            return None
        
        if count1 < count2:
            head1, head2 = head2, head1
            count1, count2 = count2, count1

        while count1 != count2:
            head1 = head1.next
            count1 -= 1

        while head1 != head2:
            head1 = head1.next
            head2 = head2.next

        return head1


if __name__ == "__main__":
    node = gen_list_node([8,4,5])
    head1 = create_head([4, 1], node)
    head2 = create_head([5, 6, 1], node)
    print(Solution().getIntersectionNode(head1, head2))

    