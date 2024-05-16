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


def genListNode(list_node):
    head_node = current_node = ListNode(list_node.pop(0))
    for node_value in list_node:
        node = ListNode(node_value)
        current_node.next = node
        current_node = node
    return head_node

def createHead(list_node, head: ListNode):
    node = root = genListNode(list_node)
    while node.next:
        node = node.next
    node.next = head
    return root
    
class Solution:
    def countListNode(self, head: ListNode):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
            count listNode A, B, then let two list equal
            sequence compare two list 
        '''
        countA = self.countListNode(headA)
        countB = self.countListNode(headB)
        
        if countA == 0 or countB == 0:
            return None
        
        if countA < countB:
            headA, headB = headB, headA
            countA, countB = countB, countA

        while countA != countB:
            headA = headA.next
            countA -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


if __name__ == "__main__":
    node = genListNode([8,4,5])
    headA = createHead([4, 1], node)
    headB = createHead([5, 6, 1], node)
    print(Solution().getIntersectionNode(headA, headB))

    