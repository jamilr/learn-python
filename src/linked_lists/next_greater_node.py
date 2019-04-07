# Leetcode Problem #1019 - https://leetcode.com/problems/next-greater-node-in-linked-list

__author__ = 'J.R.'

from src.linked_lists.data_structure import ListNode
import unittest


class NextGreaterNode:

	@classmethod
	def find_next_greater_node(cls, head:ListNode):
		arr = cls.to_array(head)
		deq = []
		size = len(arr)
		res = [0]*size
		for i in range(size):
			while len(deq) > 0 and arr[i] > arr[deq[-1]]:
				res[deq.pop()] = arr[i]
			deq.append(i)
		return res

	@classmethod
	def to_array(cls, head: ListNode):
		arr = []
		cur = head
		while cur:
			arr.append(cur.val)
			cur = cur.next
		return arr


class NextGreaterNodeTest(unittest.TestCase):

	def test_algorithm(self):
		x1 = ListNode(2)
		x1.next = ListNode(1)
		x1.next.next = ListNode(5)
		exp = [5, 5, 0]
		res = NextGreaterNode.find_next_greater_node(x1)
		self.assertEqual(exp, res)


if __name__ == '__main__':
	unittest.main()

