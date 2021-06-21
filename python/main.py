from tree.node import Node
from tree.binaryTrees.binaryTree import BinaryTree

array = []


def salve_value(node=None):
    if node is None:
        return
    array.append(node)


if __name__ == "__main__":
    BinaryTree(
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
    ).breadth_first_search()
