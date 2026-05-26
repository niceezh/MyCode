from typing import Optional

class EmptyListException(Exception):
    def __init__(self):
        self.message = "The list is empty."
        super().__init__(self.message)


class Node:
    def __init__(self, value):
        self.mvalue = value
        self.mnext: Optional[Node] = None

    def value(self):
        return self.mvalue

    def next(self):
        return self.mnext


class LinkedList:
    def __init__(self, values=None):
        self.mhead: Optional[Node] = None
        self.mlen = 0
        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        current = self.mhead
        while current:
            yield current.value()
            current = current.next()

    def __len__(self):
        return self.mlen

    def head(self):
        if not self.mhead:
            raise EmptyListException()
        return self.mhead

    def push(self, value):
        node = Node(value)
        node.mnext = self.mhead
        self.mhead = node
        self.mlen += 1

    def pop(self):
        if not self.mhead:
            raise EmptyListException()
        value = self.mhead.value()
        self.mhead = self.mhead.next()
        self.mlen -= 1
        return value

    def reversed(self):
        newlist = LinkedList()
        for value in self:
            newlist.push(value)
        return newlist
