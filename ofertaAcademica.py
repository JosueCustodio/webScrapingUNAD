# ofertaAcademica.py

from bs4 import BeautifulSoup
import requests

# URLs
URL_BASE = 'https://unad.edu.do/'
OFERTA_ACADEMICA = URL_BASE + 'oferta/'

# Obtener el HTML
pedido_obtenido = requests.get(OFERTA_ACADEMICA)
html_obtenido = pedido_obtenido.text

# Parsear el HTML
soup = BeautifulSoup(html_obtenido, 'html.parser')
sections = soup.find_all('section')

# Variables globales para usar en funciones
carrerasGrado = sections[0] if len(sections) > 0 else None
carrerasPostGrado = sections[1] if len(sections) > 1 else None
facultades = sections[2] if len(sections) > 2 else None

def buscarCarrerasGrado():
    if carrerasGrado:
        nombreCarreraGrado = carrerasGrado.find_all('span', class_='elementor-button-text')
        print("\n -------------------------------------------- \n")
        print("Las Carreras de Grado De La UNAD Son Las Siguientes: \n")
        for carreraGrado in nombreCarreraGrado:
            print(carreraGrado.text.strip())
    else:
        print("No se encontraron secciones para carreras de grado.")

def buscarCarrerasPostGrado():
    if carrerasPostGrado:
        nombreCarreraPostGrado = carrerasPostGrado.find_all('span', class_='elementor-button-text')
        print("\n -------------------------------------------- \n")
        print("Las Carreras de PostGrado De La UNAD Son Las Siguientes: \n")
        for carreraPostGrado in nombreCarreraPostGrado:
            print(carreraPostGrado.text.strip())
    else:
        print("No se encontraron secciones para carreras de postgrado.")

def buscarFacultad():
    if facultades:
        nombreFacultad = facultades.find_all('span', class_='elementor-button-text')
        print("\n -------------------------------------------- \n")
        print("Las Facultades De La UNAD Son Las Siguientes: \n")
        for facultad in nombreFacultad:
            print(facultad.text.strip())
    else:
        print("No se encontraron secciones para facultades.")
