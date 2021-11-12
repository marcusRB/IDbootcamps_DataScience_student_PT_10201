import pets

def main():
    bobby = pets.Dog('labrador', 'male', 'Bobby')
    bobby.presentacion()
    bobby.sonido()
    print()
    principessa = pets.Cat('europeo', 'female', 'Principessa')
    principessa.presentacion()
    principessa.sonido()
    print()
    kra = pets.Pet('sapo', 'comun', 'male', 'Croac, croac', 'Kra')
    kra.presentacion()
    kra.sonido()

main()