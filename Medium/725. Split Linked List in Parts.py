# 725. Split Linked List in Parts
# Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n,cur=0,root
        ans=[]
        while cur:
            n+=1
            cur=cur.next
        parts,remain=divmod(n,k)
        h=root
        for i in range(k):
            head=h
            for i in range(parts-1+(i<remain)):
                h=h.next
            if h:
                h.next,h=None,h.next
            ans.append(head)
        return ans