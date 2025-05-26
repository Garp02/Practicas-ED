"""
García Rubio Asteinza Ana Sofía
Cuenta: 320555840
Munive Ramírez Ibrahim
Cuenta: 424106083
"""

from typing import List

class Lista:
    
    # Método constructor
    def __init__(self, elementos = None):

        if elementos != None:

            if not isinstance(elementos, List):
            
                raise TypeError("Debe recibir una lista de elementos")
            
            elif len(elementos) == 1:
            
                self.cabeza = elementos[0]
                self.cola = Lista()
            
            else:
            
                self.cabeza = elementos[0]
                self.cola = Lista(elementos[1:])
        
        else:
        
            self.cabeza = None
            self.cola = None
    
    # 1. Representación en cadena (legible para humanos) de las listas.
    def __repr__(self):
        
        # Caso base: lista vacía
        if self.cabeza is None:

            return "()"
        
        else:
            
            return "({0} {1})".format(self.cabeza, repr(self.cola))

    # 2. Agrega un elmento al principio de la lista.
    def agrega_principio(self, elemento):

        # Caso base
        if self.cabeza is None:
        
            self.cabeza = elemento
            self.cola = Lista()
        
        else:
            
            # Se crea un nodo y se agrega al principio de la lista
            nodoAuxiliar = self.cabeza
            self.cabeza = elemento
            self.cola.agrega_principio(nodoAuxiliar)
            colaAuxiliar = self.cola.cola
            self.cola = Lista()
            self.cola.cabeza = nodoAuxiliar
            self.cola.cola = colaAuxiliar

    # 3. Agrega un elemento al final de la lista.
    def agrega_final(self,elemento):

        # Caso base
        if self.cabeza is None:
            
            self.cabeza = elemento
            self.cola = Lista()
        
        else:

            self.cola.agrega_final(elemento)

    # 4. Devuelve el número de elementos en la lista.
    def longitud(self):

        if self.cabeza is None:
            
            return 0

        else:
            
            return 1 + self.cola.longitud()
        
    # 5. Devuelve si el elemento se encuentra en la lista.
    def contiene(self,elemento):

        if self.cabeza is None:

            return False
        
        elif self.cabeza == elemento:
        
            return True
        
        else:
        
            return self.cola.contiene(elemento)
        
    # 6. Crea una nueva lista idéntica a esta.
    def copia(self):

        if self.cabeza is None:

            return Lista()

        else:

            nueva_lista = Lista()
            nueva_lista.cabeza = self.cabeza
            nueva_lista.cola = self.cola.copia()

            return nueva_lista

    # 7. Concatena la lista actual con la lista recibida como argumento.
    def concatena(self, lista):

        resultado = self.copia()

        if lista.cabeza is None:

            return resultado

        elif resultado.cabeza is None:

            return lista.copia()

        else:

            temp = resultado

            while temp.cola.cabeza is not None:

                temp = temp.cola

            temp.cola = lista.copia()

            return resultado

    # 8. Regresa una lista con los elementos en orden invertido a la original.
    def reversa(self):

        if self.cabeza is None:

            return Lista()
        
        else:
        
            resultado = self.cola.reversa()
            resultado_temp = resultado
        
            if resultado_temp.cabeza is None:
        
                resultado_temp.cabeza = self.cabeza
                resultado_temp.cola = Lista()
        
            else:
        
                while resultado_temp.cola.cabeza is not None:
        
                    resultado_temp = resultado_temp.cola
        
                resultado_temp.cola.cabeza = self.cabeza
                resultado_temp.cola.cola = Lista()
        
            return resultado
        
    # 9. Devuelve la lista resultante de aplicar una función f sobre los elementos de la lista.
    def mapea(self,f):

        if self.cabeza is None:

            return Lista()

        else:

            resultado = Lista()
            resultado.cabeza = f(self.cabeza)
            resultado.cola = self.cola.mapea(f)

            return resultado
        
    # 10. Devuelve la lista resultante de seleccionar los elementos que cumplan con la condición f.
    def filtra(self,f):

        if self.cabeza is None:

            return Lista()

        else:

            resultado = self.cola.filtra(f)

            if f(self.cabeza):

                nueva_lista = Lista()
                nueva_lista.cabeza = self.cabeza
                nueva_lista.cola = resultado

                return nueva_lista

            else:

                return resultado
        
    # Compara dos listas y devuelve si son iguales.
    def __eq__(self, lista):

        if not isinstance(lista, Lista):

            return False

        if self.cabeza is None and lista.cabeza is None:

            return True

        elif self.cabeza is None or lista.cabeza is None:
            
            return False
        
        else:
        
            return self.cabeza == lista.cabeza and self.cola == lista.cola


# Ejemplos
"""
lista1 = Lista([1, 2, 3, 4, 5])
lista2 = Lista([6, 7, 8])
listaVacia = Lista()

# 1. Representación en cadena (legible para humanos) de las listas.
print("\nRepresentación de lista: ")
print(lista1) 

# 2. Agrega un elmento al principio de la lista.
print("\nAgregar un elemento al principio:")
lista1.agrega_principio(0)
print(lista1) 

# 3. Agrega un elemento al final de la lista.
print("\nAgrega un elemento al final: ")
lista1.agrega_final(6)
print(lista1)

# 4. Devuelve el número de elementos en la lista.
print("\nLongitud de la lista:")
print(lista1.longitud())

# 5. Devuelve si el elemento se encuentra en la lista.
print("\nContiene un elemento: ")
print(lista1.contiene(3))  

# 6. Copiar lista
print("\nCopia:")
listaCopia = lista1.copia()
print(listaCopia)

# 7. Concatena la lista actual con la lista recibida como argumento.
print("\nConcatenar lista:")
listaConcatenada = lista1.concatena(lista2)
print(listaConcatenada)  

# 8. Regresa una lista con los elementos en orden invertido a la original.
print("\nReversa de la lista:")
listaInvertida = lista1.reversa()
print(listaInvertida)

# 9. Devuelve la lista resultante de aplicar una función f sobre los elementos de la lista.
print("\nMapeo de lista: ")
listaDoble = lista1.mapea(lambda x: x * 2)
print(listaDoble)

# 10. Devuelve la lista resultante de seleccionar los elementos que cumplan con la condición f.
print("\nFiltrar lista:")
listaFiltrada = lista1.filtra(lambda x: x % 2 == 0)
print(listaFiltrada)
"""