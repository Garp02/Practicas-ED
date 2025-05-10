import pathlib
from typing import List
from itertools import product

Asignacion = List[bool]

class Formula:
    """
    Clase para representar fórmulas booleanas.
    """
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
        conectivos=['C','D','I','E','N']
        if (conectivo == None
                and not (isinstance(izquierda, int) and izquierda > -1)):
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

    def __repr__(self):
        """
        Representación en cadena, legible para humanos, de
        las fórmulas.
        """
        return ""

    def lista_variables(self):
        """
        Devuelve la lista de todas las variables que ocurren
        en una fórmula, en orden.
        """
        return []

    def ultima_variable(self):
        """
        Devuelve la última variable que ocurre en una fórmula.
        """
        return 0

    def numero_conectivos(self):
        """
        Devuelve el número de conectivos que ocurren en la fórmula.
        """
        return 0


    def _evalua_aux(self, asignacion: Asignacion, posiciones: List[int]):
        """
        Función auxiliar para evaluar una fórmula. Recibe una lista de
        booleanos (una asignación de verdad), y una lista con las posiciones
        en las que ocurren las variables de la fórmula.
        """
        return 0

    def evalua(self, asignacion: Asignacion):
        """
        Devuelve el valor de verdad de la fórmula bajo una
        asignación dada, que recibe como entrada en la forma
        de una lista de booleanos.
        """
        return 0

    def aplana(self):
        """
        Devuelve una lista con la versión aplanada del árbol
        de sintáxis de la fórmula.
        """
        return []

    def aplana_sin_variables(self):
        """
        Devuelve una lista con la versión aplananada del
        árbol de sintaxis de la fórmula, sin las hojas.
        """
        return []
