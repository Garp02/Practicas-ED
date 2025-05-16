import unittest
import random
from itertools import product
from formulas import *

class TestFormula(unittest.TestCase):

    # Prueba que el constructor de Formula funcione para variables.
    def test_constructor_variable(self):

        n = random.randint(0,100)
        x = Formula(n)

        self.assertIsInstance(x, Formula)
        self.assertEqual(x.izquierda, n)
        self.assertIsNone(x.conectivo)
        self.assertIsNone(x.derecha)

    # Prueba que el constructor de Formula funcione para negaciones.
    def test_constructor_negacion(self):
        
        n = random.randint(0,100)
        x = Formula(n)
        negacion = Formula(x, 'N')
        self.assertIsInstance(negacion, Formula)
        self.assertEqual(negacion.izquierda, x)
        self.assertEqual(negacion.conectivo, 'N')
        self.assertIsNone(negacion.derecha)

    # Prueba que el constructor de Formula funcione para conjunciones.
    def test_constructor_conjuncion(self):

        n = random.randint(0,100)
        m = random.randint(0,100)

        while m == n:
        
            m = random.randint(0,100)
        
        x = Formula(n)
        y = Formula(m)
        conjuncion = Formula(x, 'C', y)
        
        self.assertIsInstance(conjuncion, Formula)
        self.assertEqual(conjuncion.izquierda, x)
        self.assertEqual(conjuncion.conectivo, 'C')
        self.assertEqual(conjuncion.derecha, y)

    # Prueba que el constructor de Formula funcione para disyunciones.
    def test_constructor_disyuncion(self):

        n = random.randint(0,100)
        m = random.randint(0,100)

        while m == n:
        
            m = random.randint(0,100)
        
        x = Formula(n)
        y = Formula(m)
        disyuncion = Formula(x, 'D', y)
        
        self.assertIsInstance(disyuncion, Formula)
        self.assertEqual(disyuncion.izquierda, x)
        self.assertEqual(disyuncion.conectivo, 'D')
        self.assertEqual(disyuncion.derecha, y)

    # Prueba que el constructor de Formula funcione para implicaciones.
    def test_constructor_implicacion(self):

        n = random.randint(0,100)
        m = random.randint(0,100)

        while m == n:
        
            m = random.randint(0,100)
        
        x = Formula(n)
        y = Formula(m)
        implicacion = Formula(x, 'I', y)
        
        self.assertIsInstance(implicacion, Formula)
        self.assertEqual(implicacion.izquierda, x)
        self.assertEqual(implicacion.conectivo, 'I')
        self.assertEqual(implicacion.derecha, y)

    # Prueba que el constructor de Formula funcione para bicondicionales.
    def test_constructor_bicondicional(self):

        n = random.randint(0,100)
        m = random.randint(0,100)

        while m == n:
        
            m = random.randint(0,100)
        
        x = Formula(n)
        y = Formula(m)
        bicondicional = Formula(x, 'E', y)
        
        self.assertIsInstance(bicondicional, Formula)
        self.assertEqual(bicondicional.izquierda, x)
        self.assertEqual(bicondicional.conectivo, 'E')
        self.assertEqual(bicondicional.derecha, y)

    # Prueba que __repr__ de Formula funcione para variables.
    def test_repr_variable(self):

        n = random.randint(0,100)
        x = Formula(n)
        self.assertEqual(repr(x), f'x{n}')

    # Prueba que __repr__ de Formula funcione para negaciones.
    def test_repr_negacion(self):

        n = random.randint(0,100)
        x = Formula(n)
        f = Formula(x,'N')
        self.assertEqual(repr(f), f'(¬x{n})')

    # Prueba que __repr__ de Formula funcione para conjunciones y disyunciones
    def test_repr_conjuncion_disyuncion(self):

        n = random.randint(0,100)
        m = random.randint(0,100)
        
        while m == n:
        
            m = random.randint(0,100)
        
        x = Formula(n)
        y = Formula(m)
        
        conjuncion = Formula(x, 'C', y)
        disyuncion = Formula(x, 'D', y)
        
        self.assertEqual(repr(conjuncion), f'(x{n} ∧ x{m})')
        self.assertEqual(repr(disyuncion), f'(x{n} ∨ x{m})')

    # Prueba que __repr__ de Formula funcione para implicaciones.
    def test_repr_implicacion(self):

        n = random.randint(0,100)
        m = random.randint(0,100)

        while m == n:

            m = random.randint(0,100)

        x = Formula(n)
        y = Formula(m)
        implicacion = Formula(x, 'I', y)

        self.assertEqual(repr(implicacion), f'(x{n} → x{m})')

    # Prueba que __repr__ de Formula funcione para bicondicionales.
    def test_repr_bicondicional(self):

        n = random.randint(0,100)
        m = random.randint(0,100)

        while m == n:
        
            m = random.randint(0,100)
        
        x = Formula(n)
        y = Formula(m)
        bicondicional = Formula(x, 'E', y)
        
        self.assertEqual(repr(bicondicional), f'(x{n} ↔ x{m})')

    # Prueba que lista_variables de Formula funcione para todas las formulas.
    def test_lista_variables(self):

        x1 = Formula(0)
        x2 = Formula(1)
        x3 = Formula(2)
        x4 = Formula(3)
        x5 = Formula(4)

        f1 = Formula(x1,'N')
        f2 = Formula(x2,'C',x3)
        f3 = Formula(x4,'C',f1)
        f4 = Formula(f2,'D',x5)
        f5 = Formula(x5,'I',x3)
        f6 = Formula(f3,'I',f4)
        f7 = Formula(f5,'E',f6)

        self.assertEqual(x1.lista_variables() , [0])
        self.assertEqual(f1.lista_variables() , [0])
        self.assertEqual(f2.lista_variables() , [1,2])
        self.assertEqual(f3.lista_variables() , [0,3])
        self.assertEqual(f4.lista_variables() , [1,2,4])
        self.assertEqual(f5.lista_variables() , [2,4])
        self.assertEqual(f6.lista_variables() , [0,1,2,3,4])
        self.assertEqual(f7.lista_variables() , [0,1,2,3,4])
    
    # Prueba que el método ultima_variable de Formula funcione para todas las formulas.
    def test_ultima_variable(self):
    
        x1 = Formula(0)
        x2 = Formula(1)
        x3 = Formula(2)
        x4 = Formula(3)
        x5 = Formula(4)

        f1 = Formula(x1,'N')
        f2 = Formula(x2,'C',x3)
        f3 = Formula(x4,'D',f1)
        f4 = Formula(f2,'I',x5)
        f5 = Formula(x5,'E',x3)

        self.assertEqual(x1.ultima_variable(), 0)
        self.assertEqual(f1.ultima_variable(), 0)
        self.assertEqual(f2.ultima_variable(), 2)
        self.assertEqual(f3.ultima_variable(), 3)
        self.assertEqual(f4.ultima_variable(), 4)
        self.assertEqual(f5.ultima_variable(), 4)

    # Prueba que el método numero_conectivos de Formula funcione para todas las fórmulas.
    def test_numero_conectivos(self):

        x1 = Formula(0)
        x2 = Formula(1)
        x3 = Formula(2)
        x4 = Formula(3)
        x5 = Formula(4)

        f1 = Formula(x1,'N')
        f2 = Formula(x2,'C',x3)
        f3 = Formula(x4,'D',f1)
        f4 = Formula(f2,'I',f3)
        f5 = Formula(f4,'E',x5)

        self.assertEqual(x1.numero_conectivos(), 0)
        self.assertEqual(f1.numero_conectivos(), 1)
        self.assertEqual(f2.numero_conectivos(), 1)
        self.assertEqual(f3.numero_conectivos(), 2)
        self.assertEqual(f4.numero_conectivos(), 4)
        self.assertEqual(f5.numero_conectivos(), 5)
    
    # Prueba que el método evalua de Formula funcione para variables.
    def test_evalua_variable(self):
    
        x = Formula(0)
        self.assertEqual(x.evalua([0]), 0)
        self.assertEqual(x.evalua([1]), 1)
    
    # Prueba que el método evalua de Formula funcione para la negacion.
    def test_evalua_negacion(self):
    
        x = Formula(0)
        f = Formula(x,'N')
        self.assertEqual(f.evalua([0]), 1)
        self.assertEqual(f.evalua([1]), 0)


    # Prueba que el método evalua de Formula funcione para conjunciones.
    def test_evalua_conjuncion(self):
    
        x = Formula(0)
        y = Formula(1)
        conjuncion = Formula(x, 'C', y)
        asignaciones = product([0,1], repeat = 2)

        for asignacion in asignaciones:
        
            self.assertEqual(conjuncion.evalua(asignacion), asignacion[0] and asignacion[1])
    
    # Prueba que el método evalua de Formula funcione para disyunciones.
    def test_evalua_disyuncion(self):

        x = Formula(0)
        y = Formula(1)
        disyuncion = Formula(x, 'D', y)
        asignaciones = product([0,1], repeat = 2)
        
        for asignacion in asignaciones:
           
            self.assertEqual(disyuncion.evalua(asignacion), asignacion[0] or asignacion[1])
    
    # Prueba que el método evalua de Formula funcione para implicaciones.
    def test_evalua_implicacion(self):

        x = Formula(0)
        y = Formula(1)

        implicacion = Formula(x, 'I', y)
        
        asignaciones = product([0,1], repeat = 2)
        for asignacion in asignaciones:
        
            self.assertEqual(implicacion.evalua(asignacion), not asignacion[0] or asignacion[1])

    # Prueba que el método evalua de Formula funcione para bicondicionales.
    def test_evalua_bicondicional(self):

        x = Formula(0)
        y = Formula(1)

        bicondicional = Formula(x, 'E', y)

        asignaciones = product([0,1], repeat = 2)

        for asignacion in asignaciones:
            self.assertEqual(bicondicional.evalua(asignacion), (not asignacion[0] or asignacion[1]) and (not asignacion[1] or asignacion[0]))

if __name__ == "__main__":
    unittest.main()