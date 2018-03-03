def main():
	print(" Bienvenido a esta nueva aventura.\n")
	nombre = input(" Dime, ¿Cómo te llamas? ")
	exp = 6000
	nivel = int((1+(exp/1000))//1)
	turno = 0

	dir_opciones = ["NORTE", "SUR", "ESTE", "OESTE"]

	def movimiento(direccion, turno):

		while True:
			direccion = input(" Primero, elije hacia donde quieres ir (norte, sur, este, oeste): ")
			if any(item == direccion.upper() for item in dir_opciones):
				turno += 1
				if direccion.upper() == dir_opciones[0]:
					norte(turno)
				elif direccion.upper() == dir_opciones[1]:
					sur(turno)
				elif direccion.upper() == dir_opciones[2]:
					este(turno)
				elif direccion.upper() == dir_opciones[3]:
					oeste(turno)
			else:
				print("\nTienes que decirme una dirección valida.")


	def norte(turno):
		if turno == 1:
			print("[Camino cortado, vuelves al cruce anterior]")
			turno -= 1
		else:
			return
		movimiento("", turno)

	def sur(turno):
		if turno == 1:
			input("[Ves dos caminos, uno al este y otro al sur] ¿Dónde quieres ir?")
		else:
			return
		movimiento(direccion, turno)

	def este(turno):
		if turno == 1:
			print("[Desde la lejanía ves un oso y te das la vuelta, vuelves al cruce anterior]")
		else:
			return
		movimiento(direccion, turno)

	def oeste(turno):
		if turno == 1:
			input("[Te encuentras otro camino al oeste] ¿Dónde quieres ir?")
		else:
			return
		movimiento(direccion, turno)


	print("\tEsta va a ser una gran aventura.")

	movimiento("", turno)

	print("=========================================\n",
		  "   Nombre: ", nombre, "|| Nivel: ", nivel, "\n", 
		  "=========================================\n",
		  sep='')

main()