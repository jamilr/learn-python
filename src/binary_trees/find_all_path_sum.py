# LeetCode 113 - https://leetcode.com/problems/path-sum-ii/


__author__ = 'J.R.'

from src.binary_trees.data_structure import TreeNode
import unittest


class AllPathSum:

	def __init__(self):
		pass

	def find_all_path_sum(self, root: TreeNode, a: int):
		if not root:
			return []
		return self.path_sum(root, a)

	def path_sum(self, root: TreeNode, a: int):
		if not root:
			return []
		if not root.left and not root.right:
			if a - root.val == 0:
				return [[root.val]]

		a = a - root.val
		left = self.path_sum(root.left, a)
		right = self.path_sum(root.right, a)

		if len(left) > 0:
			for i in range(len(left)):
				left[i].insert(0, root.val)

		if len(right) > 0:
			for i in range(len(right)):
				right[i].insert(0, root.val)

		return left + right


class PathSumTest(unittest.TestCase):

	def test_path_sum(self):

		root = TreeNode(5)

		left = TreeNode(6)
		right = TreeNode(7)

		left.left = TreeNode(9)
		left.right = TreeNode(9)

		right.left = TreeNode(8)
		right.right = TreeNode(8)

		root.left = left
		root.right = right

		all_path_sum = AllPathSum()
		result = all_path_sum.find_all_path_sum(root, 20)

		[print(result[i]) for i in range(len(result))]


if __name__ == '__main__':
	unittest.main()