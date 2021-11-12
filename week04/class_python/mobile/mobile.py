
class Mobile():
    '''
    Clase mobile
    Francesco Esposito 05/11/2021
    '''
    def __init__(self, ram, display, price, camera, battery):
        self.ram = ram
        self.display = display
        self.price = price
        self.camera = camera
        self.battery = battery

    # Creamos metodos para configurar los atributos de la clase
    def set_ram(self, ram):
        self.ram = ram
    
    def set_display(self, display):
        self.display = display

    def set_price(self, price):
        self.price = price

    def set_camera(self, camera):
        self.camera = camera
    
    def set_battery(self, battery):
        self.battery = battery

    # Creamos metodos para recoger los atributos
    def get_ram(self):
        return self.ram  
    
    def get_display(self):
        return self.display 
    # Etc, etc, 

    def print_specs(self):
        print(f'Éstas son las caracteristicas del móvil:')
        print(f'Memoria RAM: {self.ram}GB')
        print(f'Pantalla: {self.display}"')
        print(f'Precio: {self.price}€')
        print(f'Cámara: {self.camera}mpx')
        print(f'Batería: {self.battery}mAh')

class Samsung(Mobile):
    # Inicializamos la clase Samsung
    def __init__(self, ram, display, price, camara, bateria, performance):
        Mobile.__init__(self, ram, display, price, camara, bateria)
        # inicializa la clase Mobile
        self.performance = performance

    def set_perfomance(self, performance):
        self.perfomance = performance

    def get_perfomance(self):
        return self.performance

class Apple(Mobile):
    def __init__(self, ram, display, price, camera, battery, ios):
        Mobile.__init__(self, ram, display, price, camera, battery)
        self.ios = ios
    
    def set_ios(self, ios):
        self.ios = ios
    
    def get_ios(self):
        return self.ios

iphone = Apple(8, 7.2, 690, 12, 2800, '13.1.5')
iphone.print_specs()
print(iphone.get_ram())