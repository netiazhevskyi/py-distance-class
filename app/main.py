class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if is_distance_instance(other):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other):
        if is_distance_instance(other):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other):
        if is_distance_instance(other):
            return Distance(self.km * other.km)
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        if is_distance_instance(other):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other):
        if is_distance_instance(other):
            return self.km > other
        return self.km > other

    def __eq__(self, other):
        if is_distance_instance(other):
            return self.km == other.km
        return self.km == other

    def __le__(self, other):
        if is_distance_instance(other):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other):
        if is_distance_instance(other):
            return self.km >= other.km
        return self.km >= other

    def __len__(self):
        return self.km


def is_distance_instance(element):
    return isinstance(element, Distance)
