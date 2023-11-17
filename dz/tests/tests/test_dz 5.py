import pytest
from dz5.dz_5 import poisk


@pytest.mark.parametrize("sequence, item, esequencepected", [  
    ([1, 2, 3, 4, 5], 3, 2),    
    ([1, 2, 2, 3, 4, 5], 2, 1),  
    ([0], 0, 0), 
    ([-1, 0, 42], 0, 1), 
    ([-42, 0, 42], 42, 2), 
    ([-6, -5, -4, -3, -2, -1], -4, 2), 
    ([1, 2, 3, 4, 5, 6], 4, 3), 
    ([1, 2, 3, 4, 5, 6, 7], 4, 3),  
    ([42, 42, 42, 42, 42], 42, 0), 
    ([-42, -42, -42, -42, -42], -42, 0), 
    ([42, 42, 42, 42, 43], 43, 4), 
    ([41, 42, 42, 42, 42], 41, 0), 
    ([-2, -2, -1, 0, 1, 2, 2, 2], -1, 2), 
    ([-2, -2, -1, 0, 1, 1, 2, 2], 1, 4) 
])  
def test_poisk(sequence, item, esequencepected):  
    assert poisk(sequence, item) == esequencepected


@pytest.mark.parametrize("sequence, item", [  
      
    ([1, 2, 3, 4, 5], 6), 
    ([], 42), 
    ([1], 0),
    ([0], 1),
    ([1, 2, 3, 4, 5], 7), 
    ([1, 2, 3, 4, 5, 6], 7),
])  
def test_poisk__none(sequence, item):  
    assert poisk(sequence, item) is None
