#Importamos librerias
import random

# Función para generar una carta aleatoria
def obtener_carta():
    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cartas)

# Función para calcular el valor de las cartas del jugador
def valor_carta(carta):
    if carta in ['J', 'Q', 'K']:
        return 10
    elif carta == 'A':
        return 11
    else:
        return int(carta)
    
# Función para calcular el valor total de las cartas del jugador
def valor_total(cartas):
    #Esta función convierte una carta a su valor numérico y los suma.
    total = sum(valor_carta(carta) for carta in cartas)
    # Ajustar el valor del as si el total es mayor a 21
    # num_as cuenta cuantos ases contienen las cartas, Si el total es 
    # mayor a 21 y hay ases disponibles para ajustar, el valor de cada as se reduce de 11 a 1.
    # Tambien en "total -= 10" reducimos el total en 10 por cada as que ajustamos.
    # Esto se debe a que cada as inicialmente cuenta como 11 y si se ajusta,
    # se cuenta como 1, lo que reduce el total en 10.
    # En "num_as -= 1:" disminuimos el contador de ases porque hemos ajustado uno
    num_as = cartas.count('A')
    while total > 21 and num_as > 0:
        total -= 10
        num_as -= 1
    return total

def main():
    # Creamos la lista en donde se iran guardando las cartas del jugador
    cartas_jugador = []

    #Se le da la bienvenida 
    print ("Hola, Bienvenid@ al BlackJack.jk")

    # Se inicia un ciclo que terminara cuando el jugador decida quedarse con sus cartas
    # o se supere la cantidad establecida (21)
    while True:

        # Se le empieza preguntando si desea mas cartas o gusta mantenerse con las que ya tiene
        decision = input("¿Quieres pedir una carta (p) o te mantienes (m)? ").strip().lower()

        # Si decide pedir una carta
        # se llama a la funcion "Obtener_cartas" para que le genera al jugador una carta
        # Con "Cartas_jugador.append" la carta obtenida se añade a la lista de cartas del jugador.
        # Se calcula el valor total de las cartas con la función "valor_total(cartas_jugador)"
        # se muestra el valor total actual al jugador al igual que la carta que obtuvo
        if decision == 'p':
            carta = obtener_carta()
            cartas_jugador.append(carta)
            total_jugador = valor_total(cartas_jugador)
            print(f"Has recibido una {carta}. Tu total actual es {total_jugador}.")

            # Se comprueba despues de esto si el jugador a perdido
            # Si es asi el ciclo se cierra y se le devuelve un mensaje de derrota.
            if total_jugador > 21:
                print("Te has pasado de 21. ¡Has perdido!")
                print("Gracias por jugar a BlackJack.Jk")
                return
        
        #Por el contrario si el usuario decide mantenerse el ciclo se cierra automaticamente
        elif decision == 'm':
             break
        
        #Si el jugador ingresa algo distinto a 'p' o 'm', el programa muestra un mensaje de error 
        # y vuelve a pedir la decisión.
        else:
          print("Opción no válida. Por favor elige 'p' para pedir una carta o 'm' para mantenerte.")

    valor_casa = random.randint(17, 26)
    total_jugador = valor_total(cartas_jugador)
    print(f"\nTus cartas: {cartas_jugador} con un total de {total_jugador}.")
    print(f"El total de la casa es: {valor_casa}.")
    
    # Determinamos el resultado
    #Condiciones para ganar:
    #   El jugador tiene exactamente 21 y la casa tiene menos de 21.
    #   La casa se pasa de 21 y el jugador no.
    #   El jugador tiene un total menor o igual a 21 y mayor que el de la casa.
    #   El jugador y la casa tienen el mismo total, pero el jugador lo ha hecho con menos cartas (máximo 5).

    if (total_jugador == 21 and valor_casa < 21) or \
       (valor_casa > 21 and total_jugador <= 21) or \
       (total_jugador <= 21 and valor_casa <= 21 and total_jugador > valor_casa) or \
       (total_jugador <= 21 and valor_casa <= 21 and total_jugador == valor_casa and len(cartas_jugador) < 5):
        print("¡Has ganado!")

    #Condiciones para un empate:
    #   Ambos se pasan de 21.
    #A  mbos tienen el mismo valor y el jugador ha usado exactamente 5 cartas.
    elif (total_jugador > 21 and valor_casa > 21) or \
         (total_jugador <= 21 and valor_casa <= 21 and total_jugador == valor_casa and len(cartas_jugador) == 5):
        print("Es un empate.")
    
    #En cualquier otro caso, el jugador pierde.
    else:
        print("¡Has perdido!")

#Esta línea ejecuta el juego si el archivo se ejecuta directamente. 
#Llama a la función main() para iniciar el juego.
if __name__ == "__main__":
    main()
