import requests
from config import BASE_URL, HEADERS
from logs import registrar_log
from utilidades import *

def menu_medicos():
    while True:
        limpiar()
        print("===== GESTIÓN DE MÉDICOS =====")
        print("1 - Alta médicos")
        print("2 - Buscar médico")
        print("3 - Modificar médico")
        print("4 - Eliminar médico")
        print("5 - Listar médicos")
        print("6 - Volver")

        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                alta_medico()

            case "2":
                buscar_medico()

            case "3":
                modificar_medico()

            case "4":
                eliminar_medico()

            case "5":
                listar_medicos()

            case "6":
                break

            case _:
                print("Opción inválida")
                pausar()


# =======alta medico========1
def alta_medico():
    limpiar()
    try:
        url = f"{BASE_URL}/medicos/"
        medico = {
            "matricula": pedir_texto("Matrícula: "),
            "nombre": pedir_texto("Nombre: "),
            "apellido": pedir_texto("Apellido: "),
            "especialidad": pedir_texto("Especialidad: "),
            "telefono": input("Teléfono: ")
        }
        respuesta = requests.post(url, json=medico, headers=HEADERS)

        if respuesta.status_code in [200, 201]:
            medico_creado = respuesta.json()
            print("Médico creado correctamente")
            print(f"ID del médico creado: {medico_creado['id']}")
            registrar_log(f"Médico creado correctamente. ID: {medico_creado['id']}")
        elif respuesta.status_code == 400:
            mostrar_error(respuesta)
            registrar_log(f"Error al crear médico:{respuesta.text}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al crear médico: {respuesta.text}")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al crear médico: {error}")
        pausar()

#=======buscar medico========2
def buscar_medico():
    limpiar()
    try:
        id_medico = input("Ingrese ID del médico: ")
        url = f"{BASE_URL}/medicos/{id_medico}"
        respuesta = requests.get(url , headers=HEADERS)

        if respuesta.status_code == 200:
            registrar_log(f"Médico encontrado correctamente. ID: {id_medico}")
            medico = respuesta.json()
            print("Médico encontrado:")
            print("----------------")
            print(f"ID: {medico['id']}")
            print(f"Matrícula: {medico['matricula']}")
            print(f"Nombre: {medico['nombre']} {medico['apellido']}")
            print(f"Especialidad: {medico['especialidad']}")
            print(f"Teléfono: {medico['telefono']}")
            print("----------------")
        elif respuesta.status_code == 404:
            mostrar_error(respuesta)
            registrar_log(f"Médico no encontrado. ID: {id_medico}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al buscar médico. ID: {id_medico}")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al buscar médico: {error}")
        pausar()

#=======modificar medico========3
def modificar_medico():
    limpiar()
    try:
        id_medico = input("ID del médico a modificar: ")
        url = f"{BASE_URL}/medicos/{id_medico}"

        medico = {
            "matricula": pedir_texto("Nueva matrícula: "),
            "nombre": pedir_texto("Nuevo nombre: "),
            "apellido": pedir_texto("Nuevo apellido: "),
            "especialidad": pedir_texto("Nueva especialidad: "),
            "telefono": input("Nuevo teléfono: ")
        }
        respuesta = requests.put(url, json=medico, headers=HEADERS)

        if respuesta.status_code == 200:
            print("Médico modificado correctamente")
            registrar_log(f"Médico modificado correctamente. ID: {id_medico}")
            print(respuesta.json())
        elif respuesta.status_code == 404:
            mostrar_error(respuesta)
            registrar_log(f"Intento de modificación de médico no encontrado. ID: {id_medico}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al modificar médico. ID: {id_medico}")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al modificar médico: {error}")
        pausar()


#=======eliminar medico========4
def eliminar_medico():
    limpiar()
    try:
        id_medico = input("Ingrese ID del médico a eliminar: ")

        confirmacion = input(f"¿Está seguro que desea eliminar al médico con ID {id_medico}? (s/n): ").strip().upper()
        if confirmacion != "S":
            print("Eliminación cancelada.")
            pausar()
            return
        url = f"{BASE_URL}/medicos/{id_medico}"
        respuesta = requests.delete(url , headers=HEADERS)

        if respuesta.status_code in [200, 204]:
            print("Médico eliminado correctamente")
            registrar_log(f"Médico eliminado correctamente. ID: {id_medico}")
        elif respuesta.status_code == 404:
            print("Médico no encontrado.")
            registrar_log(f"Intento de eliminación de médico no encontrado. ID: {id_medico}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al eliminar médico. ID: {id_medico}")

        pausar()
    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al eliminar médico: {error}")
        pausar()


#========listar medicos========5
def listar_medicos():
    limpiar()
    try:
        url = f"{BASE_URL}/medicos/"
        respuesta = requests.get(url, headers=HEADERS)

        if respuesta.status_code == 200:
            registrar_log("Médicos listados correctamente")
            medicos = respuesta.json()
            if not medicos:
                print("No hay médicos registrados.")
            else:
                for medico in medicos:
                    print("----------------")
                    print(f"ID: {medico['id']}")
                    print(f"Matrícula: {medico['matricula']}")
                    print(f"Nombre: {medico['nombre']} {medico['apellido']}")
                    print(f"Especialidad: {medico['especialidad']}")
                    print(f"Teléfono: {medico['telefono']}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al listar médicos: {respuesta.text}")

        print("----------------")
        pausar()
        
    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al listar médicos: {error}")
        pausar()