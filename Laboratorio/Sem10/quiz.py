import os
print ("cifrado de programa")
opcion = 0
menu=[]
d=""
while opcion != "4" :
		print ("1 introdusca texto")
		print ("2 cifrar texto")
		print ("3 descifrar texto")
		print ("4 imprimir el texto en pantalla")
		
		opcion = input ("instrodusca opcion:")
		
		if opcion == "1" :
			texto = input ("Introdusca texto: ")
		if opcion == "2" :
			for letra in (texto) :
				a=ord(letra)
				b=a+1
				c=chr(b)
				d=c+d
			print ("El texto cifrado es :",d)
				
input ()
				
			
			
			
		