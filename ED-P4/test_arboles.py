import unittest
import random
from arboles import *

class TestArbol(unittest.TestCase):

    # Prueba que el construcror de árboles sea correcto.
    def test_constructor_arbol(self):
    
        # El izquierdo debe ser árbol
        with self.assertRaises(TypeError):
       
            Arbol(1, 2, Arbol())
       
        # El derecho debe ser árbol
        with self.assertRaises(TypeError):
       
            Arbol(1, Arbol(), 2)
       
        # Constructor vacío
        a = Arbol()
        self.assertEqual(a.raiz, None)
        self.assertEqual(a.izquierdo, None)
        self.assertEqual(a.derecho, None)

        # Constructor con izquierdo y derecho
        a = Arbol(1, Arbol(2), Arbol(3))
        self.assertEqual(a.raiz, 1)
        self.assertEqual(a.izquierdo.raiz, 2)
        self.assertEqual(a.derecho.raiz, 3)

    # Prueba que la función es_vacio funcione correctamente.
    def test_es_vacio(self):
        
        a = Arbol()
        self.assertTrue(a.es_vacio())
        a = Arbol(1)
        self.assertFalse(a.es_vacio())

    # Prueba que la función es_hoja funcione correctamente. 
    def test_es_hoja(self):
        
        a = Arbol()
        self.assertFalse(a.es_hoja())
        a = Arbol(1)
        self.assertTrue(a.es_hoja())
        a = Arbol(1, Arbol(2), None)
        self.assertFalse(a.es_hoja())

    # Prueba que la función copia funcione correctamente.
    def test_copia(self):

        a = Arbol()
        b = a.copia()
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        a = Arbol(random.randint(0, 100))
        b = a.copia()
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        e = []

        for i in range(6):

            e.append(random.randint(0, 100))

        a = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], Arbol(e[5]), None))
        b = a.copia()
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        self.assertIsNot(a.izquierdo, b.izquierdo)
        self.assertIsNot(a.derecho, b.derecho)

    # Prueba que la función num_nodos funcione correctamente.
    def test_num_nodos(self):

        a = Arbol()
        self.assertEqual(a.num_nodos(), 0)
        a = Arbol(random.randint(0, 100))
        self.assertEqual(a.num_nodos(), 1)
        e = []
        for i in range(6):
            e.append(random.randint(0, 100))
        a = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], Arbol(e[5]), None))
        self.assertEqual(a.num_nodos(), 6)

    # Prueba que la función direccion funcione correctamente.        
    def test_direccion(self):

        elemento = 42
        arbol = Arbol()
        # Árbol vacío no contiene a nadie.
        self.assertFalse(arbol.direccion(elemento))
        izquierdo = Arbol(32, Arbol(10), Arbol(2))
        derecho = Arbol(5, Arbol(3), Arbol(21))
        arbol = Arbol(16, izquierdo, derecho)
        # El elemento no está contenido
        self.assertFalse(arbol.direccion(elemento))
        izquierdo.raiz = 42
        # El elemento está en la posición 0
        self.assertEqual(arbol.direccion(elemento), "0")
        izquierdo.raiz = 32
        derecho.izquierdo.raiz = 42
        # El elemento está en la posición 10
        self.assertEqual(arbol.direccion(elemento), "10")


    # Prueba que la función gira funcione correctamente. 
    def test_gira(self):

        a = Arbol()
        b = a.gira("")
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        a = Arbol("hola")
        b = a.gira("")
        self.assertIsNot(a, b)
        self.assertEqual(a, b)
        izquierdo = Arbol(32, Arbol(10), Arbol(2))
        derecho = Arbol(5, Arbol(3), Arbol(21))
        a = Arbol(16, izquierdo, derecho)
        b = a.gira("")
        c = Arbol(16, derecho.copia(), izquierdo.copia())
        self.assertIsNot(b, c)
        self.assertEqual(b, c)
        b = a.gira("0")
        c = Arbol(16, Arbol(izquierdo.raiz, izquierdo.derecho.copia(), izquierdo.izquierdo.copia()), derecho.copia())
        self.assertIsNot(b, c)
        self.assertEqual(b, c)
        b = a.gira("1")
        c = Arbol(16, izquierdo.copia(), Arbol(derecho.raiz, derecho.derecho.copia(), derecho.izquierdo.copia()))
        self.assertIsNot(b, c)
        self.assertEqual(b, c)

    # Prueba que la función es_isomorfo funcione correctamente.        
    def test_es_isomorfo(self):

        a = Arbol()
        b = Arbol()
        self.assertTrue(a.es_isomorfo(b))
        x = random.randint(0, 100)
        a = Arbol(x)
        b = Arbol(x)
        self.assertTrue(a.es_isomorfo(b))
        e = []
        
        for i in range(6):
            
            e.append(random.randint(0, 100))

        a = Arbol(e[0], Arbol(e[1]), Arbol(e[2]))
        b = Arbol(e[0], Arbol(e[1]), Arbol(e[2]))
        c = Arbol(e[0], Arbol(e[2]), Arbol(e[1]))

        self.assertTrue(a.es_isomorfo(b))
        self.assertTrue(c.es_isomorfo(b))
        self.assertTrue(a.es_isomorfo(a))

        a = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], Arbol(e[5]), None))
        b = Arbol(e[0], Arbol(e[4], Arbol(e[5]), None), Arbol(e[1], Arbol(e[2]), Arbol(e[3])))
        c = Arbol(e[0], Arbol(e[1], Arbol(e[2]), Arbol(e[3])), Arbol(e[4], None, Arbol(e[5])))
        d = Arbol(e[0], Arbol(e[1], Arbol(e[3]), Arbol(e[2])), Arbol(e[4], None, Arbol(e[5])))

        self.assertTrue(a.es_isomorfo(b))
        self.assertTrue(c.es_isomorfo(b))
        self.assertTrue(a.es_isomorfo(a))
        self.assertTrue(a.es_isomorfo(d))
        self.assertTrue(c.es_isomorfo(d))
        self.assertTrue(b.es_isomorfo(d))

        c = a.copia()
        
        self.assertTrue(a.es_isomorfo(c))
        self.assertTrue(a.es_isomorfo(a))
        
    # Prueba que la función lca funcione correctamente.
    def test_lca(self):
        
        t7 = Arbol(7)
        t6 = Arbol(6)
        t4= Arbol(4,t6,t7)
        t5 = Arbol(5)
        t3 = Arbol(3,t4,t5)
        t2 = Arbol(2)
        t1 = Arbol(1,t2,t3)
        self.assertEqual(t1.lca(6,7),"10")
        self.assertEqual(t1.lca(5,6),"1")