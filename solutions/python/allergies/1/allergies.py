class Allergies:

    ALLERGIES = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

    def __init__(self, score):
        self.hits = [hit for hit in bin(score)[2:].rjust(8, '0')[::-1]]

    def allergic_to(self, item):
        return self.hits[self.ALLERGIES.index(item)] == '1'

    @property
    def lst(self):
        return [item for item, hit in zip(self.ALLERGIES, self.hits) if hit == '1']
