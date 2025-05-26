import unittest
import practica1 as p1
class TestPractica1(unittest.TestCase):
    def test_promedio_tuplas(self):
        t1 = p1.promedioTuplas(((11,30,7,5.2),(4,1.3,2.222,5.0,9,10,19),(40,30,20,10)))
        t2 = p1.promedioTuplas(((10,20,19),(1,2.1,3.9,4.8),
                                (200,2.00,14,1.9),(4,9,13.9,12.2)))
        self.assertEqual(t1, [13.3, 7.217428571428571, 25.0])
        self.assertEqual(t2, [16.333333333333332, 2.95, 54.475, 9.774999999999999])