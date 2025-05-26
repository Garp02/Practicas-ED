import unittest
import practica1 as p1
class TestPractica1(unittest.TestCase):
    def test_dibuja_triangulo(self):
        triangulo1 =  '* \n\n'
        triangulo3 =  '  * \n\n  * \n * * \n\n  * \n * * \n* * * \n\n'
        triangulo5 =  '    * \n\n    * \n   * * \n\n    * \n   * * \n  * * * \n\n'
        triangulo5 += '    * \n   * * \n  * * * \n * * * * \n\n    * \n   * * '
        triangulo5 += '\n  * * * \n * * * * \n* * * * * \n\n'

        self.assertEqual(triangulo1, p1.dibujaTriangulo(1))
        self.assertEqual(triangulo3, p1.dibujaTriangulo(3))
        self.assertEqual(triangulo5, p1.dibujaTriangulo(5))
