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

# usuario = input("Crear nombre de usuario: ")
# contraseña = input("Ingresa tu contraseña: ")
# cedula = int(input("Ingresa tu número de identidad: "))

# listaDatos = [usuario, contraseña, cedula]

# while True:
    
#     usuarioLogin = input("Ingresa tu nombre de usuario: ")
#     contraseñaLogin = input("Ingresa tu contraseña: ")
#     cedulaLogin = int(input("Ingresa tu número de identidad: "))
    
#     if usuario.lower() == usuarioLogin and contraseña == contraseñaLogin and cedula == cedulaLogin: 
#         print("Ingresaste de forma correcta al sistema")
#         print(listaDatos)
#         break
    
#     elif usuario.lower() == usuarioLogin and contraseña == contraseñaLogin and cedula != cedulaLogin:
#         print("La cédula no coincide")
#         print(listaDatos[0:2]) 
        
#     elif usuario.lower() == usuarioLogin and contraseña != contraseñaLogin and cedula == cedulaLogin:
#         print("La contraseña no coincide")
#         print([listaDatos[0], listaDatos[2]])  
        
#     elif usuario.lower() != usuarioLogin and contraseña == contraseñaLogin and cedula == cedulaLogin:
#         print("El usuario no coincide")
#         print(listaDatos[1:]) 
        
#     else:
#         print("Ingresa datos correctos")



# listas

arrai = ["cosas de la vida", "de la vida cosas", 2, 20.7, ["hola", "que", "hace"], True, False]

# funcion "len " es para contal la cantidad de datos que hay en una lista
print(len(arrai))

# la funcion append, es para agregar algo mas a la lista, al final
arrai.append(int(input("datoa a ingresar a la lsita: ")))

# funcón .insert, es para colocar un dato en la posicion señalada: .insert(1,) (el 1 es la posicion que quieres poner el dato)
arrai.insert(1,int(input("dato en numero que deseas agregar a la lisne ne la posicón 1")))
print(arrai)



# si necesito agregar mas de  un dato en especifico, puedo usar la funcion .exted([]), ya agregar una lista a una lista basia
arrai = []

arrai.extend([str(input("que valir tipo str deas aagregar: ")),
            int(input("que valor int deas agregar: ")),
            float(input("que valor tipo flotante deas agregar: ")),
            bool(input("que tipo de valor bool deas agregar: "))])

print(arrai)