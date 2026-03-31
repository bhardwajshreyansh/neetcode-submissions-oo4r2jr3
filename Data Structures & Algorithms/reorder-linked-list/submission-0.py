# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        #middle element
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverse the 2nd list and reverse links

        second = slow.next 
        prev = slow.next = None
        while second:
            tmp = second.next   #store value of next number into tmp
            second.next = prev   #reverse the link 
            prev = second        #move pre to current node
            second = tmp        #move second to next node

        #Now merge 
        first, second = head, prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2