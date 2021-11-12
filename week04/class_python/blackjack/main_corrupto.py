import blackjack

barajas = blackjack.Deck()
barajas.shuffle()
# nombre = input('Bienvenido al juego del BlackJack. ?Como te llamas? ')

# Juega el jugador
jugador = blackjack.Player()
jugador.take_card(barajas.draw())
while True:
    print(f'Tu mano es: {jugador.hand}')
    if jugador.hit():
        jugador.take_card(barajas.draw())
    else:
        break
totJugador = sum(jugador.hand)
if totJugador > 21:
    print(f'Tu puntuación es: {totJugador}')
    print('Te has pasado, has perdido')
else:
    print(f'Tu puntuación es: {totJugador}')

# Juega la cpu
cpu = blackjack.Player('CPU')
cpu.take_card(barajas.draw())
while True:
    if sum(cpu.hand) < 15:
        cpu.take_card(barajas.draw()
    elif sum(cpu.hand) > 21:
        print('La CPU se ha pasado, ¡Has ganado!')
        break
    else:
        totCpu = sum(cpu.hand)
        print(f'La mano de la CPU es: {totCpu}')





