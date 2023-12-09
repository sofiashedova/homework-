import pytest 
from dz7.dz_7 import bfs 
 
def check(node, t):
    return node == t


@pytest.mark.parametrize("g, s, t, check, expected", [ 
    #({}, 1, 5, check, None),
  #  ({1: [], 2: [], 3: [],  4: [],  5: []}, 1, 5, check, None), 
    ({1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}, 1, 5, check, 2), 
    ({1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}, 1, 4, check, 2), 
    #({1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}, 1, 6, check, None), 
    #({1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}, 1, 1, check, 0), 
]) 
def test_bfs(g, s, t, check, expected): 
    assert bfs(g, s, t, check) == expected
