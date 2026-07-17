import requests
from config import BASE_URL, HEADERS
from logs import registrar_log
from utilidades import *

def menu_internaciones():
    while True:
        limpiar()
        print("===== GESTIÓN DE INTERNACIONES =====")
        print("1. Alta internación")
        print("2. Buscar internación")
        print("3. Modificar internación")
        print("4. Eliminar internación")
        print("5. Listar internaciones")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                alta_internacion()

            case "2":
                buscar_internacion()

            case "3":
                modificar_internacion()

            case "4":
                eliminar_internacion()

            case "5":
                listar_internaciones()

            case "6":
                break
            case _:
                print("Opción inválida")
                pausar()
    


#=======alta internacion========1
def alta_internacion():
    limpiar()
    try:
        url = f"{BASE_URL}/internaciones/"
        internacion = {
            "paciente_id": int(input("ID paciente: ")),
            "medico_id": int(input("ID médico: ")),
            "fecha_ingreso": input("Fecha ingreso: "),
            "diagnostico": input("Diagnóstico: "),
            "habitacion": int(input("Habitación: ")),
            "estado": input("Estado: ")
        }

        respuesta = requests.post(url,json=internacion,headers=HEADERS)

        if respuesta.status_code in [200, 201]:
            internacion_creada = respuesta.json()
            print("Internación creada correctamente")
            print(f"ID de la internación creada: {internacion_creada['id']}")
            registrar_log(f"Internación creada correctamente. ID: {internacion_creada['id']}")
        elif respuesta.status_code == 400:
            mostrar_error(respuesta)
            registrar_log(f"Error al crear internación: {respuesta.text}")
        elif respuesta.status_code == 422:
            mostrar_error(respuesta)
            registrar_log(f"Error de validacion al crear internacion: {respuesta.text}")

        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al crear internación: {respuesta.text}")
        pausar()

    except ValueError:
        print("Los IDs y la habitación deben ser números.")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Ocurrió un error: {error}")
        pausar()


#=======buscar internaciones======= 2
def buscar_internacion():
    limpiar()
    try:
        id_internacion = input("Ingrese ID de la internación: ")
        url = f"{BASE_URL}/internaciones/{id_internacion}"
        respuesta = requests.get(url, headers=HEADERS)

        if respuesta.status_code == 200:
            internacion = respuesta.json()
            registrar_log(f"Internación encontrada correctamente. ID: {id_internacion}")
            print("Internación encontrada:")
            print("------------------------")
            print(f"ID: {internacion['id']}")
            print(f"Paciente ID: {internacion['paciente_id']}")
            print(f"Médico ID: {internacion['medico_id']}")
            print(f"Fecha ingreso: {internacion['fecha_ingreso']}")
            print(f"Diagnóstico: {internacion['diagnostico']}")
            print(f"Habitación: {internacion['habitacion']}")
            print(f"Estado: {internacion['estado']}")
            print("------------------------")
        elif respuesta.status_code == 404:
            print("Internación no encontrada")
            registrar_log(f"Internación no encontrada. ID: {id_internacion}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Internación no encontrada. ID: {id_internacion}")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Ocurrió un error al buscar internación: {error}")
        pausar()

# ======= modificar internacion ======= 3
def modificar_internacion():
    limpiar()
    try:
        id_internacion = input("ID de la internación a modificar: ")
        url = f"{BASE_URL}/internaciones/{id_internacion}"

        internacion = {
            "medico_id": int(input("Nuevo ID médico: ")),
            "fecha_ingreso": input("Nueva fecha ingreso: "),
            "diagnostico": input("Nuevo diagnóstico: "),
            "habitacion": int(input("Nueva habitación: ")),
            "estado": input("Nuevo estado: ")
        }
        respuesta = requests.put(url,json=internacion, headers=HEADERS)

        if respuesta.status_code == 200:
            print("Internación modificada correctamente")
            registrar_log(f"Internación modificada correctamente. ID: {id_internacion}")
            print(respuesta.json())
        elif respuesta.status_code == 404:
            print("Internación no encontrada.")
            registrar_log(f"Intento de modificación de internación no encontrada. ID: {id_internacion}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al modificar internación. ID: {id_internacion}")
        pausar()
    except ValueError:
        print("El ID del médico y la habitación deben ser números.")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al modificar internación: {error}")
        pausar()

# ======= eliminar internacion ======= 4
def eliminar_internacion():
    limpiar()
    try:
        id_internacion = input("Ingrese ID de la internación a eliminar: ")
        
        confirmacion = input(f"¿Está seguro que desea eliminar la internación con ID {id_internacion}? (s/n): ").strip().upper()
        if confirmacion != "S":
            print("Eliminación cancelada.")
            pausar()
            return
        url = f"{BASE_URL}/internaciones/{id_internacion}"
        respuesta = requests.delete(url, headers=HEADERS)

        if respuesta.status_code in [200, 204]:
            print("Internación eliminada correctamente")
            registrar_log(f"Internación eliminada correctamente. ID: {id_internacion}")
        elif respuesta.status_code == 404:
            print("Internación no encontrada.")
            registrar_log(f"Intento de eliminación de internación no encontrada. ID: {id_internacion}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al eliminar internación. ID: {id_internacion}")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al eliminar internación: {error}")
        pausar()

# ======= listar internaciones ======= 5

def listar_internaciones():
    limpiar()
    try:
        url = f"{BASE_URL}/internaciones/"
        respuesta = requests.get(url, headers=HEADERS)

        if respuesta.status_code == 200:
            internaciones = respuesta.json()
            registrar_log(f"Internaciones listadas correctamente")
            if not internaciones:
                print("No hay internaciones registradas")
            else:
                for internacion in internaciones:
                    print("----------------")
                    print(f"ID: {internacion['id']}")
                    print(f"Paciente ID: {internacion['paciente_id']}")
                    print(f"Médico ID: {internacion['medico_id']}")
                    print(f"Fecha ingreso: {internacion['fecha_ingreso']}")
                    print(f"Diagnóstico: {internacion['diagnostico']}")
                    print(f"Habitación: {internacion['habitacion']}")
                    print(f"Estado: {internacion['estado']}")
        else:
            mostrar_error(respuesta)
            registrar_log(f"Error al listar internaciones.{respuesta.text}")
        print("----------------")
        pausar()

    except Exception as error:
        print("Error {error}")
        registrar_log(f"Error al listar internaciones: {error}")
        pausar()