import unittest
import practica1 as p1
import itertools
class TestPractica1(unittest.TestCase):
    def restar(self):
        t1 = p1.restar(5,2)
        t2 = p1.restar(336,-90)
        self.assertEqual(t1, 3)
        self.assertEqual(t2, 426)

    def test_palindroma(self):
        t1 = p1.esPalindroma("anita lava la tina")
        t2 = p1.esPalindroma("yo dono rosas oro no doy")
        t3 = p1.esPalindroma("aniita lava la tina")
        self.assertTrue(t1)
        self.assertTrue(t2)
        self.assertFalse(t3)


    def test_promedio_tuplas(self):
        t1 = p1.promedioTuplas(((11,30,7,5.2),(4,1.3,2.222,5.0,9,10,19),(40,30,20,10)))
        t2 = p1.promedioTuplas(((10,20,19),(1,2.1,3.9,4.8),
                                (200,2.00,14,1.9),(4,9,13.9,12.2)))
        self.assertEqual(t1, [13.3, 7.217428571428571, 25.0])
        self.assertEqual(t2, [16.333333333333332, 2.95, 54.475, 9.774999999999999])


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

    def test_filtrar_pares(self):
        r1 = [1,2,3,4,5,6,7]
        r2 = [1200, 1451, 1300, 129, 2001]
        self.assertEqual(p1.filtrarPares(r1),[2,4,6])
        self.assertEqual(p1.filtrarPares(r2),[1200, 1300])

    def test_suma_digitos(self):
        nums = [1238,49132,389123,32983,2302,9,0]
        res  = [5,1,8,7,7,9,0]
        r = []

        for num in nums:
            r += [p1.sumaDigitos(num)]
        self.assertEqual(res, r)

    def test_dibuja_triangulo(self):
        triangulo1 =  '* \n\n'
        triangulo3 =  '  * \n\n  * \n * * \n\n  * \n * * \n* * * \n\n'
        triangulo5 =  '    * \n\n    * \n   * * \n\n    * \n   * * \n  * * * \n\n'
        triangulo5 += '    * \n   * * \n  * * * \n * * * * \n\n    * \n   * * '
        triangulo5 += '\n  * * * \n * * * * \n* * * * * \n\n'

        self.assertEqual(triangulo1, p1.dibujaTriangulo(1))
        self.assertEqual(triangulo3, p1.dibujaTriangulo(3))
        self.assertEqual(triangulo5, p1.dibujaTriangulo(5))
