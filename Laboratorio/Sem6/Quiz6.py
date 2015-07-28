print("directorio")
directorio = {}
opcion = 0
while opcion != 5:
  print("1. observe numero")
  print("2. ingresar numero ")
  print("3. eliminar numero")
  print("4. buscar numero")
  print("5. salir")
  
  opcion =int( input("ingresar obcion: "))
  if opcion == 1:
    print("agenda\n" + str(directorio)+"")
  if opcion == 2:
    nombre = input("ingrasar contacto: ")
    num = int(input("numero de contacto: "))
    directorio[nombre] = num
  if opcion == 3:
    nombre = input("nonbre del contacto:")
    del directorio[nombre]
  if opcion == 4:
    nombre = input("ingrasar numero de la persona:")
    print(str(directorio[nombre]) )

