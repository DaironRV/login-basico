# listas intoduccon

# arrai = ["futbol", "pc", 18.7, 18, [5,5,8], True, False]


# # el "[5]", es el numeor de dato que necedito, en este caso es el true, comienzan desde el 0
# print(arrai[-3])

# # si quiero usar para solamente un bloque, se le agrega un rango.
# print(arrai[2:-1])

# lsitas mis cosas


# # se pueden llamar listas dentro de listas.
# musica = ["gitarra", "flauta", "violin"]

# deporte = ["futbol", "spining", "basquetbool"]

# comida = ["papa", "verduras", "pan"]

# Conjuntos = [comida, deporte, musica]

# conjuntos2 = [comida, deporte]

# conjuntos3 = [musica,deporte]


# print(musica)

# print(conjuntos2)



# listas de datos: 

usuario = input("Crear nombre de usuario: ")
contraseña = input("Ingresa tu contraseña: ")
cedula = int(input("Ingresa tu número de identidad: "))

listaDatos = [usuario, contraseña, cedula]

while True:
    
    usuarioLogin = input("Ingresa tu nombre de usuario: ")
    contraseñaLogin = input("Ingresa tu contraseña: ")
    cedulaLogin = int(input("Ingresa tu número de identidad: "))
    
    if usuario.lower() == usuarioLogin and contraseña == contraseñaLogin and cedula == cedulaLogin: 
        print("Ingresaste de forma correcta al sistema")
        print(listaDatos)
        break
    
    elif usuario.lower() == usuarioLogin and contraseña == contraseñaLogin and cedula != cedulaLogin:
        print("La cédula no coincide")
        print(listaDatos[0:2]) 
        
    elif usuario.lower() == usuarioLogin and contraseña != contraseñaLogin and cedula == cedulaLogin:
        print("La contraseña no coincide")
        print([listaDatos[0], listaDatos[2]])  
        
    elif usuario.lower() != usuarioLogin and contraseña == contraseñaLogin and cedula == cedulaLogin:
        print("El usuario no coincide")
        print(listaDatos[1:]) 
        
    else:
        print("Ingresa datos correctos")

