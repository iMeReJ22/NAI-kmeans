class Vector:
    def __init__(self, vector):
        self.vector = vector
        self.cluster = -1
        self.distance = 99999999

    def reset(self):
        self.cluster = -1
        self.distance = 99999999
