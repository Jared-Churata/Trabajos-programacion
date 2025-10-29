turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "003": ["Julian Martinez", "Argentina", "19-09-2023"],
    "004": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "008": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "009": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "010": ["Ana Santos", "Brasil", "03-10-2023"],
    "011": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "012": ["Sofia Gomez", "Argentina", "07-04-2024"],
}
def turistas_por_pais(pais):
    Buscar_Turistas_por_pais = [datos[0] for datos in turistas.values() if datos[1].lower() == pais.lower()]
    if Buscar_Turistas_por_pais:
        print(f"Turistas de {pais}:")
        for nombre in Buscar_Turistas_por_pais:
            print("-", nombre)
    else:
        print(f"No hay turistas llamados {pais}.")
def turistas_por_mes(mes):
    while mes < 1 or mes > 12:
        print("Mes inválido por favor el numero del mes debe estar entre 1 y 12.")
        try:
            mes = int(input("Ingrese el mes del 1 al 12: "))
        except ValueError:
            mes = 0
    total = len(turistas)
    conteo_mes = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_turista = int(fecha.split("-")[1])
        if mes_turista == mes:
            conteo_mes += 1

    porcentaje = round((conteo_mes / total) * 100, 1)
    return porcentaje
def eliminar_turista():
    nombre = input("Ingrese el nombre del turista para eliminarlo: ").strip()
    eliminado = False
    for key, datos in list(turistas.items()):
        if datos[0].lower() == nombre.lower():
            del turistas[key]
            eliminado = True
            break
    if eliminado:
        print("Turista eliminado con éxito.")
    else:
        print("No existen turistas con ese nombre.")
def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1.- Turistas por país")
        print("2.- Turista por mes")
        print("3.- Eliminar turista")
        print("4.- Salir")
        op = input("Ingresf op: ")
        if op == "1":
            pais = input("Ingrese el país: ")
            turistas_por_pais(pais)
        elif op == "2":
            try:
                mes = int(input("Ingrese el mes (1-12): "))
                porcentaje = turistas_por_mes(mes)
                print(f"Porcentaje de turistas que ingresaron en el mes {mes}: {porcentaje}%")
            except ValueError:
                print("Debe ingresar un número válido.")
        elif op == "3":
            eliminar_turista()
        elif op == "4":
            print("Adios papu...")
            break
        else:
            print("Debe seleccionar una opción válida.")
menu()