from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return False

elemento1 = Elemento( " Consola ")
elemento2 = Elemento( " Terminal ")
elemento3 = Elemento( " Consola ")

print(elemento1 == elemento2)  
print(elemento1 == elemento3)  
