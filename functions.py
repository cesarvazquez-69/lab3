from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)



@dataclass
class Tests(unittest.TestCase):

pass


@dataclass(frozen=True)
class Empty:
    pass

@dataclass(frozen=True)
class Link:
    first: int
    rest: "LinkedList"

LinkedList = Union[Empty, Link]

class Node:
    value: int
    next: Optional['Node']

def range(max_exclusive: int) -> Optional['Node']:
    # Accepts an integer larg er than 0 & returns a LinkedList
    if max_exclusive == 0:
        return None
    else:
        rest = range(max_exclusive -1)
        return append(rest, max_exclusive - 1)
    

def occurs(value: int, lst: Optional[Node]) -> bool:
    if lst is None:
        return False
    elif lst.value == value: 
        return True
    else:
        return occurs(value, lst.next)

def has_dup(lst: Optional[Node]) -> bool:
    if lst is None:
        return False
    elif occurs(lst.value, lst.next):
        return True
    else:
        return has_dup(lst.next)


def append (lst: Optional[Node], value: int) -> Node:
    if lst is None:
        return Node(value, None)
    else:
        return Node (lst.value, append(lst.next, value))





class Tests(unittest.TestCase):

    def test_range_5(self):
        self.assertEqual(
            range(5),
            Node(0, Node(1, Node(2, Node(3, Node(4, None)))))
        )

    def test_occurs_true(self):
        lst = Node(0, Node(1, Node(2, None)))
        self.assertTrue(occurs(1, lst))

    def test_occurs_false(self):
        lst = Node(0, Node(1, Node(2, None)))
        self.assertFalse(occurs(5, lst))

    
    def test_has_dup_true(self):
        lst = Node(1, Node(2, Node(1, None)))
        self.assertTrue(has_dup(lst))

    def test_has_dup_false(self):
        lst = Node(1, Node(2, Node(3, None)))
        self.assertFalse(has_dup(lst))



# Returns True if n appears in nums.
def occurs(n: int, nums: LinkedList) -> bool:
    match nums:
        case Empty():
            return False
        case Link(first, rest):
            return first == n or occurs(n, rest)
  # Returns True if any number appears more than once.
def has_dup(nums: LinkedList) -> bool:
    match nums:
        case Empty():
            return False
        case Link(first, rest):
            return occurs(first, rest) or has_dup(rest)

# Inserts n into a sorted linked list in ascending order.
def insert(n: int, nums: LinkedList) -> LinkedList:
    match nums:
        case Empty():
            return Link(n, Empty())
        case Link(first, rest):
            if n <= first:
                return Link(n, nums)
            return Link(first, insert(n, rest))


# Returns a sorted version of nums in ascending order.
def insertion_sort(nums: LinkedList) -> LinkedList:
    match nums:
        case Empty():
            return Empty()
        case Link(first, rest):
            return insert(first, insertion_sort(rest))





# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module.
if (__name__ == '__main__'):
unittest.main()
