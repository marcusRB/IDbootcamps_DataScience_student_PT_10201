class Pet:
    def __init__(self, species, breed, sex, sound='', name='Sin nombre'):
        self.species = species
        self.breed = breed
        self.sex = sex
        self.sound = sound
        self.name = name
        
    def sonido(self):
        if self.species == 'perro':
            print(self.sound)
        elif self.species == 'gato':
            print(self.sound)
        else:
            print(f'Hago algo así: {self.sound}')

    def presentacion(self):
        print(f'Hola, mi nombre es {self.name} y soy un {self.species} de la raza {self.breed}')

class Dog(Pet):
    def __init__(self, breed, sex, name='Sin nombre'):
        Pet.__init__(self, 'perro', breed, sex, 'Guau, guau!', name)
   
    # def sonido(self):
    #     Pet.sonido(self)
    
    # def presentacion(self):
    #     print(f'Hola, mi nombre es {self.name} y soy un {self.species} de la raza {self.breed}')
        
class Cat(Pet):
    def __init__(self, breed, sex, name='Sin nombre'):
        Pet.__init__(self, 'gato', breed, sex, 'Meow!!', name)

    # def sonido(self):
        # Pet.sonido(self)
    
    # def presentacion(self):
    #     print(f'Hola, mi nombre es {self.name} y soy un {self.species} de la raza {self.breed}')
