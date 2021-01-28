# 19. Remove Nth Node From End of List
# Medium

# 4605

# 281

# Add to List

# Share
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        
        while n > 0:
            fast = fast.next
            n -= 1
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head