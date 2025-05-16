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

        conectivos = ['C','D','I','E','N','B']

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
        elif self.conectivo == 'E' or self.conectivo == 'B':
        
            return f'({self.izquierda} ↔ {self.derecha})'

        return ""

    # Devuelve la lista de todas las variables que ocurren en una fórmula, en orden.
    def lista_variables(self):

        # Si es una variable
        if self.conectivo is None:

            return [self.izquierda]
        
        # Si es una negación
        elif self.conectivo == 'N':

            return self.izquierda.lista_variables()
        
        # Si es un conectivo binario
        else:

            # Combinar las variables de ambas subfórmulas
            izq_vars = self.izquierda.lista_variables()
            der_vars = [] if self.derecha is None else self.derecha.lista_variables()
            
            # Eliminar duplicados manteniendo el orden
            resultado = []

            # Ordenar las variables numéricamente para asegurar consistencia
            todas_vars = sorted(set(izq_vars + der_vars))
            return todas_vars

    # Devuelve la última variable que ocurre en una fórmula.
    def ultima_variable(self):

        # Si es una variable
        if self.conectivo is None:
        
            return self.izquierda
        
        # Si es una negación
        elif self.conectivo == 'N':
        
            return self.izquierda.ultima_variable()
        
        # Si es un conectivo binario
        else:
        
            # Obtener la última variable de la subfórmula izquierda
            izq_var = self.izquierda.ultima_variable()
            
            # Obtener la última variable de la subfórmula derecha (si existe)
            der_var = 0 if self.derecha is None else self.derecha.ultima_variable()
            
            # Devolver la mayor de las dos
            return max(izq_var, der_var)

    # Devuelve el número de conectivos que ocurren en la fórmula.
    def numero_conectivos(self):

        # Si es una variable
        if self.conectivo is None:
        
            return 0
        
        # Si es una negación
        elif self.conectivo == 'N':
        
            return 1 + self.izquierda.numero_conectivos()
        
        # Si es un conectivo binario
        else:
        
            return 1 + self.izquierda.numero_conectivos() + self.derecha.numero_conectivos()

    # Función auxiliar para evaluar una fórmula
    def _evalua_aux(self, asignacion: Asignacion, posiciones: dict):

        # Si es una variable
        if self.conectivo is None:
        
            # Devuelve el valor de la variable en la asignación
            return asignacion[posiciones[self.izquierda]]
        
        # Si es una negación
        elif self.conectivo == 'N':
        
            # Niega el valor de la subfórmula izquierda
            return 1 - self.izquierda._evalua_aux(asignacion, posiciones)
        
        # Si es una conjunción
        elif self.conectivo == 'C':
        
            # Devuelve la conjunción de las subfórmulas
            return self.izquierda._evalua_aux(asignacion, posiciones) and self.derecha._evalua_aux(asignacion, posiciones)
        
        # Si es una disyunción
        elif self.conectivo == 'D':
        
            # Devuelve la disyunción de las subfórmulas
            return self.izquierda._evalua_aux(asignacion, posiciones) or self.derecha._evalua_aux(asignacion, posiciones)
        
        # Si es una implicación
        elif self.conectivo == 'I':
        
            # Devuelve la implicación de las subfórmulas
            return (not self.izquierda._evalua_aux(asignacion, posiciones)) or self.derecha._evalua_aux(asignacion, posiciones)
        
        # Si es un bicondicional
        elif self.conectivo == 'E' or self.conectivo == 'B':
        
            # Devuelve el bicondicional de las subfórmulas
            izq = self.izquierda._evalua_aux(asignacion, posiciones)
            der = self.derecha._evalua_aux(asignacion, posiciones)
        
            return (not izq or der) and (not der or izq)

    # Devuelve el valor de verdad de la fórmula bajo una asignación dada.
    def evalua(self, asignacion: Asignacion):
      
        # Obtener la lista de variables en la fórmula
        variables = self.lista_variables()
        
        # Crear un diccionario para mapear cada variable a su posición en la asignación
        posiciones = {var: i for i, var in enumerate(variables)}
        
        # Evaluar la fórmula con la asignación dada
        return self._evalua_aux(asignacion, posiciones)

    # Devuleve una lista con la versión aplanada del árbol de sintáxis de la fórmula.
    def aplana(self):
       
        # Si es una variable
        if self.conectivo is None:
       
            return [self.izquierda]
        
        # Si es una negación
        elif self.conectivo == 'N':
       
            return [self.conectivo] + self.izquierda.aplana()
        
        # Si es un conectivo binario
        else:
           
            return [self.conectivo] + self.izquierda.aplana() + self.derecha.aplana()

    # Devuelve una lista con la versión aplanada del árbol de sintáxis de la fórmula, sin las hojas.
    def aplana_sin_variables(self):
      
        # Si es una variable
        if self.conectivo is None:
      
            return []
        
        # Si es una negación
        elif self.conectivo == 'N':
        
            return [self.conectivo] + self.izquierda.aplana_sin_variables()
        
        # Si es un conectivo binario
        else:
        
            return [self.conectivo] + self.izquierda.aplana_sin_variables() + self.derecha.aplana_sin_variables()