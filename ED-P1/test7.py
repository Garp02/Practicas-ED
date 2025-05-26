import unittest
import practica1 as p1
import itertools
class TestPractica1(unittest.TestCase):
    def test_suma_digitos(self):
        nums = [1238,49132,389123,32983,2302,9,0]
        res  = [5,1,8,7,7,9,0]
        r = []

        for num in nums:
            r += [p1.sumaDigitos(num)]
        self.assertEqual(res, r)