import pytest
from collections import counter 
from dz5.dz_5 import poisk


assert poisk ([], 42) is None
assert poisk ([0], 0) == 0
assert poisk ([0], 1) is None
assert poisk ([-1, 0, 42], 0) == 1
assert poisk ([-42, 0, 42], 42) == 2
assert poisk ([-6, -5, -4, -3, -2, -1], -4) == 2
assert poisk ([1, 2, 3, 4, 5, 6], 4) == 3
assert poisk ([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert poisk ([1, 2, 3, 4, 5], 7) is None
assert poisk ([1, 2, 3, 4, 5, 6], 7) is None
assert poisk ([42, 42, 42, 42, 42], 42) == 0
assert poisk ([-42, -42, -42, -42, -42], -42) == 0
assert poisk ([42, 42, 42, 42, 43], 43) == 4
assert poisk ([41, 42, 42, 42, 42], 41) == 0
assert poisk ([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
assert poisk ([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4