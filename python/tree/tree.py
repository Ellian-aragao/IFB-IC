import asyncio
from queue import Queue
ROOT = "root"


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def breadth_first_search(self, node=None, function=print):
        if node is None:
            node = self.root
        asyncio.run(self._breadth_first_search(node, function))

    async def _breadth_first_search(self, node=None, function=print):
        if node is None:
            return

        self._executor_node(node.data, function)
        await asyncio.gather(
            self._breadth_first_search(node.left, function),
            self._breadth_first_search(node.right, function)
        )

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
            print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    def preorder_traversal(self, node=None, function=print):
        if node is None:
            node = self.root
        self._executor_node(node.data, function)
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node=None, function=print):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        self._executor_node(node.data, function)
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None, function=print):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        self._executor_node(node.data, function)

    def _executor_node(self, node=None, function=print):
        if node == None:
            return

        if function == print:
            function(node, end=' ')
        else:
            function(node)

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

    def levelorder_traversal(self, node=ROOT, function=print):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.put(node)
        while queue.qsize():
            node = queue.get()
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
            self._executor_node(node.data, function)


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

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node=ROOT):
        if node == ROOT:
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


array = []


def salve_value(node=None):
    if node is None:
        return
    array.append(node)


if __name__ == "__main__":
    tree = BinaryTree(
        node=Node(
            'Brasil',
            Node(
                'Norte',
                Node(
                    'Noroeste'
                ),
                Node(
                    'Nordeste'
                )
            ),
            Node(
                'Sul',
                Node(
                    'Sudoeste'
                ),
                Node(
                    'Sudeste'
                )
            )
        )
    )
