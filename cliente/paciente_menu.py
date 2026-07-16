import requests

#Menu de pacientes
def menu_pacientes():
    while True:
        print("\n===== GESTIÓN DE PACIENTES =====")
        print("1 - Alta pacientes")
        print("2 - Buscar paciente")
        print("3 - Modificar paciente")
        print("4 - Eliminar paciente")
        print("5 - Listar pacientes")
        print("6 - Volver")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                alta_paciente()

            case "2":
                buscar_paciente()

            case "3":
                modificar_paciente()

            case "4":
                eliminar_paciente()

            case "5":
                listar_pacientes()
                
            case "6":
                break

            case _:
                print("Opción inválida")

#=============alta paciente ====================================1
def alta_paciente():
    try:
        url = "http://127.0.0.1:8000/pacientes"

        paciente = {
            "dni": input("DNI: "),
            "nombre": input("Nombre: "),
            "apellido": input("Apellido: "),
            "edad": int(input("Edad: ")),
            "telefono": input("Teléfono: "),
            "obra_social": input("Obra social: ")
        }
        respuesta = requests.post(url, json=paciente)

        if respuesta.status_code == 200 or respuesta.status_code == 201:
            print("Paciente creado correctamente")
            print(respuesta.json())

        else:
            print("Error al crear paciente")
            print(respuesta.json())

    except ValueError:
        print("La edad debe ser un número.")

    except Exception as error:
        print(f"Ocurrió un error: {error}")


#=============buscar paciente ====================================2
def buscar_paciente():
    id_paciente = input("Ingrese ID del paciente: ")

    try:
        url = f"http://127.0.0.1:8000/pacientes/{id_paciente}"

        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            paciente = respuesta.json()

            print("\nPaciente encontrado:")
            print(f"ID: {paciente['id']}")
            print(f"Nombre: {paciente['nombre']} {paciente['apellido']}")
            print(f"DNI: {paciente['dni']}")

        else:
            print("Paciente no encontrado.")

    except Exception as error:
        print(f"Ocurrió un error: {error}")


#=============modificar paciente ====================================3
def modificar_paciente():
    try:
        id_paciente = input("Ingrese ID del paciente a modificar: ")

        url = f"http://127.0.0.1:8000/pacientes/{id_paciente}"

        paciente = {
            "dni": input("Nuevo DNI: "),
            "nombre": input("Nuevo nombre: "),
            "apellido": input("Nuevo apellido: "),
            "edad": int(input("Nueva edad: ")),
            "telefono": input("Nuevo teléfono: "),
            "obra_social": input("Nueva obra social: ")
        }

        respuesta = requests.put(url, json=paciente)

        if respuesta.status_code == 200:
            print("Paciente modificado correctamente")
            print(respuesta.json())

        else:
            print("Error al modificar paciente")
            print(respuesta.json())

    except ValueError:
        print("La edad debe ser un número.")

    except Exception as error:
        print(f"Ocurrió un error: {error}")


#===========eliminar paciente=====================================4
def eliminar_paciente():
    try:
        id_paciente = input("Ingrese ID del paciente a eliminar: ")

        url = f"http://127.0.0.1:8000/pacientes/{id_paciente}"

        respuesta = requests.delete(url)

        if respuesta.status_code == 200 or respuesta.status_code == 204:
            print("Paciente eliminado correctamente")
    

        else:
            print("Error al eliminar paciente")
            print(respuesta.text())

    except Exception as error:
        print(f"Ocurrió un error: {error}")


#=============listar pacientes ====================================5
def listar_pacientes():
    try:
        url = "http://127.0.0.1:8000/pacientes"

        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            pacientes = respuesta.json()

            for paciente in pacientes:
                print("\n----------------")
                print(f"ID: {paciente['id']}")
                print(f"Nombre: {paciente['nombre']} {paciente['apellido']}")
                print(f"DNI: {paciente['dni']}")
                print(f"Edad: {paciente['edad']}")
        else:
            print("Error al obtener pacientes.")

    except Exception as error:
        print(f"Ocurrió un error: {error}")