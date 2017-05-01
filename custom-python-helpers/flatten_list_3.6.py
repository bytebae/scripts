# Run with python3.6 as it uses the yield from keyword
# This is approach applies to lists of lists, numbers and other mixed containers types

from collections import Iterable

def flatten(items):
    for x in items:
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x
