import unittest
from dm_set.dm_set import DMSet

class TestDMSet(unittest.TestCase):

    def setUp(self):
        self.set1 = DMSet()
        self.set2 = DMSet()
        self.universal_set = DMSet()

        for i in [1, 2, 3]:
            self.set1.add(i)
        for i in [3, 4, 5]:
            self.set2.add(i)
        for i in [1, 2, 3, 4, 5]:
            self.universal_set.add(i)

    def test_add(self):
        self.set1.add(4)
        self.assertTrue(self.set1.contains(4))

    def test_remove(self):
        self.set1.remove(3)
        self.assertFalse(self.set1.contains(3))

    def test_union(self):
        result = self.set1.union(self.set2)
        expected = {1, 2, 3, 4, 5}
        self.assertEqual(str(result), str(expected))

    def test_intersection(self):
        result = self.set1.intersection(self.set2)
        expected = {3}
        self.assertEqual(str(result), str(expected))

    def test_complement(self):
        result = self.set1.complement(self.universal_set)
        expected = {4, 5}
        self.assertEqual(str(result), str(expected))

    def test_difference(self):
        result = self.set1.difference(self.set2)
        expected = {1, 2}
        self.assertEqual(str(result), str(expected))

    def test_symmetric_difference(self):
        result = self.set1.symmetric_difference(self.set2)
        expected = {1, 2, 4, 5}
        self.assertEqual(str(result), str(expected))

if __name__ == '__main__':
    unittest.main()
