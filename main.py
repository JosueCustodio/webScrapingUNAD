# main.py

import ofertaAcademica
import consultaCarrera
import consultaPostgrado

def mostrar_menu():
    print("\n========== MENÚ DE CONSULTA ==========\n")
    print("1. Ver Carreras de Grado")
    print("2. Ver Carreras de Postgrado")
    print("3. Ver Facultades")
    print("4. Consultar Informacion de una Carrera de Grado")
    print("5. Consultar Informacion de una Carrera de Post Grado")
    print("6. Salir del Programa")

while True:
    mostrar_menu()
    opcion = input("\n Selecciona una opción (1-6): ")

    if opcion == "1":
        ofertaAcademica.buscarCarrerasGrado()
    elif opcion == "2":
        ofertaAcademica.buscarCarrerasPostGrado()
    elif opcion == "3":
        ofertaAcademica.buscarFacultad()
    elif opcion == "4":
        consultaCarrera.consultarCarrera()
    elif opcion == "5":
        consultaPostgrado.consultarPostgrado()
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
