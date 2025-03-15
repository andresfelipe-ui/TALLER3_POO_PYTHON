# ****ZONA DE CLASE*****
#se crea la clase
class cliente:
    #se crea el metodo constructo de la clase
    def __int__(self):
        #se crean los atributos de la clase
        self.nombre_cliente = ""
        self.apellido_cliente = ""
        
    #crear metodos get y set por atributos
    def get_nombre(self):
        return self.nombre_cliente
    
    def get_apellido(self):
        return self.apellido_cliente
    
    def set_nombre(self, dato_nombre):
        self.nombre_cliente = dato_nombre
        
    def set_apellido(self, dato_apellido):
        self.apellido_cliente = dato_apellido
        
            
    # se crean metodos normales de la clase
    
    def tomar_datos(self):
        self.nombre_cliente = input("digite el nombre  : ")
        self.apellido_cliente = input("digite el apellido : ")
    
    
    def procesar_datos(self):
        aux = self.nombre_cliente + " " + self.apellido_cliente
    
    def mostrar_info_cliente(self):
        print(f"nombre cliente: {self.nombre_cliente} - apellido cliente: {self.apellido_cliente}")
        