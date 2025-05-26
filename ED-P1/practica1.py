'''
Casillas Álvarez Mauricio 
Munive Ramírez Ibrahim 
'''

import linkedList as linked

# EJERCICIO 1
def restar(n,k):

    for i in range(0, k):
    
        if (n % 10 != 0):
    
            n = n - 1
    
        else:
    
            n = n // 10
    
    return n

# EJERCICIO 2
def esPalindroma(s):
    string = s.lower() # Pasa la cadena de texto a minúsculas.
    string = string.replace(" ", "") # Elimina los espacios en blanco de la cadena de texto.
    
    x = len(string) - 1
    contador = 0

    for i in range(0, x):    

        if(string[i] == string[x - i]): 
            
            contador += 1
    
    if(contador == x):
            
        return True
    
    else:
            
        return False

# EJERCICIO 3
def promedioTuplas(tuplas):

    lista_promedios = []  
    
    for tupla in tuplas:
    
        suma = 0  
    
        cantidad = 0 
        
        for numero in tupla:  
    
            suma += numero 
    
            cantidad += 1 
        
        promedio = suma / cantidad  
    
        lista_promedios.append(promedio)  
    
    return lista_promedios

# EJERCICIO 4
def filtrarPares(positiveNumbers):
    pares = []
    
    for i in range (0, (len(positiveNumbers) - 1)):
    
        if (positiveNumbers[i] % 2 == 0):
    
            pares.append(positiveNumbers[i])

    return pares

# EJERCICIO 5
def dibujaTriangulo(n):
    
    resultado = []
    
    ancho_total = 2 * n - 1  

    for i in range(1, n + 1): 
    
        for j in range(1, i + 1): 
    
            espacios = (ancho_total - (2 * j - 1)) // 2  
    
            resultado.append(' ' * espacios + '* ' * j)
    
        resultado.append('\n')

    return '\n'.join(resultado)

# EJERCICIO 6
def permutaciones(nums):
    if(len(nums) == 0):
    
        return [[]] 
    
    resultado = []
    
    for i in range(0, len(nums)):
    
        resto = nums[:i] + nums[i+1:]
    
        for p in permutaciones(resto):
    
            resultado.append([nums[i]] + p)
    
    return resultado

# EJERCICIO 7
def sumaDigitos(n):

    while (n >= 10):
    
        n = sum(int(d) for d in str(n))
    
    return n

# EJERCICIO 8
def buscarCoincidencia(nums,n):

    contadorCoincidencias = 0

    for i in range(0, len(nums)):
        
        if (nums[i] == n):
            
            contadorCoincidencias += 1
        
    if (contadorCoincidencias > 0):

        return "T"

    else:

        return "F"

# Recuerda que dada una linked list s,
# el primer elemento es s.head, y 
# el sigueinte s.head.next, también,
# recuerda usar head.data.

# EJERCICIO 9

class Nodo:

    # Constructor
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def obtenerGises(linkedListGises):

    if (linkedListGises is None):
    
        return 0
    
    return (linkedListGises.valor + obtenerGises(linkedListGises.siguiente))

nodo1 = Nodo(4)
nodo2 = Nodo(10)
nodo3 = Nodo(2)

nodo1.siguiente = nodo2

nodo2.siguiente = nodo3