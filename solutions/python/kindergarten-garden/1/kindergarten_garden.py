class Garden:

    PLANTS = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets',
    }

    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.diagram = [[plant_key for plant_key in row] for row in diagram.split('\n')]
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)
        plants = []
        for row in self.diagram:
            for i in range(2):
                plants.append(self.PLANTS[row[2 * index + i]])
        return plants

if __name__ == '__main__':
    garden = Garden('VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV')
    print(garden.diagram)
    print(garden.plants('Alice'))
