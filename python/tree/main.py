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
