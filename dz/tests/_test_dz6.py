import pytest
from dz6.dz_6 import *


@pytest.mark.parametrize("key, value", [("apple", 5), ("banana", 7), ("orange", 3)])
def test_add_to_hash_table(self):
        hash_table = HashTable(10)
        hash_table.add_to_hash_table("apple", 5)
        hash_table.add_to_hash_table("banana", 7)
        hash_table.add_to_hash_table("orange", 3)

        self.assertEqual(hash_table.table[hash_table.calculate_hash("apple")], ("apple", 5))
        self.assertEqual(hash_table.table[hash_table.calculate_hash("banana")], ("banana", 7))
        self.assertEqual(hash_table.table[hash_table.calculate_hash("orange")], ("orange", 3))

def test_collision_handling(self):
        hash_table = HashTable(10)
        hash_table.add_to_hash_table("a", 1)
        hash_table.add_to_hash_table("k", 2)
        hash_table.add_to_hash_table("u", 3)

        # Collision for key "a" should be handled by linear probing
        self.assertEqual(hash_table.table[hash_table.calculate_hash("a")], ("a", 1))
        self.assertEqual(hash_table.table[hash_table.calculate_hash("k")], ("k", 2))
        self.assertEqual(hash_table.table[hash_table.calculate_hash("u")], ("u", 3))

if __name__ == '__main__':
    unittest.main()

