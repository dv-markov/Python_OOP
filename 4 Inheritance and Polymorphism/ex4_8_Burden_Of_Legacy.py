# 4.8 Испытание "Бремя наследия"
from math import inf

class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1: Vertex, v2: Vertex, dist: int = 1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist
        self.set_vertex_record(v1)
        self.set_vertex_record(v2)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    def set_vertex_record(self, v):
        if self not in v.links:
            v.links.append(self)

    def get_2nd_vertex(self, v):
        return self.v2 if v is self.v1 else self.v1


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v: Vertex):
        if v not in self._vertex:
            self._vertex.append(v)
            # for l in v.links:
            #     self.add_link(l)

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def find_path(self, start_v, stop_v):
        def get_adjacency_matrix():
            # создание матрицы смежности
            v_number = len(self._vertex)
            adj_matrix = [[None for _ in range(v_number)] for _ in range(v_number)]
            print(*adj_matrix, sep='\n')
            for i, v1 in enumerate(self._vertex):
                v1_edges = {edge.get_2nd_vertex(v1): edge.dist for edge in v1.links}
                print(v1_edges)
                for j, v2 in enumerate(self._vertex):
                    adj_matrix[i][j] = v1_edges.get(v2, 0)
            return adj_matrix

        def get_link_v(v, D):
            for i, weight in enumerate(D[v]):
                if weight > 0:
                    yield i

        def arg_min(T, S):
            amin = -1
            m = max(T)
            for i, t in enumerate(T):
                if t < m and i not in S:
                    m = t
                    amin = i

            return amin

        D = get_adjacency_matrix()

        N = len(D)  # число вершин в графе
        T = [inf] * N  # последняя строка в таблице
        print(T)

        v0 = 1
        v = v0  # стартовая вершина (нумерация с нуля)
        S = {v}  # множество просмотренных вершин
        T[v] = 0  # нулевой вес для стартовой вершины
        print(T)

        while v != -1:  # цикл пока не просмотрим все вершины
            for j in get_link_v(v, D):  # перебираем все связанные вершины
                if j not in S:  # если вершина еще не просмотрена
                    w = T[v] + D[v][j]
                    if w < T[j]:
                        T[j] = w

            v = arg_min(T, S)  # выбираем следующий узел с минимальным весом
            if v != v0:  # выбрана новая вершина, в оригинале было v > 0
                S.add(v)  # добавляем вершину в множество просмотренных

        print(f'Вектор весов для вершины {v0}: {T}')
        return D


# # test_my_example
# lg = LinkedGraph()
# v_list = [Vertex() for _ in range(3)]
# link_list = [Link(v_list[0], v_list[1], 1), Link(v_list[1], v_list[2], 2), Link(v_list[0], v_list[2], 5)]
# for lnk in link_list:
#     print(f'{lnk}: {lnk.v1}, {lnk.v2}, {lnk.dist}')
#     lg.add_link(lnk)
# # print(lg._links)
# # print(lg._vertex)
#
# print(*lg.find_path(v_list[0], v_list[2]), sep='\n')


# Balakirev https://www.youtube.com/watch?v=MCfjc_UIP1M&t=708s
lg = LinkedGraph()
v_list = [Vertex() for _ in range(6)]
link_list = [Link(v_list[0], v_list[1], 3),
             Link(v_list[0], v_list[2], 1),
             Link(v_list[0], v_list[3], 3),
             Link(v_list[1], v_list[2], 4),
             Link(v_list[2], v_list[4], 7),
             Link(v_list[2], v_list[5], 5),
             Link(v_list[3], v_list[5], 2),
             Link(v_list[5], v_list[4], 4)]
for lnk in link_list:
    print(f'{lnk}: {lnk.v1}, {lnk.v2}, {lnk.dist}')
    lg.add_link(lnk)

print(*lg.find_path(v_list[0], v_list[2]), sep='\n')




