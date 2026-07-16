import requests
from config import BASE_URL, HEADERS
from logs import registrar_log

def menu_internaciones():
    while True:
        print("\n==============================")
        print("     MENÚ INTERNACIONES")
        print("==============================")
        print("1. Alta internación")
        print("2. Buscar internación")
        print("3. Modificar internación")
        print("4. Eliminar internación")
        print("5. Listar internaciones")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_internacion()

        elif opcion == "2":
            buscar_internacion()

        elif opcion == "3":
            modificar_internacion()

        elif opcion == "4":
            eliminar_internacion()

        elif opcion == "5":
            listar_internaciones()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")


#=======alta internacion========1
def alta_internacion():
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

        respuesta = requests.post(
            url,
            json=internacion,
            headers=HEADERS
        )

        if respuesta.status_code in [200, 201]:
            registrar_log("Internación creada correctamente")
            print("Internación creada correctamente")
            print(respuesta.json())

        else:
            print("Error al crear internación")
            print(respuesta.text)

    except ValueError:
        print("Los IDs y la habitación deben ser números.")

    except Exception as error:
        print(f"Ocurrió un error: {error}")


#=======buscar internaciones======= 2
def buscar_internacion():
    try:
        id_internacion = input("Ingrese ID de la internación: ")

        url = f"{BASE_URL}/internaciones/{id_internacion}"

        respuesta = requests.get(
            url,
            headers=HEADERS
        )

        if respuesta.status_code == 200:
            internacion = respuesta.json()
            registrar_log("Internación encontrada correctamente")

            print("\nInternación encontrada:")
            print("------------------------")
            print(f"ID: {internacion['id']}")
            print(f"Paciente ID: {internacion['paciente_id']}")
            print(f"Médico ID: {internacion['medico_id']}")
            print(f"Fecha ingreso: {internacion['fecha_ingreso']}")
            print(f"Diagnóstico: {internacion['diagnostico']}")
            print(f"Habitación: {internacion['habitacion']}")
            print(f"Estado: {internacion['estado']}")

        else:
            print("Internación no encontrada")
            print(respuesta.text)

    except Exception as error:
        print(f"Ocurrió un error: {error}")

# ======= modificar internacion ======= 3
def modificar_internacion():
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

        respuesta = requests.put(
            url,
            json=internacion,
            headers=HEADERS
        )

        if respuesta.status_code == 200:
            print("Internación modificada correctamente")
            registrar_log("Internación modificada correctamente")
            print(respuesta.json())

        else:
            print("Error al modificar internación")
            print(respuesta.text)

    except ValueError:
        print("El ID del médico y la habitación deben ser números.")

    except Exception as error:
        print(f"Ocurrió un error: {error}")

# ======= eliminar internacion ======= 4
def eliminar_internacion():
    try:
        id_internacion = input("Ingrese ID de la internación a eliminar: ")

        url = f"{BASE_URL}/internaciones/{id_internacion}"

        respuesta = requests.delete(
            url,
            headers=HEADERS
        )

        if respuesta.status_code==204:
            print("Internación eliminada correctamente")
            registrar_log("Internación eliminada correctamente")
        else:
            print("Error al eliminar internación")
            print(respuesta.text)

    except Exception as error:
        print(f"Ocurrió un error: {error}")

# ======= listar internaciones ======= 5

def listar_internaciones():
    try:
        url = f"{BASE_URL}/internaciones/"

        respuesta = requests.get(
            url,
            headers=HEADERS
        )

        if respuesta.status_code == 200:
            internaciones = respuesta.json()
            registrar_log("Internaciones listadas correctamente")

            if len(internaciones) == 0:
                print("No hay internaciones registradas")

            else:
                for internacion in internaciones:
                    print("\n----------------")
                    print(f"ID: {internacion['id']}")
                    print(f"Paciente ID: {internacion['paciente_id']}")
                    print(f"Médico ID: {internacion['medico_id']}")
                    print(f"Fecha ingreso: {internacion['fecha_ingreso']}")
                    print(f"Diagnóstico: {internacion['diagnostico']}")
                    print(f"Habitación: {internacion['habitacion']}")
                    print(f"Estado: {internacion['estado']}")

        else:
            print("Error al listar internaciones")
            print(respuesta.text)

    except Exception as error:
        print(f"Ocurrió un error: {error}")