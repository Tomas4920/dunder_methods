class Elemento:
    def __init__(self, nombre):
        self.nombre = nombre

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.lista_elementos = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        if isinstance(elemento, Elemento):
            return any(e.nombre == elemento.nombre for e in self.lista_elementos)
        return False

    def agregar_elemento(self, elemento):
        if isinstance(elemento, Elemento):
            if not self.contiene(elemento):
                self.lista_elementos.append(elemento)
            else:
                print(f" {elemento.nombre} ya está en el conjunto. " )

    def unir(self, otro_conjunto):
        if isinstance(otro_conjunto, Conjunto):
            for elemento in otro_conjunto.lista_elementos:
                self.agregar_elemento(elemento)
        else:
            print( " No es objeto de la clase Conjunto " )

    def __add__(self, otro_conjunto):
        resultado = Conjunto(f" {self.nombre} Unido {otro_conjunto.nombre} " )
        resultado.unir(self)
        resultado.unir(otro_conjunto)
        return resultado

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        if isinstance(conjunto1, Conjunto) and isinstance(conjunto2, Conjunto):
            elementos_interseccion = [e for e in conjunto1.lista_elementos if conjunto2.contiene(e)]
            nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
            resultado = Conjunto(nombre_resultado)
            resultado.lista_elementos = elementos_interseccion
            return resultado
        else:
            print( " No son objetos de la clase Conjunto ")

    def __str__(self):
        elementos = ", ".join([elem.nombre for elem in self.lista_elementos])
        return f"Conjunto {self.nombre}: ({elementos})"

elemento1 = Elemento( " Consola " )
elemento2 = Elemento( " Terminal ")
elemento3 = Elemento( " Programa " )

conjunto1 = Conjunto( " Componentes de programación ")
conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)

conjunto2 = Conjunto( " Programación " )
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

print(conjunto1) 
print(conjunto2) 

print(conjunto1.contiene(elemento1))  
print(conjunto1.contiene(elemento3))  

conjunto1.agregar_elemento(elemento3)  
print(conjunto1) 

conjunto_union = conjunto1 + conjunto2
print(conjunto_union) 

conjunto_interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print(conjunto_interseccion) 
