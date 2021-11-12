# Importo las librerias
import random

# Creamos el objeto Class
class Card:
    '''
    Costruimos las semillas y los valores de las cartas
    '''

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        vals = {'J':10, 'Q':10, 'K':10, 'A':11}
        # Hay que definir el valor a cada una de las cartas
        self.actual_value = value if isinstance(value, int) else vals[value]
    
    def __repr__(self):
        '''
        Creamos un método que defina la representación misma de las cartas,
        que tomará el calculo de los valores de las cartas.
        '''
        return f"{str(self.value).rjust(3,' ')}{self.suit}"
    
    def __add__(self, other):
        return self.actual_value + other

    def __radd__(self, other):
        return self.actual_value + other

class Deck:
    # Inizializamos Deck
    def __init__(self):
        # Creamos la combinación de las 52 cartas por semilla y color
        self.cards = []
        for suit in ["♠","♥","♦","♣"]:
            # por cada valor en las 4 semillas generamos el objeto Carta
            for value in ['A'] + list(range(2, 11)) + ['J', 'Q', 'K']:
                self.cards.append(Card(value, suit))
    
    # Creamos el método de mezclar las cartas
    def shuffle(self):
        random.shuffle(self.cards)

    # Creamos el método para controlar el listado de cartas remanentes
    def draw(self):
        if self.cards:
            return self.cards.pop(0) # con pop(0) estamos eliminando siempre la primera carta
        else:
            return 'No hay más cartas'

# Creamos la clase Player
class Player:
    # inicializamos 
    def __init__(self, name="Player1"):
        self.name = name
        self.hand = []
        
    # definimos el método de coger una carta
    def take_card(self, card):
        self.hand.append(card)
    
    # definimos el método de preguntar si necesita otra carta
    def hit(self):
        hit = input(f"{self.name}, quieres otra carta? [y|n] ")
        if hit.lower() == 'y':
            return True
        elif hit.lower() == 'n':
            return False
        else:
            print("Te has equivocado, contesta y|n")
            return self.hit()
        
    def __repr__(self):
        return self.name

# cartas = Deck()
# print(len(cartas.cards))
# print(cartas.cards[10:20])
# random.shuffle(cartas)

# deck = Deck()
# deck.shuffle()
# jugador = Player()

# if jugador.hit():
#     jugador.take_card(deck.draw())

# print(jugador.hand)

# if jugador.hit():
#     jugador.take_card(deck.draw())

# print(jugador.hand)
# print(deck.cards)