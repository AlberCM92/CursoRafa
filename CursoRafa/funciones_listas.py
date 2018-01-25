# "piedra, papel o tijera" y "adivina el numero" con listas y funciones

import random

print("Juegos:\n", "1. Piedra, papel o tijera.\n", "2. Adivina el numero.");

seleccion_juego = input("¿A que juego quieres jugar? ")

def piedraPapelTijera():

	print("\nBienvenido a piedra, papel o tijera, esto es una partida al mejor de 3.")

	opciones = ["PIEDRA", "PAPEL", "TIJERA"]

	puntuacion_jugador = 0
	puntuacion_maquina = 0

	while abs(puntuacion_jugador - puntuacion_maquina) != 2:
		opcion_maquina = random.randint(0,2)
		opcion_jugador = input("¿Cual será tu arma? (piedra, papel o tijera): ")

		if opcion_jugador.upper() == opciones[0] or opcion_jugador.upper() == opciones[1] or opcion_jugador.upper() == opciones[2] or opcion_jugador.upper() == "TIJERAS":
			print("\nMaquina: ", opciones[opcion_maquina], " || Jugador: ", opcion_jugador.upper(), "\n")
		else:
			print("\nerror ", opcion_jugador.upper(), " no está en la lista.")
	
		if opcion_jugador.upper() == opciones[0]:
			if opcion_maquina == 0:
				print("Empate")
			elif opcion_maquina == 1:
				print("Pierdes")
				puntuacion_maquina += 1
			elif opcion_maquina == 2:
				print("Ganas")
				puntuacion_jugador += 1
		elif opcion_jugador.upper() == opciones[1]:
			if opcion_maquina == 0:
				print("Ganas")
				puntuacion_jugador += 1
			elif opcion_maquina == 1:
				print("Empate")
			elif opcion_maquina == 2:
				print("Pierdes")
				puntuacion_maquina += 1
		elif opcion_jugador.upper() == opciones[2] or opcion_jugador.upper() == "TIJERAS":
			if opcion_maquina == 0:
				print("Pierdes")
				puntuacion_maquina += 1
			elif opcion_maquina == 1:
				print("Ganas")
				puntuacion_jugador += 1
			elif opcion_maquina == 2:
				print("Empate")
		print("\nPuntuacion: Maquina -> ", puntuacion_maquina, "|| Jugador -> ", puntuacion_jugador, "\n")
		print("=============================================================")

	if puntuacion_jugador < puntuacion_maquina:
		print("\nHas perdido.")
	else:
		print("\nHas ganado!!!")
	print("\nFin de la partida.\n")


def adivinaNumero():
	numero_maquina = random.randint(1, 100)
	seguir = True
	contador = 0
	while contador > 9 or seguir == True:
		numero_jugador = int(input("Introduce un numero del 1 al 100: "))
		if numero_jugador == numero_maquina:
			print("¡Correcto! El numero era: ", numero_jugador, "\nFin de la partida.\n")
			seguir = False
		else:
			if numero_jugador < numero_maquina:
				print("Mas alto.")
			else:
				print("Mas bajo.")
			print("Intentalo de nuevo.\n")
			contador += 1

def seleccionaJuego(seleccion_juego):
	if int(seleccion_juego) == 1:
		piedraPapelTijera()
	elif int(seleccion_juego) == 2:
		adivinaNumero()


seleccionaJuego(seleccion_juego)