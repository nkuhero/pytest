from enum import Enum, unique

@unique
class Weekday(Enum):

    Sun = 0
    Mon = 1
    Tue = 2


if __name__ == "__main__":
    day = Weekday.Mon
    print(day.value)

