class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.succeeding = node
            self.tail = node
        self.size += 1

    def pop(self):
        if self.tail is None:
            raise IndexError('List is empty')
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.succeeding = None
        else:
            self.head = None
        self.size -= 1
        return value

    def shift(self):
        if self.head is None:
            raise IndexError('List is empty')
        value = self.head.value
        self.head = self.head.succeeding
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        self.size -= 1
        return value

    def unshift(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.succeeding = self.head
            self.head.previous = node
            self.head = node
        self.size += 1

    def delete(self, value):
        node = self.head
        while node:
            if node.value == value:
                if node.previous:
                    node.previous.succeeding = node.succeeding
                else:
                    self.head = node.succeeding
                if node.succeeding:
                    node.succeeding.previous = node.previous
                else:
                    self.tail = node.previous
                self.size -= 1
                return
            node = node.succeeding
        raise ValueError('Value not found')

    def __len__(self):
        return self.size
