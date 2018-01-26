# "piedra, papel o tijera" y "adivina el numero" con listas y funciones

import random

seleccionar = True

def piedraPapelTijera():

	print("\nBienvenido a piedra, papel o tijera, esto es una partida al mejor de 3.")

	opcionesPPC = ["PIEDRA", "PAPEL", "TIJERA"]

	puntuacion_jugador = 0
	puntuacion_maquina = 0

	while abs(puntuacion_jugador - puntuacion_maquina) != 2:
		opcion_maquina = random.randint(0,2)
		opcion_jugador = input("¿Cual será tu arma? (piedra, papel o tijera): ")

		if opcion_jugador.upper() == opcionesPPC[0] or opcion_jugador.upper() == opcionesPPC[1] or opcion_jugador.upper() == opcionesPPC[2] or opcion_jugador.upper() == "TIJERAS":
			print("\nMaquina: ", opcionesPPC[opcion_maquina], " || Jugador: ", opcion_jugador.upper(), "\n")
		else:
			print("\nerror ", opcion_jugador.upper(), " no está en la lista.")
	
		if opcion_jugador.upper() == opcionesPPC[0]:
			if opcion_maquina == 0:
				print("Empate")
			elif opcion_maquina == 1:
				print("Pierdes")
				puntuacion_maquina += 1
			elif opcion_maquina == 2:
				print("Ganas")
				puntuacion_jugador += 1
		elif opcion_jugador.upper() == opcionesPPC[1]:
			if opcion_maquina == 0:
				print("Ganas")
				puntuacion_jugador += 1
			elif opcion_maquina == 1:
				print("Empate")
			elif opcion_maquina == 2:
				print("Pierdes")
				puntuacion_maquina += 1
		elif opcion_jugador.upper() == opcionesPPC[2] or opcion_jugador.upper() == "TIJERAS":
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
		numero_jugador = input("Introduce un numero del 1 al 100: ")

		try:
			if int(numero_jugador) == numero_maquina:
				print("¡Correcto! El numero era: ", numero_jugador, "\nFin de la partida.")
				seguir = False
			else:
				if int(numero_jugador) < numero_maquina:
					print("Mas alto.")
				else:
					print("Mas bajo.")
				print("Intentalo de nuevo.\n")
				contador += 1
		except ValueError:
			print("Eso no es un numero. Vuelve a intentarlo.")

def seleccionaJuego(seleccion_juego):
	if int(seleccion_juego) == 1:
		piedraPapelTijera()
	elif int(seleccion_juego) == 2:
		adivinaNumero()
	elif int(seleccion_juego) == 3:
		print("Hasta pronto!")
		return

while seleccionar == True:
	print("Juegos:\n", "1. Piedra, papel o tijera.\n", "2. Adivina el numero.\n", "3. Salir");
	seleccion_juego = input("¿A que juego quieres jugar? ")
	if int(seleccion_juego) < 3:
		seleccionaJuego(seleccion_juego)
	elif int(seleccion_juego) > 3:
		print("Ese juego no existe. Selecciona un juego.")
	elif int(seleccion_juego) == 3:
		print("Hasta pronto.")
		seleccionar = False