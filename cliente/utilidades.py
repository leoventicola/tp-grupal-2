import os

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("Presione Enter para continuar...")

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()

        if valor:
            return valor

        print("El campo no puede estar vacío.")

def mostrar_error(respuesta):
    try:
        error = respuesta.json()

        if isinstance(error.get("detail"), list):
            for detalle in error["detail"]:
                print(f"- {detalle['msg']}")
        else:
            print(error["detail"])
    except Exception:
        print("Error inesperado")