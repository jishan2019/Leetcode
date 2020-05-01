# 817. Linked List Components
# Linked List
# We are given head, the head node of a linked list containing unique integer values.
#
# We are also given the list G, a subset of the values in the linked list.
#
# Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        #using set to solve
        set_G=set(G)
        count=0
        while head:
            if head.val in set_G:
                if (head.next and head.next.val not in set_G or not head.next):
                    count+=1
            head=head.next
        return count

