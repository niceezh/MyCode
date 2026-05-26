class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        if self.properties != other.properties:
            return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if not input_string:
        raise ValueError('tree missing')
    pos = 0
    n = len(input_string)

    def peek():
        return input_string[pos] if pos < n else None

    def consume():
        nonlocal pos
        pos += 1

    def parse_value():
        if peek() != '[':
            raise ValueError('properties without delimiter')
        consume()
        value_chars = []
        while True:
            c = peek()
            if c is None:
                raise ValueError('unexpected end of input')
            if c == ']':
                consume()
                break
            if c == '\\':
                consume()
                next_c = peek()
                if next_c is None:
                    raise ValueError('unexpected end of input')
                consume()
                if next_c == '\n':
                    continue
                elif next_c.isspace():
                    value_chars.append(' ')
                else:
                    value_chars.append(next_c)
            else:
                consume()
                value_chars.append(' ' if c == '\t' else c)
        return ''.join(value_chars)

    def parse_node():
        if peek() != ';':
            raise ValueError('node expected')
        consume()
        properties = {}
        while True:
            c = peek()
            if c in (None, ';', '(', ')'):
                break
            prop_key = []
            while c is not None and c.isupper():
                prop_key.append(c)
                consume()
                c = peek()
            key_str = ''.join(prop_key)
            if not key_str:
                if c is not None and c.islower():
                     raise ValueError('property must be in uppercase')
                else:
                    raise ValueError('properties without delimiter')
            if c is not None and c.islower():
                 raise ValueError('property must be in uppercase')
            values = []
            if peek() != '[':
                raise ValueError('properties without delimiter')
            while peek() == '[':
                values.append(parse_value())
            properties[key_str] = values
        return SgfTree(properties=properties)

    def parse_game_tree():
        if peek() != '(':
            raise ValueError('tree missing')
        consume()
        if peek() == ')':
             consume()
             raise ValueError('tree with no nodes')
        if peek() != ';':
             raise ValueError('tree with no nodes')
        nodes = []
        while peek() == ';':
            nodes.append(parse_node())
        root_node = nodes[0]
        current = root_node
        for next_node in nodes[1:]:
            current.children = [next_node]
            current = next_node
        while peek() == '(':
            current.children.append(parse_game_tree())
        if peek() != ')':
            raise ValueError('tree missing')
        consume()
        return root_node

    result = parse_game_tree()
    if pos != n:
        raise ValueError('tree missing')
    return result
