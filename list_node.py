class ListNode(object):
    def __init__(self, val):
        self.next = None
        self.val = val

    def __repr__(self):
        return str(self.val)

l1, l2, l3 = ListNode(1), ListNode(2), ListNode(3)
l1.next = l2
l2.next = l3

def reverse(head):
    if head is None: return None
    p = head
    cur = None
    pre = None
    while p:
        cur = p.next
        p.next = pre
        pre = p
        p = cur
    return pre

l1 = reverse(l1)
head = l1
while head:
    print(head.val)
    head = head.next
