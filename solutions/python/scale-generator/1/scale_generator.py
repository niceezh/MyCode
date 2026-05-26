class Scale:

    SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    SHARPMAP = {'A': 0, 'B': 2, 'C': 3, 'D': 5, 'E': 7, 'F#': 9, 'G': 10, 'a': 0, 'b': 2, 'c#': 4, 'd#': 6, 'e': 7, 'f#': 9, 'g#': 11}
    FLATMAP = {'Bb': 1, 'Db': 4, 'Eb': 6, 'F': 8, 'Gb': 9, 'Ab': 11, 'bb': 1, 'c': 3, 'd': 5, 'eb': 6, 'f': 8, 'g': 10}

    def __init__(self, tonic):
        if tonic in self.SHARPMAP:
            self.tonic = tonic
            self.mode = self.SHARPS
            self.index = self.SHARPMAP[tonic]
        elif tonic in self.FLATMAP:
            self.tonic = tonic
            self.mode = self.FLATS
            self.index = self.FLATMAP[tonic]
        else:
            raise ValueError('Invalid tonic!')

    def chromatic(self):
        return self.mode[self.index:] + self.mode[:self.index]

    def interval(self, intervals):
        result = [self.mode[self.index]]
        if not intervals:
            return result
        curindex = self.index
        for interval in intervals:
            if interval == 'm':
                curindex = (curindex + 1) % 12
                result.append(self.mode[curindex])
                continue
            if interval == 'M':
                curindex = (curindex + 2) % 12
                result.append(self.mode[curindex])
                continue
            if interval == 'A':
                curindex = (curindex + 3) % 12
                result.append(self.mode[curindex])
                continue
            raise ValueError('Invalid interval!')
        return result
