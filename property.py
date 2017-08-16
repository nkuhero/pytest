class Student(object):

    def __init__(self, name, score):
        self._name = name
        self._score = score

    @property
    def score(self):
        return self._score


    @score.setter
    def score(self, value):
        self._score = value


if __name__ == "__main__":
    s = Student("Bob", 90)
    s.score = 100
    print(s.score)
