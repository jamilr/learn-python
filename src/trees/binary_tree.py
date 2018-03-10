__author__ = "J.R."


# Node - node in a binary tree
class Node(object):

    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None

    def __repr__(self):
        return '{}'.format(self.item)

    # add a new value to the binary tree
    def add(self, value):
        if not self.item:
            self.item = value
        elif value < self.item:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.add(value)
        elif value > self.item:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.add(value)
        return self

    # search for a node with the specified value
    def search(self, value):
        if not self:
            return self
        if self.left and value < self.item:
            return self.left.search(value)
        elif self.right and value >= self.item:
            return self.right.search(value)
        else:
            return None

    # in-order traversal of binary tree using recursive approach
    @classmethod
    def in_order(cls, root, items):
        if not root:
            return
        if root.left:
            root.in_order(root.left, items)
        items.append(root.item)
        if root.right:
            root.in_order(root.right, items)

    # in-order traversal of binary tree using iterative approach
    @classmethod
    def in_order_iterative(cls, root):
        if not root:
            return None
        s = list()
        result = list()
        cur = root
        while cur or len(s) != 0:
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop()
            result.append(cur.item)
            cur = cur.right
        return result

    # pre-order traversal of binary tree using iterative approach
    @classmethod
    def pre_order_iterative(cls, root):
        if not root:
            return None
        s = list()
        result = list()
        cur = root
        while cur or len(s) != 0:
            while cur:
                result.append(cur.item)
                s.append(cur)
                cur = cur.left
            cur = s.pop().right
        return result

    # post-order traversal of binary tree using iterative approach
    @classmethod
    def post_order_iterative(cls, root):
        if not root:
            return None
        s = list()
        result = list()
        cur = root
        while cur or len(s) != 0:
            while cur:
                result.insert(0, cur.item)
                s.append(cur)
                cur = cur.right
            cur = s.pop().left
        return result

    @classmethod
    def main(cls):
        root = Node(10)
        root.add(4)
        root.add(12)
        items = list()

        root.in_order(root, items)
        print('In-order recursive traversal - {}'.format(items))
        print('In-order iterative traversal - {}'.format(root.in_order_iterative(root)))
        print('Pre-order iterative traversal - {}'.format(root.pre_order_iterative(root)))
        print('Post-order iterative traversal - {}'.format(root.post_order_iterative(root)))


if __name__ == '__main__':
    Node.main()
