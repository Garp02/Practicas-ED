import unittest
import practica1 as p1
class TestPractica1(unittest.TestCase):
    def test_restar(self):
        t1 = p1.restar(10,1)
        t2 = p1.restar(25,6)
        self.assertEqual(t1, 1)
        self.assertEqual(t2, 2)