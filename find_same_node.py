#交叉链表求交点
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __repr__(self):
        return str(self.val)

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

l2 = ListNode(5, ListNode(3, ListNode(6, ListNode(8))))

def find_same_node(l1, l2):
    head1 = l1
    while head1:
        v1 = head1.val
        print("v1=%s"%v1)
        head2 = l2
        while head2:
            v2 = head2.val
            print("v2=%s"%v2)
            if v1 == v2:
                return v1
            else:
                head2 = head2.next
        head1 = head1.next
    return None

result = find_same_node(l1, l2)
print(result)
