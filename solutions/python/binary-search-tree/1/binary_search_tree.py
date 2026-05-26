class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        if tree_data:
            self.create(tree_data)

    def data(self):
        return self.root

    def sorted_data(self):
        return self.inorder(self.root)

    def create(self, tree_data):
        for data in tree_data:
            if not self.root:
                self.root = TreeNode(data)
                continue
            leaf = TreeNode(data)
            node = self.root
            while True:
                if leaf.data <= node.data:
                    if node.left:
                        node = node.left
                    else:
                        node.left = leaf
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = leaf
                        break

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.data] + self.inorder(node.right)

if __name__ == '__main__':
    tree = BinarySearchTree(["2", "1", "3", "6", "7", "5"])
    print(tree.data())
    print(tree.sorted_data())
