Blackjack.JK - Juego de BlackJack en Python

Institución:
[Instiucion superiores palmore]

Materia:
[Programacion 2]

Fecha:
[16/09/2024]

Descripción del proyecto:
Este programa consiste en un juego de Blackjack que se ejecuta en la terminal. El jugador puede pedir cartas o mantenerse, con el objetivo de obtener un valor total lo más cercano a 21 sin pasarse. El juego sigue las reglas básicas del Blackjack, donde las cartas con figuras (J, Q, K) valen 10, los ases pueden valer 11 o 1 dependiendo de la situación, y las demás cartas tienen su valor numérico.

Instrucciones:
Al iniciar el programa, el jugador será recibido con un mensaje de bienvenida y se le ofrecerá la opción de pedir una carta (p) o mantenerse con sus cartas actuales (m).

Si el jugador elige pedir una carta, se genera una carta aleatoria y se añade a la mano del jugador. El valor total de sus cartas se calcula y se muestra en pantalla. Si el total supera 21, el jugador pierde automáticamente.

Si el jugador decide mantenerse, se comparan las cartas del jugador con las de la casa (la cual tiene un valor generado aleatoriamente entre 17 y 26).

Condiciones de victoria:
El jugador tiene exactamente 21 y la casa tiene menos de 21.
La casa se pasa de 21 y el jugador no.
El jugador tiene un total menor o igual a 21 y mayor que el de la casa.
El jugador y la casa tienen el mismo total, pero el jugador lo ha hecho con menos cartas (máximo 5).


Condiciones de empate:
Ambos se pasan de 21.
Ambos tienen el mismo valor y el jugador ha usado exactamente 5 cartas.
Si ninguna de las condiciones de victoria o empate se cumple, el jugador pierde.

Descripción de cada parte del código:
Librerías:
El código usa la librería random para generar cartas de forma aleatoria y el valor de la casa.

Función obtener_carta():
Genera una carta aleatoria de la baraja de cartas estándar de Blackjack (2-10, J, Q, K, A).

Función valor_carta(carta):
Asigna el valor correspondiente a cada carta. Las figuras valen 10, el as puede valer 11 o 1, y las cartas numéricas tienen su valor.

Función valor_total(cartas):
Calcula el valor total de la mano del jugador, ajustando los ases de 11 a 1 si es necesario para evitar que el total supere 21.

Función main():
Es la función principal que controla el flujo del juego:

Pregunta al jugador si quiere pedir una carta o mantenerse.
Gestiona las cartas del jugador y la lógica del juego.
Al finalizar, compara el valor de las cartas del jugador con las de la casa y determina el resultado (victoria, empate o derrota).

Ejemplo de ejecución en la terminal:
Hola, Bienvenid@ al BlackJack.jk
¿Quieres pedir una carta (p) o te mantienes (m)? p
Has recibido una 7. Tu total actual es 7.
¿Quieres pedir una carta (p) o te mantienes (m)? p
Has recibido una K. Tu total actual es 17.
¿Quieres pedir una carta (p) o te mantienes (m)? m

Tus cartas: ['7', 'K'] con un total de 17.
El total de la casa es: 20.

¡Has perdido!
Gracias por jugar a BlackJack.Jk

Nombre:
[B.A. Guigon Palacios]




