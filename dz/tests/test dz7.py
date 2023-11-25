import unittest
from dz7 import bfs



class BfsSearchTest(unittest.TestCase):
    def test_bfs_search(self):
        # Тест 1: граф без путей
        g1 = {
            'A': [],
            'B': [],
            'C': []
        }
        assert bfs(g1, 'A', 'C') == None

        # Тест 2: простой граф
        g2 = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C', 'E'],
            'E': ['D']
        }
        assert bfs(g2, 'A', 'E') == 3

        # Тест 3: граф с циклом
        g3 = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C', 'E'],
            'E': ['D']
        }
        assert bfs(g3, 'A', 'A') == 0

        # Тест 4: граф с несколькими путями
        g4 = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'E'],
            'D': ['B', 'E'],
            'E': ['C', 'D']
        }
        assert bfs(g4, 'A', 'E') == 2

        # Тест 5: когда граф не пустой, но мы ничего не нашли
        g5 = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'E'],
            'D': ['B', 'F'],
            'E': ['C', 'F'],
            'F': ['D', 'E']
        }
        assert bfs(g5, 'A', 'G') == None