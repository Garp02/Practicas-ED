import unittest
import practica1 as p1
import linkedList as linked
class TestPractica1(unittest.TestCase):
    def test_obtenerGises(self):
        l1 = linked.LinkedList()
        l1.insertAtBegin(2)
        l1.insertAtBegin(2)
        l1.insertAtBegin(10)
        l1.insertAtBegin(4)
        t1 = p1.obtenerGises(l1)
        self.assertEqual(t1, 18)
