from .BinaryTree import BinaryTree

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def min(self, node=self.ROOT):
        if node == self.ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=self.ROOT):
        if node == self.ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node=self.ROOT):
        if node == self.ROOT:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            self._remove(value, node)

        return node

    def _remove(self, value, node=None):
        if node is None:
            return

        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            self._remove_swap(node.data, node.right)

    def _remove_swap(self, data, node_right):
        substitute = self.min(node_right)
        data = substitute
        node_right = self.remove(substitute, node_right)
