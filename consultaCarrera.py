import requests
from bs4 import BeautifulSoup

URL_BASE = "https://www.unad.edu.do"
URL_OFERTA_ACADEMICA = URL_BASE + "/oferta/"

def consultarCarrera():
    # Obtener página de oferta académica
    respuesta = requests.get(URL_OFERTA_ACADEMICA)
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    # Buscar el primer <section> con las carreras de grado
    secciones = soup.find_all('section')
    if len(secciones) < 1:
        print("No se encontraron las carreras.")
        return

    carrerasGrado = secciones[0]
    links = carrerasGrado.find_all('a', class_='elementor-button-link')

    # Mostrar lista de carreras
    print("\nCarreras disponibles:\n")
    for i, link in enumerate(links):
        texto = link.find('span', class_='elementor-button-text').text.strip()
        print(f"{i + 1}. {texto}")

    # Preguntar al usuario cuál carrera quiere consultar
    opcion = input("\nElige una carrera por número: ")

    if not opcion.isdigit():
        print("Opción inválida.")
        return

    indice = int(opcion) - 1
    if indice < 0 or indice >= len(links):
        print("Número fuera de rango.")
        return

    # Obtener la ruta de la carrera
    enlace = links[indice].get('href')
    url_carrera = URL_BASE + enlace

    # Hacer solicitud a la página de la carrera
    respuesta_carrera = requests.get(url_carrera)
    soup_carrera = BeautifulSoup(respuesta_carrera.text, 'html.parser')

    print("\n-------------------------------------------\n")

    # Título
    titulo = soup_carrera.find('h1')
    if titulo:
        print("Carrera:", titulo.text.strip())

    # Descripción
    descripcion = soup_carrera.find('div', class_='elementor-widget-text-editor')
    if descripcion:
        print("\nDescripción:")
        print(descripcion.text.strip())

    # Campos como Duración, Modo, etc.
    etiquetas = soup_carrera.find_all('h2')
    for etiqueta in etiquetas:
        texto = etiqueta.text.strip().lower()
        if "duración" in texto or "modo" in texto or "facultad" in texto or "inicia" in texto:
            siguiente = etiqueta.find_next_sibling()
            if siguiente:
                print(f"\n{etiqueta.text.strip()}:")
                print(siguiente.text.strip())

    # ¿Qué hace un estudiante?
    que_hace = soup_carrera.find('h2', string=lambda t: t and "¿Que hace un estudiante" in t)
    if que_hace:
        parrafo = que_hace.find_next('p')
        if parrafo:
            print("\n¿Qué hace un estudiante?")
            print(parrafo.text.strip())

    print("\n-------------------------------------------")
