# 876. Middle of the Linked List
# Linked list


#  using two pointers
def middleNode(self, head: 'ListNode') -> 'ListNode':
    fast = slow = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow