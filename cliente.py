from abc import ABC, abstractmethod from datetime import datetime 
class SerVivo(ABC): def init(self, nombre: str, edad: int): self._nombre = nombre self._edad = 
edad 
@abstractmethod 
def alimentar(self): 
    pass 
 
def get_nombre(self): 
    return self._nombre 
 
def get_edad(self): 
    return self._edad 
