import unittest
import practica1 as p1
class TestPractica1(unittest.TestCase):
    def test_filtrar_pares(self):
        r1 = [1,2,3,4,5,6,7]
        r2 = [1200, 1451, 1300, 129, 2001]
        self.assertEqual(p1.filtrarPares(r1),[2,4,6])
        self.assertEqual(p1.filtrarPares(r2),[1200, 1300])