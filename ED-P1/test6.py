import unittest
import practica1 as p1
import itertools
class TestPractica1(unittest.TestCase):
    def test_permutaciones(self):
        r1 = [1,2,3]
        r2 = [1,2,3,4,5]
        t1 = itertools.permutations(r1)
        t2 = itertools.permutations(r2)
        t1_p = p1.permutaciones(r1)
        t2_p = p1.permutaciones(r2)
        self.assertEqual(len(t1_p), 6)
        self.assertEqual(len(t2_p),120)
        for p in t1:
            self.assertTrue(list(p) in t1_p)
        for p in t2:
            self.assertTrue(list(p) in t2_p)