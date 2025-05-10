"""
Munive Ramírez Ibrahim
cuenta: 424106083
García Rubio Asteinza Ana Sofía (no hizo nada)
cuenta: 3231 
"""

"""
Clase para representar árboles binarios recursivos. La variable 'raiz' es un
elemento, 'izquierdo' es un árbol y 'derecho' es un árbol.
"""
class Arbol:

    def __init__(self, raiz = None, izquierdo = None, derecho = None):

        if raiz is None:
            
            self.raiz = self.izquierdo = self.derecho = None
        
        else:
        
            self.raiz = raiz
        
            if izquierdo is None:
        
                self.izquierdo = Arbol()
        
            elif not isinstance(izquierdo, Arbol):
        
                raise TypeError("¡El subárbol izquierdo debe ser árbol!")
        
            else:
        
                self.izquierdo = izquierdo
        
            if derecho is None:
        
                self.derecho = Arbol()
        
            elif not isinstance(derecho, Arbol):
        
                    raise TypeError("¡El subárbol derecho debe ser árbol!")
        
            else:
        
                self.derecho = derecho

    # 1. Represenración en cadena (legible para humanos) de un árbol. 
    def __repr__(self):
        
        if self.es_vacio():
            
            return "∅"
        
        elif self.es_hoja():
        
            return str(self.raiz)
        
        else:
        
            return f"({self.raiz}, {self.izquierdo}, {self.derecho})"

    # 2. Comprueba si un árbol es vacío. 
    def es_vacio(self):

        return self.raiz is None

    # 3. Comprueba si un árbol tiene un único nodo. 
    def es_hoja(self):

        return not self.es_vacio() and self.izquierdo.es_vacio() and self.derecho.es_vacio()

    # 4. Devuelve un árbol idéntico al original.
    def copia(self):

        if self.es_vacio():
 
            return Arbol()
 
        else:
 
            return Arbol(self.raiz, self.izquierdo.copia(), self.derecho.copia())

    # 5. Devuelve el número de nodos en el árbol.
    def num_nodos(self):

        if self.es_vacio():

            return 0

        else:

            return 1 + self.izquierdo.num_nodos() + self.derecho.num_nodos()

    # 6. Si elemento se encuentra en el árbol, devuelve cadena con la dirección el primer nodo del árbol que contenga al elemento.
    def direccion(self, elemento):

        if self.es_vacio():

            return False
        
        if self.raiz == elemento:

            return ""
        
        # Busca en el subárbol izquierdo
        dirIzq = self.izquierdo.direccion(elemento)

        if dirIzq is not False:

            return "0" + dirIzq
        
        # Busca en el subárbol derecho
        dirDer = self.derecho.direccion(elemento)

        if dirDer is not False:

            return "1" + dirDer
        
        return False

    # 7. Gira el subárbol que tiene como raíz al nodo con la dirección dada.
    def gira(self, direccion):
        
        # Si la dirección no corresponde a un nodo del árbol, se devuelve una copia del árbol original.
        
        if self.es_vacio():

            return Arbol()
        
        # Si la dirección está vacía, girar este nodo

        if direccion == "":
        
            return Arbol(self.raiz, self.derecho.copia(), self.izquierdo.copia())
        
        # Si la dirección comienza con 0, seguir por la izquierda
        
        if direccion[0] == "0" and not self.izquierdo.es_vacio():
        
            return Arbol(self.raiz, self.izquierdo.gira(direccion[1:]), self.derecho.copia())
        
        # Si la dirección comienza con 1, seguir por la derecha
        
        if direccion[0] == "1" and not self.derecho.es_vacio():
        
            return Arbol(self.raiz, self.izquierdo.copia(), self.derecho.gira(direccion[1:]))
        
        # Si la dirección no corresponde a un nodo, devolver copia del árbol
        return self.copia()

    # 8. Comprueba que dos árboles sean isomorfos.
    def es_isomorfo(self, arbol):

        # Dos árboles vacíos son isomorfos
        if self.es_vacio() and arbol.es_vacio():

            return True
        
        # Si uno es vacío y el otro no, no son isomorfos
        if self.es_vacio() or arbol.es_vacio():

            return False
        
        # Verificar isomorfismo directo
        isomorfoDirecto = (self.izquierdo.es_isomorfo(arbol.izquierdo) and self.derecho.es_isomorfo(arbol.derecho))
        
        # Verificar isomorfismo cruzado
        isomorfoCruzado = (self.izquierdo.es_isomorfo(arbol.derecho) and self.derecho.es_isomorfo(arbol.izquierdo))
        
        return isomorfoDirecto or isomorfoCruzado

    # 9. Busca el ancestro común más cercano a dos elementos.
    def lca(self, elemento1, elemento2):

        # Si el árbol está vacío, no hay ancestro común
        if self.es_vacio():

            return False
        
        # Si la raíz es uno de los elementos, la raíz es el ancestro común
        if self.raiz == elemento1 or self.raiz == elemento2:
         
            return ""
        
        # Buscar direcciones de los elementos
        dir1 = self.direccion(elemento1)
        dir2 = self.direccion(elemento2)
        
        # Si alguno de los elementos no está en el árbol, no hay ancestro común
        if dir1 is False or dir2 is False:
            
            return False
        
        # Encontrar el prefijo común más largo
        prefijoComun = ""

        for i in range(min(len(dir1), len(dir2))):

            if dir1[i] == dir2[i]:
            
                prefijoComun += dir1[i]
            
            else:
            
                break
        
        return prefijoComun

    """
    Método para comparar árboles (no pasan las prubeas unitarias de giro y copia sin este método)
    La verdad, la verdad, no le veo algo mal a los métodos para que no pasen las pruebas unitarias,
    pero esto lo soluciona. Este método compara los árboles de forma recursiva, y si los dos árboles 
    son iguales, entonces manda True.   
    """
    def __eq__(self, otro):

        if not isinstance(otro, Arbol):
            
            return False
        
        # Si ambos son vacios, entonces son iguales
        if self.es_vacio() and otro.es_vacio():
            
            return True
        
        # Si uno es vacío y el otro no, no son iguales
        if self.es_vacio() or otro.es_vacio():

            return False
        
        # Comparar raíces y subárboles
        return (self.raiz == otro.raiz and self.izquierdo == otro.izquierdo and self.derecho == otro.derecho)