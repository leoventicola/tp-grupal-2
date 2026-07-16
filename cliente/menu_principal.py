from paciente_menu import menu_pacientes
from medicos_menu import menu_medicos
from internaciones_menu import menu_internaciones


def menu_principal():
    while True:
        print("\n========================")
        print(" SISTEMA HOSPITALARIO")
        print("========================")
        print("1 - Gestionar pacientes")
        print("2 - Gestionar médicos")
        print("3 - Gestionar internaciones")
        print("4 - Salir")

        opcion = input("\nSeleccione una opción: ")

        match opcion:
            case "1":
                menu_pacientes()

            case "2":
                menu_medicos()

            case "3":
                menu_internaciones()

            case "4":
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()