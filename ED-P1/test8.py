import unittest
import practica1 as p1
import itertools
class TestPractica1(unittest.TestCase):
    def test_buscar_coincidencia(self):
        r1 = [1,2,3,4,5,6,7]
        v1=5
        r2 = [1200, 1451, 1300, 129, 2001]
        v2=0
        self.assertEqual(p1.buscarCoincidencia(r1,v1),'T')
        self.assertEqual(p1.buscarCoincidencia(r2,v2),'F')
