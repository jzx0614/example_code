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
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = newlist = ListNode(0)
        while list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            current.next = list1
            current = current.next
            list1 = list1.next

        current.next = list1 or list2

        return newlist.next
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2: return list1
        if not list1: return list2

        if list1.val > list2.val:
            list1, list2 = list2, list1

        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

    
if __name__ == "__main__":
    node = gen_list_node([1,2,4])
    node2 = gen_list_node([1,3,4])

    print(Solution().mergeTwoLists(node,node2))