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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return {self.v1, self.v2} == {other.v1, other.v2}


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
        if all(map(lambda x: x != link, self._links)):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def find_path(self, start_v, stop_v):
        # формат данных словаря routes - {вершина: [дистанция до нее, маршрут]}
        routes = {v: [inf, []] for v in self._vertex}
        # print(f'Количество вершин: {v_number}')
        # print(routes)

        v0 = start_v
        visited_vertices = set()
        routes.get(v0)[0] = 0

        while v0 != -1:
            v0_dist = routes.get(v0)[0]
            v0_links = routes.get(v0)[1]
            v0_edges = {edge.get_2nd_vertex(v0): [edge.dist, [edge]] for edge in v0.links}
            for v in v0_edges:
                v_dist = v0_dist + v0_edges.get(v)[0]
                if v not in visited_vertices and v_dist < routes.get(v)[0]:
                    routes.get(v)[0] = v_dist
                    routes.get(v)[1] = v0_links + v0_edges.get(v)[1]

            visited_vertices.add(v0)
            m = max(r[0] for r in routes.values())

            print(routes)
            print(f'total vertices: {len(self._vertex)}, visited vertices: {len(visited_vertices)}, max route dist: {m}')

            v0 = -1
            for r in routes:
                if r not in visited_vertices and routes[r][0] < m:
                    m = routes[r][0]
                    v0 = r

        found_links = routes.get(stop_v)[1]
        if len(found_links) < 1:
            raise RuntimeError('Маршрут не найден')
        found_vertices = [start_v]
        found_vertices.extend(lnk.get_2nd_vertex(found_vertices[i]) for i, lnk in enumerate(found_links))

        return found_vertices, found_links


class Station(Vertex):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    pass


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

print(lg.find_path(v_list[0], v_list[5]))


map_graph = LinkedGraph()

v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()
v6 = Vertex()
v7 = Vertex()

map_graph.add_link(Link(v1, v2))
map_graph.add_link(Link(v2, v3))
map_graph.add_link(Link(v1, v3))

map_graph.add_link(Link(v4, v5))
map_graph.add_link(Link(v6, v7))

map_graph.add_link(Link(v2, v7))
map_graph.add_link(Link(v3, v4))
map_graph.add_link(Link(v5, v6))

print(len(map_graph._links))   # 8 связей
print(len(map_graph._vertex))  # 7 вершин
path = map_graph.find_path(v1, v6)
print(path)


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7

