from datetime import datetime


USUARIO = "usuario_cliente"


def registrar_log(operacion):
    try:
        fecha = datetime.now()

        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"Fecha: {fecha} | Usuario: {USUARIO} | Operación: {operacion}\n"
            )
    except Exception as error:
        print(f"Error al registrar log: {error}")