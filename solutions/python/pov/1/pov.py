from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __str__(self, indent=None):
        return dumps(self.to_dict(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def to_dict(self):
        return {self.label: [c.to_dict() for c in sorted(self.children)]}

    def _find_path_from_root(self, target_label):
        if self.label == target_label:
            return [self]

        for child in self.children:
            path = child._find_path_from_root(target_label)
            if path:
                return [self] + path

        return []

    def from_pov(self, from_node):
        path = self._find_path_from_root(from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")

        def _reroot(node, target_label, new_parent_subtree=None):
            if node.label == target_label:
                new_children = list(node.children)
                if new_parent_subtree:
                    new_children.append(new_parent_subtree)

                return Tree(node.label, new_children)

            next_node_on_path = None
            for child in node.children:
                if child._find_path_from_root(target_label):
                    next_node_on_path = child
                    break

            if not next_node_on_path:
                raise ValueError("Tree could not be reoriented")

            new_siblings_for_next = []
            for child in node.children:
                if child is not next_node_on_path:
                    new_siblings_for_next.append(child)

            if new_parent_subtree:
                new_siblings_for_next.append(new_parent_subtree)

            reconstructed_current_subtree = Tree(node.label, new_siblings_for_next)
            return _reroot(next_node_on_path, target_label, reconstructed_current_subtree)

        return _reroot(self, from_node)

    def path_to(self, from_node, to_node):
        try:
            rerooted_tree = self.from_pov(from_node)
        except ValueError:
            raise ValueError("Tree could not be reoriented")

        path_nodes = rerooted_tree._find_path_from_root(to_node)

        if not path_nodes:
            raise ValueError("No path found")

        return [node.label for node in path_nodes]
