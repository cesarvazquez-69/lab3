from typing import *
from dataclasses import dataclass
import unittest
import sys
sys.setrecursionlimit(10**6)





@dataclass(frozen=True)
class Empty:
    pass

@dataclass(frozen=True)
class Link:
    first: int
    rest: "LinkedList"

LinkedList = Union[Empty, Link]



def range(max_exclusive: int) -> LinkedList:
    return range_from(0, max_exclusive)


def range_from(current: int, max_exclusive: int) -> LinkedList:
    if current == max_exclusive:
        return Empty()
    else:
        return Link(current, range_from(current + 1, max_exclusive))
    


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






class Tests(unittest.TestCase):

    def test_range_5(self):
        self.assertEqual(
            range(5),
            Link(0, Link(1, Link(2, Link(3, Link(4, Empty())))))
        )

    def test_occurs_true(self):
        lst = Link(0, Link(1, Link(2, Empty())))
        self.assertTrue(occurs(1, lst))

    def test_occurs_false(self):
        lst = Link(0, Link(1, Link(2, Empty())))
        self.assertFalse(occurs(5, lst))

    
    def test_has_dup_true(self):
        lst = Link(1, Link(2, Link(1, Empty())))
        self.assertTrue(has_dup(lst))

    def test_has_dup_false(self):
        lst = Link(1, Link(2, Link(3, Empty())))
        self.assertFalse(has_dup(lst))

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(Empty()), Empty())
        self.assertEqual(insertion_sort(Link(5, Empty())), Link(5, Empty()))
        self.assertEqual(
            insertion_sort(Link(3, Link(1, Link(2, Empty())))),
            Link(1, Link(2, Link(3, Empty())))
        )
        self.assertEqual(
            insertion_sort(Link(4, Link(2, Link(4, Link(1, Empty()))))),
            Link(1, Link(2, Link(4, Link(4, Empty()))))
        )





# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module.
if (__name__ == '__main__'):
    unittest.main()
