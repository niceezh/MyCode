VALUE = 'v'
LEFT = 'l'
RIGHT = 'r'

def tree_from_traversals(preorder, inorder):
    if preorder is None or inorder is None:
        raise ValueError('traversals cannot be None')
    if len(preorder) != len(inorder):
        raise ValueError('traversals must have the same length')
    if set(preorder) != set(inorder):
        raise ValueError('traversals must have the same elements')
    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError('traversals must contain unique items')
    if len(preorder) == 0 and len(inorder) == 0:
        return {}
    try:
        return build_tree(preorder, inorder)
    except:
        raise ValueError('traversals must be consistent')

def build_tree(preorder, inorder):
    root_value = preorder[0]
    left_size = inorder.index(root_value)
    right_size = len(preorder) - left_size - 1
    return {
        VALUE: root_value,
        LEFT: build_tree(preorder[1:left_size+1], inorder[:left_size]) if left_size else {},
        RIGHT: build_tree(preorder[left_size+1:], inorder[left_size+1:]) if right_size else {},
    }

if __name__ == '__main__':
    print(tree_from_traversals(['a', 'b', 'd', 'g', 'h', 'c', 'e', 'f', 'i'], ['g', 'd', 'h', 'b', 'a', 'e', 'c', 'i', 'f']))

