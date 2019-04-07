# data structure to represent the node in the linked list


__author__ = 'J.R.'


class TreeNode:

    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    @classmethod
    def print(cls, list_head):
        if list_head is None:
            return

        output = '('
        while list_head is not None:
            output += ' ' + str(list_head.val) + ' '
            list_head = list_head.next
        output += ')'
        print(output)
