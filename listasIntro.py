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
