# Tuple packing and unpacking
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)