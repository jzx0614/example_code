def printListNode(node):
    if node == None:
        print
        return
    print str(node.val) + " -> ", 
    printListNode(node.next)

def nodeToNum(node):
    num = 0
    pow_index = 0
    while node != None:
        num += node.val * pow(10, pow_index)
        pow_index += 1
        node = node.next
    return num
        
def numToNode(num):
    if num == 0:
        return ListNode(0)
    result = result_iter = None
    while num != 0:
        val = num % 10
        num /= 10
        if result == None:
            result = result_iter = ListNode(val)
        else:
            result_iter.next = ListNode(val)
            result_iter = result_iter.next
    return result
    

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoDigits(self, l1, l2, other_value):
        if l1 == None:
            if l2 == None:
                return None
            l1 , l2 = l2, l1
        
        if l2 == None:
            sum = l1.val + other_value
        else:
            sum = l1.val + l2.val + other_value
        return ListNode(sum%10), sum/10
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        print nodeToNum(l1)
        return numToNode(nodeToNum(l1) + nodeToNum(l2))
        # carry = 0
        # result = None
        # result_iter = None
        # while l1 or l2:
            # node, carry = self.addTwoDigits(l1, l2, carry)

            # if node == None:
                # break
        
            # if result == None:
                # result = result_iter = node
            
            # else:
                # result_iter.next = node
                # result_iter = result_iter.next

            # if l1 != None:
                # l1 = l1.next
            # if l2 != None:
                # l2 = l2.next
            
        # if value != 0:
            # result_iter.next = ListNode(value)
            
        return result
        
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8        
if __name__ == "__main__":
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    l1 = ListNode(0)
    l2 = ListNode(0)
    result = Solution().addTwoNumbers(l1, l2)
    printListNode(result)