# 24. Swap Nodes in Pairs
#  linked list



def swapPairs(self, head: ListNode) -> ListNode:
    prev, prev.next = self, head
    while prev.next and prev.next.next:
        a = prev.next    # current
        b = a.next
        prev.next, b.next, a.next = b, a, b.next
        prev = a
    return self.next