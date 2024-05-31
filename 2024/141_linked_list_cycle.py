from typing import Optional
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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow = head
        fast = head.next
        while fast and slow and slow != fast:
            slow = slow.next
            fast = fast.next.next if fast.next != None else None

        return fast != None
    
if __name__ == "__main__":
    head = gen_list_node([3,2,0,-4])
    print(Solution().hasCycle(head))