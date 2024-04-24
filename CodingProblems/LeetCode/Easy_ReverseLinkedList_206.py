from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionRecursive:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _, toRet = self.helper(head)
        return toRet
        
    def helper(self, head: Optional[ListNode]):
        if head == None:
            return None, None
        if head.next == None:
            l = ListNode(head.val, None)
            return l, l
        l, toRet = self.helper(head.next)
        l.next = ListNode(head.val, None)
        return l.next, toRet
    
class SolutionIterative:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        cur = ListNode(head.val, None)
        while head.next is not None:
            head = head.next
            cur = ListNode(head.val, cur)
        return cur
            