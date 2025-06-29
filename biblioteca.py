# Sistema de Biblioteca - Versión para principiantes sin emojis

usuarios = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []}
]

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "García Márquez", "cantidad_disponible": 2},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "cantidad_disponible": 1},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "cantidad_disponible": 0}
]

def buscar_usuario(rut):
    for usuario in usuarios:
        if usuario["rut"] == rut:
            return usuario
    return None

def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        rut = input("Ingrese el RUT: ")
        nuevo = {"nombre": nombre, "apellido": apellido, "rut": rut, "libros": []}
        usuarios.append(nuevo)
        print("Usuario registrado correctamente.")
    except:
        print("Error al registrar el usuario.")

def registrar_libro():
    try:
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        cantidad = int(input("Cantidad disponible: "))
        nuevo_id = len(libros) + 1
        nuevo_libro = {"id": nuevo_id, "titulo": titulo, "autor": autor, "cantidad_disponible": cantidad}
        libros.append(nuevo_libro)
        print("Libro registrado correctamente.")
    except:
        print("Error: asegúrese de ingresar bien los datos.")

def prestar_libro(usuario):
    print("Libros disponibles para préstamo:")
    for libro in libros:
        print(f"{libro['id']}. {libro['titulo']} - Disponibles: {libro['cantidad_disponible']}")

    try:
        id_libro = int(input("Ingrese el ID del libro a prestar: "))
        for libro in libros:
            if libro["id"] == id_libro:
                if libro["cantidad_disponible"] > 0:
                    usuario["libros"].append(id_libro)
                    libro["cantidad_disponible"] -= 1
                    print("Libro prestado correctamente.")
                else:
                    print("No hay ejemplares disponibles de ese libro.")
                return
        print("No se encontró un libro con ese ID.")
    except:
        print("Error: debe ingresar un número válido.")

def devolver_libro(usuario):
    if not usuario["libros"]:
        print("Este usuario no tiene libros prestados.")
        return

    print("Libros que tiene el usuario:")
    for i, id_libro in enumerate(usuario["libros"]):
        for libro in libros:
            if libro["id"] == id_libro:
                print(f"{i+1}. {libro['titulo']}")

    try:
        opcion = int(input("Ingrese el número del libro que desea devolver: ")) - 1
        id_devuelto = usuario["libros"].pop(opcion)
        for libro in libros:
            if libro["id"] == id_devuelto:
                libro["cantidad_disponible"] += 1
                print("Libro devuelto correctamente.")
                return
    except:
        print("Error al devolver el libro.")

def menu():
    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Buscar usuario por RUT")
        print("2. Registrar nuevo usuario")
        print("3. Registrar nuevo libro")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            rut = input("Ingrese el RUT del usuario: ")
            usuario = buscar_usuario(rut)
            if usuario:
                print(f"Bienvenido, {usuario['nombre']} {usuario['apellido']}")
                while True:
                    print("1. Prestar un libro")
                    print("2. Devolver un libro")
                    print("3. Volver al menú principal")
                    subopcion = input("Seleccione una opción: ")
                    if subopcion == "1":
                        prestar_libro(usuario)
                    elif subopcion == "2":
                        devolver_libro(usuario)
                    elif subopcion == "3":
                        break
                    else:
                        print("Opción no válida.")
            else:
                print("Usuario no encontrado.")
                respuesta = input("¿Desea registrarlo? (s/n): ")
                if respuesta.lower() == "s":
                    registrar_usuario()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            registrar_libro()
        elif opcion == "4":
            print("Saliendo del sistema. Hasta luego.")
            break
        else:
            print("Opción no válida. Intente otra vez.")

# Iniciar el sistema
menu()
