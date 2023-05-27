import requests
from bs4 import BeautifulSoup
import sys

code = str(sys.argv[1])


def news():
    url = f'https://aisweb.decea.mil.br/?i=aerodromos&codigo={code}'

    resp = requests.get(url)

    if resp.status_code == 200:
        print("Successfully opened the web page")

        soup = BeautifulSoup(resp.text, 'html.parser')

        elements = soup.find_all('ul', class_='list list-icons list-primary list-icons-style-2')

        cartas = []
        for element in elements:
            sibling = element.find_previous_sibling('h4')
            cartas.append(sibling.text)

        print(f'Cartas: {cartas}')
        sunrise = soup.find('sunrise').text
        print(f'Nascer do Sol: {sunrise}')
        sunset = soup.find('sunset').text
        print(f'Pôr do Sol: {sunset}')

        taf_metar_element = soup.find_all('h5', class_='mb-0 heading-primary')
        for el in taf_metar_element:

            sibling = el.find_next_sibling('p').text
            print(el.text + " " + sibling)

    else:
        print("Error")


news()
