import socket

dip = input("introdusca la direcion IP: ")
inicio = int(input("ingrese un puerto:"))
final= int(input("introdusca puerto final:"))

conexion = socket.socket()
for i in range(inicio,final+1):
	try:
		conexion.connect( (dip, i) )
		print ("Puerto : %s Abierto." % i)
	except:
			print ("Puerto : %s Cerrado." % i)
conexion.close()