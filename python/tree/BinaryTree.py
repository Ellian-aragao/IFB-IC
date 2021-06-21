import asyncio
from queue import Queue

class BinaryTree:
    ROOT = "root"

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

    def levelorder_traversal(self, node=self.ROOT, function=print):
        if node == self.ROOT:
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
