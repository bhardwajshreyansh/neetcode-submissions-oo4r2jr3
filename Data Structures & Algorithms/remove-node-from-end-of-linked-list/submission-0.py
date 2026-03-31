class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre = ListNode(0)
        pre.next = head
        slow = pre
        fast = pre
        for _ in range (n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return pre.next
    
#Start slow and fast pointer at the dummy node
#Move fast pointer n steps ahead
#Move slow and fast pointer one step at a time until fast reaches the end
#Remove the nth node from the end by updating the slow.next pointer
#Return the head node as pre.next not head

#     # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         slow, fast = head, head 
#         pre = ListNode(0)
#         pre.next = head
#         post = head.next
#         for _ in range (n):
#             fast = fast.next
#         while fast and fast.next:
#             self.pre = pre.next
#             post = post.next
#             slow = slow.next
#             fast = fast.next.next
#         pre.next = post
#         slow.next = None
#         return head