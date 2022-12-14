# 4.8 Испытание "Бремя наследия"

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
        self.set_vector_record(v1)
        self.set_vector_record(v2)

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

    def set_vector_record(self, v):
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
        # создать матрицу смежности
        v_number = len(self._vertex)
        adj_matrix = [[None for _ in range(v_number)] for _ in range(v_number)]
        print(adj_matrix)
        for i, v1 in enumerate(self._vertex):
            # adj_matrix[i][i] = 0
            # print(v1.links)
            v1_edges = {edge.get_2nd_vertex(v1): edge.dist for edge in v1.links}
            print(v1_edges)
            # for j, v2 in enumerate(self._vertex[(i+1):]):
            for j, v2 in enumerate(self._vertex):
                adj_matrix[i][j] = v1_edges.get(v2, 0)
        # adj_matrix[v_number-1][v_number-1] = 0
        return adj_matrix

# преобразование треугольной матрицы в симметричную
# for i in range(num_rows):
#     for j in range(i, num_cols):
#         matrix[j][i] = matrix[i][j]


lg = LinkedGraph()
v_list = [Vertex() for _ in range(3)]
link_list = [Link(v_list[0], v_list[1], 1), Link(v_list[1], v_list[2], 2), Link(v_list[0], v_list[2], 5)]
for link in link_list:
    print(f'{link}: {link.v1}, {link.v2}, {link.dist}')
    lg.add_link(link)
# print(lg._links)
# print(lg._vertex)

print(lg.find_path(v_list[0], v_list[2]))

