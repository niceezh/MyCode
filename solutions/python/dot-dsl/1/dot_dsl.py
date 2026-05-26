NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if not data:
            return
        if not isinstance(data, list):
            raise TypeError('Graph data malformed')
        for item in data:
            if not isinstance(item, tuple):
                raise TypeError('Graph item malformed')
            if not item:
                raise TypeError('Graph item incomplete')
            if item[0] == NODE:
                if len(item) < 2:
                    raise TypeError('Graph item incomplete')
                name, attrs = item[1], item[2] if len(item) > 2 else {}
                if not isinstance(name, str) or not isinstance(attrs, dict):
                    raise ValueError('Node is malformed')
                self.nodes.append(Node(name, attrs))
                continue
            if item[0] == EDGE:
                if len(item) < 3:
                    raise TypeError('Graph item incomplete')
                src, dst, attrs = item[1], item[2], item[3] if len(item) > 3 else {}
                if not isinstance(src, str) or not isinstance(dst, str) or not isinstance(attrs, dict):
                    raise ValueError('Edge is malformed')
                self.edges.append(Edge(src, dst, attrs))
                continue
            if item[0] == ATTR:
                if len(item) < 3:
                    raise TypeError('Graph item incomplete')
                key, value = item[1], item[2]
                if not isinstance(key, str) or not isinstance(value, str):
                    raise ValueError('Attribute is malformed')
                self.attrs.setdefault(key, value)
                continue
            raise ValueError('Unknown item')


if __name__ == '__main__':
    g = Graph([
        (ATTR, "foo", "1"),
        (ATTR, "title", "Testing Attrs"),
        (NODE, "a", {"color": "green"}),
        (NODE, "c", {}),
        (NODE, "b", {"label": "Beta!"}),
        (EDGE, "b", "c", {}),
        (EDGE, "a", "b", {"color": "blue"}),
        (ATTR, "bar", "true")
    ])
    print(g.nodes)
    print(g.edges)
    print(g.attrs)
