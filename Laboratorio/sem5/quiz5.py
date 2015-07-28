import os
print ("Supermercado abc")
lista = []
opcion=0
contador = 0
while opcion != "4":
		print("1. introdusca un objeto")
		print("2. Eliminar un objeto")
		print("3. chequear su lista")
		print("4. Salir")
		
		opcion = input("ingresa una opcion: ")
		
		if opcion == "1":
				objeto=input("Instrodusca un  objeto a agregar: ")
				contador = contador + 1
				objeto = (str(contador)+"- "+ str (objeto))
				lista.append(objeto)
		if opcion == "2":
				print(lista)
				eliminar= int(input("Instrodusca el objeto a eliminar: "))
				print(lista[eliminar]+" el archivo es eliminado")
				del lista [eliminar]
		if opcion == "3":
				print(lista)
input ()