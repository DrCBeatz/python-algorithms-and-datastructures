# reverse_liked_list_recursive.py

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
        
    reversed_list = reverse_list(head.next)

    head.next.next = head
    head.next = None

    return reversed_list
