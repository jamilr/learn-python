# LeetCode 112 - https://leetcode.com/problems/path-sum/


__author__ = 'J.R.'

from src.binary_trees.data_structure import TreeNode
import unittest


class PathSum:

	def __init__(self):
		pass

	def find_path_sum(self, head: TreeNode, a: int):
		if  not head:
			return False
		self.path_sum(head, a)

	def path_sum(self, head: TreeNode, a: int):
		if not head:
			return False
		if not head.left and not head.right:
			if a - head.val == 0:
				return True
		a = a - head.val
		return self.path_sum(head.left, a) or self.path_sum(head.right, a)


class PathSumTest(unittest.TestCase):

	def test_path_sum(self):
		x1 = TreeNode(10)
		x1.left = TreeNode(5)
		x1.right = TreeNode(6)
		path_sum = PathSum()
		result = path_sum.path_sum(x1, 16)
		expected = True
		self.assertEqual(expected, result)


if __name__ == '__main__':
	unittest.main()

