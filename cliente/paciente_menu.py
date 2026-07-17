import requests
from config import BASE_URL, HEADERS
from logs import registrar_log
from utilidades import *

#Menu de pacientes
def menu_pacientes():
    while True:
        limpiar()
        print("===== GESTIÓN DE PACIENTES =====")
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
                pausar()


#=============alta paciente ====================================1
def alta_paciente():
    limpiar()
    try:
        url = f"{BASE_URL}/pacientes/"
        paciente = {
            "dni": input("DNI: "),
            "nombre": pedir_texto("Nombre: "),
            "apellido": pedir_texto("Apellido: "),
            "edad": int(input("Edad: ")),
            "telefono": input("Teléfono: "),
            "obra_social": input("Obra social: ")
        }
        respuesta = requests.post(url, json=paciente , headers=HEADERS)

        if respuesta.status_code in [200, 201]:
            paciente_creado = respuesta.json()
            print("Paciente creado correctamente")
            print(f"ID del paciente creado: {paciente_creado['id']}")
            registrar_log(f"Paciente creado correctamente. ID: {paciente_creado['id']}")
        elif respuesta.status_code == 400:
            registrar_log(f"Error al crear paciente: {respuesta.text}")
            mostrar_error(respuesta)
        else:
            registrar_log(f"Error al crear paciente: {respuesta.text}")
            mostrar_error(respuesta)
        pausar()

    except ValueError:
        print("La edad debe ser un número.")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al crear paciente: {error}")
        pausar()


#=============buscar paciente ====================================2
def buscar_paciente():
    limpiar()
    try:
        id_paciente = input("Ingrese ID del paciente: ")
        url = f"{BASE_URL}/pacientes/{id_paciente}"
        respuesta = requests.get(url , headers=HEADERS)

        if respuesta.status_code == 200:
            registrar_log(f"Paciente encontrado correctamente. ID: {id_paciente}")
            paciente = respuesta.json()
            print("Paciente encontrado:")
            print("----------------")
            print(f"ID: {paciente['id']}")
            print(f"Nombre: {paciente['nombre']} {paciente['apellido']}")
            print(f"DNI: {paciente['dni']}")
            print(f"Edad: {paciente['edad']}")
            print(f"Teléfono: {paciente['telefono']}")
            print(f"Obra social: {paciente['obra_social']}")
            print("----------------")
        elif respuesta.status_code == 404:
            mostrar_error(respuesta)
            registrar_log(f"Intento de búsqueda de paciente no encontrado. ID: {id_paciente}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Intento de búsqueda de paciente no encontrado. ID: {id_paciente}")
        
        pausar()
    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al buscar paciente: {error}")
        pausar()


#=============modificar paciente ====================================3
def modificar_paciente():
    limpiar()
    try:
        id_paciente = input("Ingrese ID del paciente a modificar: ")
        url = f"{BASE_URL}/pacientes/{id_paciente}"

        paciente = {
            "dni": input("Nuevo DNI: "),
            "nombre": pedir_texto("Nuevo nombre: "),
            "apellido": pedir_texto("Nuevo apellido: "),
            "edad": int(input("Nueva edad: ")),
            "telefono": input("Nuevo teléfono: "),
            "obra_social": input("Nueva obra social: ")
        }
        respuesta = requests.put(url, json=paciente, headers=HEADERS)

        if respuesta.status_code == 200:
            print("Paciente modificado correctamente")
            registrar_log(f"Paciente modificado correctamente. ID: {id_paciente}")
            print(respuesta.json())
        elif respuesta.status_code == 404:
            mostrar_error(respuesta)
            registrar_log(f"Intento de modificación de paciente no encontrado. ID:{id_paciente}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al modificar paciente. ID: {id_paciente}")
        pausar()

    except ValueError:
        print("La edad debe ser un número.")
        pausar()
        
    except Exception as error:
        print("Error")
        registrar_log(f"Error al modificar paciente: {error}")
        pausar()


#===========eliminar paciente=====================================4
def eliminar_paciente():
    limpiar()
    try:
        id_paciente = input("Ingrese ID del paciente a eliminar: ")

        confirmacion = input(f"¿Está seguro que desea eliminar al paciente con ID {id_paciente}? (s/n): ").strip().upper()
        if confirmacion != "S":
            print("Eliminación cancelada.")
            pausar()
            return
        url = f"{BASE_URL}/pacientes/{id_paciente}"
        respuesta = requests.delete(url , headers=HEADERS)

        if respuesta.status_code == 204:
            print("Paciente eliminado correctamente")
            registrar_log("Paciente eliminado correctamente")
        elif respuesta.status_code == 404:
            mostrar_error(respuesta)
            registrar_log("Intento de eliminación de paciente no encontrado")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al eliminar paciente: {respuesta.status_code} - {respuesta.text}")

        pausar()
    except Exception as error:
        print("Error")
        registrar_log(f"Error al eliminar paciente: {error}")
        pausar()


#=============listar pacientes ====================================5
def listar_pacientes():
    limpiar()
    try:
        url = f"{BASE_URL}/pacientes/"
        respuesta = requests.get(url, headers=HEADERS)

        if respuesta.status_code == 200:
            registrar_log("Pacientes listados correctamente")
            pacientes = respuesta.json()     

            if not pacientes:
                print("No hay pacientes registrados.")
            else:   
                for paciente in pacientes:
                    print("----------------")
                    print(f"ID: {paciente['id']}")
                    print(f"Nombre: {paciente['nombre']} {paciente['apellido']}")
                    print(f"DNI: {paciente['dni']}")
                    print(f"Edad: {paciente['edad']}")
                    print(f"Teléfono: {paciente['telefono']}")
                    print(f"Obra social: {paciente['obra_social']}")
        else:
            mostrar_error(respuesta)

        print("----------------")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al listar pacientes: {error}")
        pausar()
