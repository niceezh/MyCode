class CustomSet:
    def __init__(self, elements=[]):
        self.elements = set(elements)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return self.elements.issubset(other.elements)

    def isdisjoint(self, other):
        return self.elements.isdisjoint(other.elements)

    def __eq__(self, other):
        return self.elements == other.elements

    def add(self, element):
        self.elements.add(element)

    def intersection(self, other):
        return CustomSet(list(self.elements.intersection(other.elements)))

    def __sub__(self, other):
        return CustomSet(list(self.elements.difference(other.elements)))

    def __add__(self, other):
        return CustomSet(list(self.elements.union(other.elements)))
