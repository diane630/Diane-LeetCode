# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if k == 1:
            return head
        
        dummyHead = ListNode(0)
        prevEnd = dummyHead
            
        def reverseK_onetime(head: ListNode, k: int) -> ListNode:
            """
            eg.
            k = 3
            whatever->1->2->3->whatever head 1
            None<-1<-2<-3 return 3
            """
            prev, cur = None, head
            for i in range(k):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev
        
        def has_at_least_k(head: ListNode, k:int):
            """
            return node after preoceeding k steps (can be none if is the last round)
            return False if not enough
            """
            i = 0
            q = head
            while i < k and q:
                q = q.next
                i += 1
            return q if i >= k else False
                
        
        while has_at_least_k(head, k) is not False:
            next_round_start = has_at_least_k(head, k)
            node_k_multiples = reverseK_onetime(head, k)
            prevEnd.next = node_k_multiples
            cur_round_end = node_k_multiples
            for step in range(k-1):
                cur_round_end = cur_round_end.next
            prevEnd = cur_round_end
            head = next_round_start
        
        prevEnd.next = head
        
        return dummyHead.next
            
        