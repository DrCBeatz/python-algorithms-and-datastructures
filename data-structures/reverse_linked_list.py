# reverse_linked_list.py

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head: ListNode) -> ListNode:
    prev = next = None
    cur = head

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev