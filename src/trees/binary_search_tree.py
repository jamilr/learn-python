from src.trees.binary_tree import Node
import sys

__author__ = "J.R."


class BST(object):

    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root.add(value)

    def search(self, value):
        return self.root.search(value)

    def is_bst(self):
        max_val = sys.maxsize
        min_val = -sys.maxsize - 1
        return self._is_bst(self.root, min_val, max_val)

    def _is_bst(self, root, min_val, max_val):
        if not root:
            return True
        if min_val > root.item or root.item > max_val:
            return False
        return self._is_bst(root.left, min_val, root.item) and self._is_bst(root.right, root.item, max_val)

    def in_order(self):
        r = list()
        if not self.root:
            return r
        else:
            self.root.in_order(self.root, r)
            return r

    @classmethod
    def main(cls):
        bst = BST()
        bst.add(10)
        bst.add(5)
        bst.add(15)
        print('Binary tree is binary search tree - {}'.format(bst.is_bst()))
        print('In-order traversal of tree - {}'.format(bst.in_order()))


if __name__ == '__main__':
    BST().main()