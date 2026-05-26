from collections import deque


class RelativeDistance:
    def __init__(self, family_tree):
        self.relations = {}
        for person, children in family_tree.items():
            self.relations.setdefault(person, set()).update(children)
            for child in children:
                self.relations.setdefault(child, set()).add(person)
                self.relations[child].update(children)
                self.relations[child].remove(child)

    def degree_of_separation(self, person_a, person_b):
        if person_a not in self.relations:
            raise ValueError(f'Person A not in family tree.')
        if person_b not in self.relations:
            raise ValueError(f'Person B not in family tree.')
        if person_a == person_b:
            return 0
        queue = deque([(person_a, 0)])
        visited = set([person_a])
        while queue:
            current, dist = queue.popleft()
            for neighbor in self.relations[current]:
                if neighbor == person_b:
                    return dist + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        raise ValueError("No connection between person A and person B.")


if __name__ == '__main__':
    family_tree = {
        "Aiko": ["Bao", "Carlos"],
        "Bao": ["Dalia"],
        "Carlos": ["Fatima", "Gustavo"],
        "Dalia": ["Hassan", "Isla"],
        "Fatima": ["Khadija", "Liam"],
        "Gustavo": ["Mina"],
        "Hassan": ["Noah", "Olga"],
        "Isla": ["Pedro"],
        "Javier": ["Quynh", "Ravi"],
        "Khadija": ["Sofia"],
        "Liam": ["Tariq", "Uma"],
        "Mina": ["Viktor", "Wang"],
        "Noah": ["Xiomara"],
        "Olga": ["Yuki"],
        "Pedro": ["Zane", "Aditi"],
        "Quynh": ["Boris"],
        "Ravi": ["Celine"],
        "Sofia": ["Diego", "Elif"],
        "Tariq": ["Farah"],
        "Uma": ["Giorgio"],
        "Viktor": ["Hana", "Ian"],
        "Wang": ["Jing"],
        "Xiomara": ["Kaito"],
        "Yuki": ["Leila"],
        "Zane": ["Mateo"],
        "Aditi": ["Nia"],
        "Boris": ["Oscar"],
        "Celine": ["Priya"],
        "Diego": ["Qi"],
        "Elif": ["Rami"],
        "Farah": ["Sven"],
        "Giorgio": ["Tomoko"],
        "Hana": ["Umar"],
        "Ian": ["Vera"],
        "Jing": ["Wyatt"],
        "Kaito": ["Xia"],
        "Leila": ["Yassin"],
        "Mateo": ["Zara"],
        "Nia": ["Antonio"],
        "Oscar": ["Bianca"],
        "Priya": ["Cai"],
        "Qi": ["Dimitri"],
        "Rami": ["Ewa"],
        "Sven": ["Fabio"],
        "Tomoko": ["Gabriela"],
        "Umar": ["Helena"],
        "Vera": ["Igor"],
        "Wyatt": ["Jun"],
        "Xia": ["Kim"],
        "Yassin": ["Lucia"],
        "Zara": ["Mohammed"],
    }
    rela = RelativeDistance(family_tree)
    print(rela.relations)
    print(rela.degree_of_separation('Wyatt', 'Xia'))
