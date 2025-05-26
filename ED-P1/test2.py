import unittest
import practica1 as p1
class TestPractica1(unittest.TestCase):
    def test_palindroma(self):
        t1 = p1.esPalindroma("anita lava la tina")
        t2 = p1.esPalindroma("yo dono rosas oro no doy")
        t3 = p1.esPalindroma("aniita lava la tina")
        self.assertTrue(t1)
        self.assertTrue(t2)
        self.assertFalse(t3)