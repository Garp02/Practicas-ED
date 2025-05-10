import pathlib
from typing import List
from itertools import product

Asignacion = List[bool]

# Clase para representar fórmulas booleanas.
class Formula:

    def __init__(self, izquierda, conectivo = None, derecha = None):
        """
        Constructor para la clase. En el caso de las variables,
        izquierda es el identificador de la variable, debe ser
        un entero, y conectivo y derecha deben ser None. El atributo
        conectivo debe ser un string, 'C'(onjunción), 'D'(isyunción),
        'I'(mplicación), 'N'(egación) o 'E'(quivalente). Para
        cualquier fórmula que no sea una variable, el atributo
        izquierda debe ser una fórmula, y para las fórmulas con
        conectivo distinto a 'N', el atributo derecho también tiene
        que ser una fórmula.
        """

        conectivos = ['C','D','I','E','N']

        if (conectivo == None and not (isinstance(izquierda, int) and izquierda > -1)):
            
            raise TypeError("Las variables deben ser naturales")
        
        elif conectivo != None:
        
            if not isinstance(izquierda, Formula):
        
                raise TypeError("Los conectivos deben aplicarse a fórmulas")
        
            elif (conectivo == 'N' and derecha != None):
        
                raise TypeError("En la negación no debe existir fórmula derecha")
        
            elif (conectivo not in conectivos):
        
                raise ValueError("El conectivo es incorrecto")
        
            elif (conectivo != 'N' and not isinstance(derecha, Formula)):
        
                raise TypeError("Los conectivos deben aplicarse a fórmulas")
        
        self.izquierda = izquierda
        self.conectivo = conectivo
        self.derecha   = derecha

 
    # Representación en cadena, legible para humanos, de las fórmulas.
    def __repr__(self):

        # Si es una variable
        if self.conectivo is None:
            
            return f'x{self.izquierda}'
        
        # Si es una negación
        elif self.conectivo == 'N':
        
            return f'(¬{self.izquierda})'
        
        # Si es una conjunción
        elif self.conectivo == 'C':
        
            return f'({self.izquierda} ∧ {self.derecha})'
        
        # Si es una disyunción
        elif self.conectivo == 'D':
        
            return f'({self.izquierda} ∨ {self.derecha})'
        
        # Si es una implicación
        elif self.conectivo == 'I':
        
            return f'({self.izquierda} → {self.derecha})'
        
        # Si es un bicondicional (equivalencia)
        elif self.conectivo == 'E':
        
            return f'({self.izquierda} ↔ {self.derecha})'

        return ""

    # Devuelve la lista de todas las variables que ocurren en una fórmula, en orden.
    def lista_variables(self):
        
        return []

    # Devuelve la última variable que ocurre en una fórmula.
    def ultima_variable(self):
        
        return 0

    # Devuelve el número de conectivos que ocurren en la fórmula.
    def numero_conectivos(self):
        
        return 0

    # Función auxiliar para evaluar una fórmula
    def _evalua_aux(self, asignacion: Asignacion, posiciones: List[int]):
        
        return 0

    # Devuelve el valor de verdad de la fórmula bajo una asignación dada.
    def evalua(self, asignacion: Asignacion):
        
        return 0

    # Devuleve una lista con la versión aplanada del árbol de sintáxis de la fórmula.
    def aplana(self):

        return []

    # Devuelve una lista con la versión aplanada del árbol de sintáxis de la fórmula, sin las hojas.
    def aplana_sin_variables(self):

        return []
