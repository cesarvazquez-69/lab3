from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)


@dataclass
class Tests(unittest.TestCase):

pass



class Node:
    value: int
    next: Optional['Node']

def range(max_exclusive: int) -> Optional['Node']:
    # Accepts an integer larger than 0 & returns a LinkedList
    if max_exclusive == 0:
        return None
    else:
        rest = range(max_exclusive -1)
        return append(rest, max_exclusive - 1)
    

def append (lst: Optional[Node], value: int) -> Node:
    if lst is None:
        return Node(value, None)
    else:
        return Node (lst.value, append(lst,next, value))

    







# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module.
if (__name__ == '__main__'):
unittest.main()
