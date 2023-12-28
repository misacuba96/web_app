DIRECCIÓN = "tareas.txt"


def leer_tareas(direccion=DIRECCIÓN):
    """" Lee un archivo y guarda el contenido
     en una lista que proporcionemos"""
    with open(direccion, 'r') as file_local:
        lista_local = file_local.readlines()
    return lista_local


def escribir_tareas(variable, direccion=DIRECCIÓN):
    """" Sobreescribe el contenido de un archivo
    con las líneas de una lista que proporcionemos"""
    with open(direccion, 'w') as file_local:
        file_local.writelines(variable)


if __name__ == "__main__":
    print("Estoy en el archivo de las funciones y no me ejecuto")