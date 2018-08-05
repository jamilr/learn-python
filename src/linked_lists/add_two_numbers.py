# Leetcode Problem #2 - https://leetcode.com/problems/add-two-numbers/description

__author__ = 'J.R.'


from src.linked_lists.data_structure import ListNode


class AddTwoNumbers:

    @classmethod
    def add(cls, l1=None, l2=None):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None
        head_node = ListNode(0)
        cur_node = head_node
        cur_sum = 0
        while l1 is not None or l2 is not None:
            cur_sum = cur_sum + l1.val if l1 is not None else 0
            cur_sum = cur_sum + l2.val if l2 is not None else 0
            cur_node.next = ListNode(cur_sum % 10)
            cur_node = cur_node.next
            cur_sum //= 10
            l1 = l1.next if l1.next is not None else None
            l2 = l2.next if l2.next is not None else None

        if cur_sum > 0:
            cur_node.next = ListNode(cur_sum)

        return head_node.next


if __name__ == '__main__':

    a = ListNode(2)
    a_head = ListNode(0)
    a_head.next = a

    a.next = ListNode(4)
    a = a.next
    a.next = ListNode(3)
    a = a.next

    b = ListNode(5)
    b_head = ListNode(0)
    b_head.next = b

    b.next = ListNode(6)
    b = b.next
    b.next = ListNode(4)
    b = b.next

    ListNode.print(a_head.next)
    ListNode.print(b_head.next)
    sum_head = AddTwoNumbers.add(a_head.next, b_head.next)
    ListNode.print(sum_head)