import requests
from config import BASE_URL, HEADERS
from logs import registrar_log

def menu_medicos():

    while True:
        print("""
========================
    GESTIÓN MÉDICOS
========================
1 - Alta médico
2 - Buscar médico
3 - Modificar médico
4 - Eliminar médico
5 - Listar médicos
6 - Volver
""")

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

# =======alta medico========1
def alta_medico():
    try:
        url = f"{BASE_URL}/medicos/"

        medico = {
            "matricula": input("Matrícula: "),
            "nombre": input("Nombre: "),
            "apellido": input("Apellido: "),
            "especialidad": input("Especialidad: "),
            "telefono": input("Teléfono: ")
        }

        respuesta = requests.post(url, json=medico, headers=HEADERS)

        if respuesta.status_code in [200, 201]:
            print("Médico creado correctamente")
            registrar_log("Médico creado correctamente")
            print(respuesta.json())

        else:
            print("Error al crear médico")
            print(respuesta.text)

    except Exception as error:
        print(f"Ocurrió un error: {error}")

#=======buscar medico========2
def buscar_medico():
    try:
        id_medico = input("Ingrese ID del médico: ")

        url = f"{BASE_URL}/medicos/{id_medico}"

        respuesta = requests.get(url , headers=HEADERS)

        if respuesta.status_code == 200:
            registrar_log("Médico encontrado correctamente")
            medico = respuesta.json()

            print("----------------")
            print(f"ID: {medico['id']}")
            print(f"Matrícula: {medico['matricula']}")
            print(f"Nombre: {medico['nombre']}")
            print(f"Apellido: {medico['apellido']}")
            print(f"Especialidad: {medico['especialidad']}")
            print(f"Teléfono: {medico['telefono']}")

        else:
            print("Médico no encontrado")

    except Exception as error:
        print(f"Ocurrió un error: {error}")

#=======modificar medico========3
def modificar_medico():
    try:
        id_medico = input("ID del médico a modificar: ")

        url = f"{BASE_URL}/medicos/{id_medico}"

        medico = {
            "matricula": input("Nueva matrícula: "),
            "nombre": input("Nuevo nombre: "),
            "apellido": input("Nuevo apellido: "),
            "especialidad": input("Nueva especialidad: "),
            "telefono": input("Nuevo teléfono: ")
        }

        respuesta = requests.put(url, json=medico, headers=HEADERS)

        if respuesta.status_code == 200:
            print("Médico modificado correctamente")
            registrar_log("Médico modificado correctamente")
            print(respuesta.json())

        else:
            print("Error al modificar médico")
            print(respuesta.text)

    except Exception as error:
        print(f"Ocurrió un error: {error}")

#=======eliminar medico========4
def eliminar_medico():
    try:
        id_medico = input("Ingrese ID del médico a eliminar: ")

        url = f"{BASE_URL}/medicos/{id_medico}"

        respuesta = requests.delete(url , headers=HEADERS)

        if respuesta.status_code in [200, 204]:
            print("Médico eliminado correctamente")
            registrar_log("Médico eliminado correctamente")

        else:
            print("Error al eliminar médico")
            print(respuesta.text)

    except Exception as error:
        print(f"Ocurrió un error: {error}")


#========listar medicos========5
def listar_medicos():
    try:
        url = f"{BASE_URL}/medicos/"
        respuesta = requests.get(url, headers=HEADERS)

        if respuesta.status_code == 200:
            registrar_log("Médicos listados correctamente")
            medicos = respuesta.json()
            if len(medicos) == 0:
                print("No hay médicos registrados")
            else:
                for medico in medicos:
                    print("----------------")
                    print(f"ID: {medico['id']}")
                    print(f"Matrícula: {medico['matricula']}")
                    print(f"Nombre: {medico['nombre']}")
                    print(f"Apellido: {medico['apellido']}")
                    print(f"Especialidad: {medico['especialidad']}")
                    print(f"Teléfono: {medico['telefono']}")
        else:
            print("Error al listar médicos")
            print(respuesta.text)
    except Exception as error:
        print(f"Ocurrió un error: {error}")