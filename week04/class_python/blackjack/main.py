import blackjack
end = False
# Creamos la baraja y la mezclamos
barajas = blackjack.Deck()
barajas.shuffle()

# Creamos los jugadores
nombre = input('Bienvenido al juego del BlackJack. ¿Como te llamas? ')
if nombre != '':
    jugador = blackjack.Player(nombre)
else:
    jugador = blackjack.Player()
cpu = blackjack.Player('CPU')

# Distribuimos dos cartas cada uno
jugador.take_card(barajas.draw())
jugador.take_card(barajas.draw())
cpu.take_card(barajas.draw())
cpu.take_card(barajas.draw())

# Juega el jugador
while True:
    print(f'Tu mano es: {jugador.hand}')
    if sum(jugador.hand) > 21:
        print('Te has pasado. ¡Has perdido!')
        end = True
        break
    if jugador.hit():
        jugador.take_card(barajas.draw())
    else:
        totJugador = sum(jugador.hand)
        print(f'Tu puntuación es: {totJugador}')
        break

# Juega la CPU
if end == False:
    while True:
        if sum(cpu.hand) < 17:
            cpu.take_card(barajas.draw())
        elif sum(cpu.hand) > 21:
            print(f'La puntación de la CPU es: {sum(cpu.hand)}')
            print('La CPU se ha pasado. ¡Has ganado!')
            end = True
            break
        else:
            totCpu = sum(cpu.hand)
            print(f'La puntación de la CPU es: {totCpu}')
            break

# Se comparan las puntuaciones
if end == False:
    if totJugador > totCpu:
        print('¡Has ganado!')
    elif totJugador < totCpu:
        print('¡Has perdido!')
    else:
        print('Empate')