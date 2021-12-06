# Importa la función choice del módulo random
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
from random import choice

# Asigna a una lista las 3 posibles opciones: 'piedra', 'papel' o 'tijeras'. 
options = ['PIEDRA', 'PAPEL', 'TIJERAS']

# Asigna una variable al número de partidas máxima: 1, 3, 5, etc...
# games = 3

# Asigna una variable al número de partidas que debe ganar un jugador para ganar. 
# Preferiblemente el valor será en función de el número de partidas máximas
to_win = 3

# Define una función que devuelva aleatoriamente una de las 3 opciones. 
# Esto corresponderá a la jugada de la máquina. Totalmente aleatoria. 2
def cpu_choice():
    return choice(options)

# Define una función que pregunte tu elección: 'piedra', 'papel' o 'tijeras'
# sólo debe permitir una de las 3 opciones. Esto es programación defensiva. 
# Si no es piedra, papel o tijeras sigue preguntando hasta que lo sea. 
def user_choice():
    while True:
        symbol = input('Elige un simbolo (PIEDRA (1), PAPEL(2) o TIJERAS(3)): ')
        if symbol == '1': symbol = 'PIEDRA'
        if symbol == '2': symbol = 'PAPEL'
        if symbol == '3': symbol = 'TIJERAS'

        if symbol == 'PIEDRA' or symbol == 'PAPEL' or symbol == 'TIJERAS':
            return symbol
        else:
            print(f'¡{symbol} no es un simbolo valido!')

# Define una función que resuelva un combate. 
# Devuelve 0 si hay empate, 1 si gana la máquina, 2 si gana el jugador humano 
def match():
    user = user_choice()
    cpu = cpu_choice()
    if user == 'PIEDRA':
        if cpu == 'PIEDRA': game = 0
        elif cpu == 'PAPEL': game = 1
        elif cpu == 'TIJERAS': game = 2
    if user == 'PAPEL':
        if cpu == 'PAPEL': game = 0
        elif cpu == 'TIJERAS': game = 1
        elif cpu == 'PIEDRA': game = 2
    if user == 'TIJERAS':
        if cpu == 'TIJERAS': game = 0
        elif cpu == 'PIEDRA': game = 1
        elif cpu == 'PAPEL': game = 2
    return game, user, cpu

# Define una función que muestre la elección de cada jugador y el estado de la partida
# Esta función debe utilizarse cada vez que se actualicen los puntos acumulados
def status():
    global userGames, cpuGames
    game, user, cpu = match()
    if game == 0:
        print(f'¡Empate! {user} vs {cpu}')
    elif game == 1:
        print(f'La CPU gana con {cpu} vs {user}')
        cpuGames += 1
    elif game == 2:
        print(f'El jugador gana con {user} vs {cpu}')
        userGames += 1

# Crea dos variables que acumulen las partidas ganadas de cada participante
cpuGames = 0
userGames = 0

# Crea un bucle que itere mientras ningún jugador alcance el mínimo de victorias
# necesarias para ganar. Dentro del bucle resuelve la jugada de la
# máquina y pregunta la del jugador. Comparalas y actualiza el valor de las variables
# que acumulen las partidas ganadas de cada participante. 
while userGames < to_win and cpuGames < to_win:
    status()
    print(f'El resultado es: Player {userGames} - {cpuGames} CPU')
    print()
    
# Anuncia por consola el ganador del juego en función de quién tiene más victorias 
# aculumadas
if userGames < cpuGames:
    print('*** ¡La CPU gana! ***')
else:
    print('*** ¡El jugador gana! ***')