class AB:
    def __init__(self, a, b, distance=0):
        self.a = a
        self.b = b
        self.distance = distance


class Node:
    def __init__(self, data, distance, children=None):
        self.data = data
        self.distance = distance
        self.children = children

    def __str__(self):
        return str(self.data)


def busca_a_estrela(raiz):
    if raiz is None:
        raise ValueError('Can not send something is not a Node')

    ordered_list = [{'ab': child, 'delta': child.b.distance + child.distance}
                    for child in raiz.children]
    ordered_list.sort(key=(lambda x: x.get('delta')))

    array.append(ordered_list[0].get('ab'))

    if ordered_list[0].get('delta') != 0:
        busca_a_estrela(ordered_list[0].get('ab').b)


array = []

if __name__ == "__main__":
    arad = Node("arad", 366)
    zerind = Node("zerind", 374)
    timisoara = Node("timisoara", 329)
    oradea = Node("oradea", 380)
    sibiu = Node("sibiu", 253)
    fagaras = Node("fagaras", 178)
    rimnicu = Node("rimnicu", 193)
    pitesti = Node("pitesti", 98)
    bucacharest = Node("bucacharest", 0)
    cralova = Node("cralova", 160)

    arad.children = {
        AB(arad, zerind, 75),
        AB(arad, sibiu, 140),
        AB(arad, timisoara, 118)
    }

    zerind.children = {
        AB(zerind, oradea, 71),
        AB(zerind, arad, 75)
    }

    oradea.children = {
        AB(oradea, zerind, 71),
        AB(oradea, sibiu, 151)
    }

    timisoara.children = {
        AB(timisoara, arad, 118)
    }

    sibiu.children = {
        AB(sibiu, arad, 140),
        AB(sibiu, rimnicu, 80),
        AB(sibiu, fagaras, 99),
        AB(sibiu, oradea, 151)
    }

    fagaras.children = {
        AB(fagaras, sibiu, 99),
        AB(fagaras, bucacharest, 221)
    }

    rimnicu.children = {
        AB(rimnicu, sibiu, 80),
        AB(rimnicu, cralova, 146),
        AB(rimnicu, pitesti, 97)
    }

    pitesti.children = {
        AB(pitesti, rimnicu, 97),
        AB(pitesti, cralova, 138),
        AB(pitesti, bucacharest, 101)
    }

    bucacharest.children = {
        AB(bucacharest, pitesti, 101),
        AB(bucacharest, bucacharest, 0)
    }

    busca_a_estrela(arad)
    for ab in array:
        print(ab.a, end=' -> ')
