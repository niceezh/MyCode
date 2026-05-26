class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.value == other.value and self.left == other.left and self.right == other.right

    def __repr__(self):
        return f"Node({self.value}, {self.left}, {self.right})"


class Zipper:

    VALUE = 'value'
    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self, focus, path):
        self.focus = focus
        self.path = path

    @staticmethod
    def from_tree(tree):
        if tree is None:
            return None
        node = Zipper._dict_to_node(tree)
        return Zipper(node, [])

    @staticmethod
    def _dict_to_node(d):
        if d is None:
            return None
        return Node(d[Zipper.VALUE], Zipper._dict_to_node(d[Zipper.LEFT]), Zipper._dict_to_node(d[Zipper.RIGHT]))

    def value(self):
        return self.focus.value if self.focus else None

    def set_value(self, value):
        if self.focus is None:
            return self
        new_focus = Node(value, self.focus.left, self.focus.right)
        return Zipper(new_focus, self.path)

    def left(self):
        if self.focus is None or self.focus.left is None:
            return None
        new_path = self.path + [(self.focus, Zipper.LEFT)]
        return Zipper(self.focus.left, new_path)

    def set_left(self, tree):
        if self.focus is None:
            return self
        new_left = Zipper._dict_to_node(tree) if isinstance(tree, dict) else tree
        new_focus = Node(self.focus.value, new_left, self.focus.right)
        return Zipper(new_focus, self.path)

    def right(self):
        if self.focus is None or self.focus.right is None:
            return None
        new_path = self.path + [(self.focus, Zipper.RIGHT)]
        return Zipper(self.focus.right, new_path)

    def set_right(self, tree):
        if self.focus is None:
            return self
        new_right = Zipper._dict_to_node(tree) if isinstance(tree, dict) else tree
        new_focus = Node(self.focus.value, self.focus.left, new_right)
        return Zipper(new_focus, self.path)

    def up(self):
        if not self.path:
            return None
        parent, direction = self.path[-1]
        new_path = self.path[:-1]

        new_parent = None
        if direction == Zipper.LEFT:
            new_parent = Node(parent.value, self.focus, parent.right)
        if direction == Zipper.RIGHT:
            new_parent = Node(parent.value, parent.left, self.focus)

        return Zipper(new_parent, new_path)

    def to_tree(self):
        if self.focus is None:
            return None

        current = self.focus
        for parent, direction in reversed(self.path):
            if direction == Zipper.LEFT:
                current = Node(parent.value, current, parent.right)
            if direction == Zipper.RIGHT:
                current = Node(parent.value, parent.left, current)

        return self._node_to_dict(current)

    def _node_to_dict(self, node):
        if node is None:
            return None
        return {
            Zipper.VALUE: node.value,
            Zipper.LEFT: self._node_to_dict(node.left),
            Zipper.RIGHT: self._node_to_dict(node.right)
        }
