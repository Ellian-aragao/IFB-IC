from __future__ import annotations
from typing import List


class Node:
    def __init__(self, data: str, distance: float, children: List[A2B] = []):
        self.data = data
        self.distance = distance
        self.children = children

    def busca_a_estrela(self, array: List[A2B] = []) -> List[A2B]:
        var: A2B = sorted(self.children, reverse=True, key=(
            lambda x: x.get_a_distance_b_plus_b_final()
        )).pop()
        array.append(var)
        if var.get_a_distance_b_plus_b_final() != 0:
            var.b.busca_a_estrela(array)
        return array

    def __str__(self):
        return str(self.data)


class A2B:
    def __init__(self, a: Node, b: Node, distance=0):
        self.a = a
        self.b = b
        self.distance = distance

    def get_a_distance_b_plus_b_final(self) -> float:
        return self.distance + self.b.distance

    def __str__(self):
        return '{} -> {}'.format(self.a, self.b)


if __name__ == '__main__':
    arad = Node('arad', 366)
    zerind = Node('zerind', 374)
    timisoara = Node('timisoara', 329)
    oradea = Node('oradea', 380)
    sibiu = Node('sibiu', 253)
    fagaras = Node('fagaras', 178)
    rimnicu = Node('rimnicu', 193)
    pitesti = Node('pitesti', 98)
    bucacharest = Node('bucacharest', 0)
    cralova = Node('cralova', 160)

    arad.children = {
        A2B(arad, zerind, 75),
        A2B(arad, sibiu, 140),
        A2B(arad, timisoara, 118)
    }

    zerind.children = {
        A2B(zerind, oradea, 71),
        A2B(zerind, arad, 75)
    }

    oradea.children = {
        A2B(oradea, zerind, 71),
        A2B(oradea, sibiu, 151)
    }

    timisoara.children = {
        A2B(timisoara, arad, 118)
    }

    sibiu.children = {
        A2B(sibiu, arad, 140),
        A2B(sibiu, rimnicu, 80),
        A2B(sibiu, fagaras, 99),
        A2B(sibiu, oradea, 151)
    }

    fagaras.children = {
        A2B(fagaras, sibiu, 99),
        A2B(fagaras, bucacharest, 221)
    }

    rimnicu.children = {
        A2B(rimnicu, sibiu, 80),
        A2B(rimnicu, cralova, 146),
        A2B(rimnicu, pitesti, 97)
    }

    pitesti.children = {
        A2B(pitesti, rimnicu, 97),
        A2B(pitesti, cralova, 138),
        A2B(pitesti, bucacharest, 101)
    }

    bucacharest.children = {
        A2B(bucacharest, pitesti, 101),
        A2B(bucacharest, bucacharest, 0)
    }

    for ab in arad.busca_a_estrela():
        print('{:0>3} | {}'.format(ab.get_a_distance_b_plus_b_final(), ab))
