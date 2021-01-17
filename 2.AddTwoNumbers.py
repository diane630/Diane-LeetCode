# 2. Add Two Numbers
# Medium

# 10489

# 2568

# Add to List

# Share
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if l1 else l2
        
        dummy_head = ListNode(0)
        res = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            if l1 and l2:
                res_val = (l1.val + l2.val + carry) #if carry else (l1.val + l2.val)
                
            elif l1 or l2:
                res_val = (l1.val + carry) if l1 else (l2.val + carry)
                    
            elif carry: # only has carry
                res.next = ListNode(carry)
                break
                            
            carry = 0
            if res_val >= 10:
                carry = res_val // 10
                res_val = res_val % 10
                
            res.next = ListNode(res_val)
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            if res: res = res.next
        
        return dummy_head.next