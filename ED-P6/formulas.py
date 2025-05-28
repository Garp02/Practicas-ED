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

        conectivos=['C','D','I','E','N']

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


    # Devuelve el renglón con esa asignación de la tabla de verdad.
    def evalua_sub(self, asignacion: Asignacion) -> List[bool]:
    
        valores = []

        # Función recursiva que evalúa la fórmula y devuelve el valor de verdad
        def evalua(f):
            
            if f.conectivo is None:
            
                valor = asignacion[f.izquierda - 1]
                valores.append(valor)
            
                return valor
            
            elif f.conectivo == 'N':
            
                izq = evalua(f.izquierda)
                valor = not izq
                valores.append(valor)
            
                return valor
            
            else:

                izq = evalua(f.izquierda)
                der = evalua(f.derecha)

                if f.conectivo == 'C':
                
                    valor = izq and der
                
                elif f.conectivo == 'D':
                
                    valor = izq or der
                
                elif f.conectivo == 'I':
                
                    valor = (not izq) or der
                
                elif f.conectivo == 'E':
                
                    valor = izq == der
                
                valores.append(valor)
                
                return valor

        evalua(self)
        return valores

    # Devuelve una lista de listas correspondientes a la tabla de verdad
    def renglones_verdad(self) -> List[List[int]]:
    
        def cuenta_variables(f):
            
            if f.conectivo is None:
            
                return {f.izquierda}
            
            elif f.conectivo == 'N':
            
                return cuenta_variables(f.izquierda)
            
            else:
            
                return cuenta_variables(f.izquierda).union(cuenta_variables(f.derecha))

        variables = sorted(list(cuenta_variables(self)))
        n = len(variables)
        
        combinaciones = list(product([0, 1], repeat=n))

        # Encabezado: x1, x2, ..., fórmula compuesta
        encabezado = ['x' + str(i) for i in variables]
        subvalores = self.evalua_sub([0] * n)
        encabezado += ['x' + str(i + 1 + max(variables)) for i in range(len(subvalores) - n)]

        tabla = [encabezado]
        
        for c in combinaciones:
        
            resultado = self.evalua_sub(list(c))
            fila = list(c) + resultado[n:]
            tabla.append(fila)

        return tabla

    # Devuelve una cadena que indica si la fórmula es taulogía, contingencia o contradicción.
    def tipo_formula(self) -> str:
        
        tabla = self.renglones_verdad()
        resultados = [fila[-1] for fila in tabla[1:]]
        
        if all(resultados):
        
            return 'T'  # Tautología
        
        elif not any(resultados):
        
            return 'C'  # Contradicción
        
        else:
        
            return 'N'  # La otra cosa de nombre raro.



    # Crea un archivo .tex que contiene un documento de LaTex con la tabla de verdad en LaTex.
    def LaTex(self):

        tabla = self.renglones_verdad()
        with open(nombre + ".tex", "w") as f:
            
            f.write("\\documentclass{article}\n\\begin{document}\n\n")
            f.write("\\begin{center}\n\\begin{tabular}{|" + "c|" * len(tabla[0]) + "}\n\\hline\n")
            
            encabezado = " & ".join(tabla[0]) + " \\\\\n\\hline\n"
            f.write(encabezado)
            
            for fila in tabla[1:]:
            
                linea = " & ".join(str(e) for e in fila) + " \\\\\n"
                f.write(linea)
            
            f.write("\\hline\n\\end{tabular}\n\\end{center}\n\n\\end{document}")
