from bs4 import BeautifulSoup
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from typing import Any

urllib3.disable_warnings(InsecureRequestWarning)

def main() -> (dict[str, dict[str, Any]]):
    url_base = 'https://gatob.kz/'

    url = f'{url_base}#tab05_2024/'

    try:
        response = requests.get(url, verify=False)
        print(f'Подключение к серверу прошло успешно, {response.status_code = }')
    except requests.exceptions.ConnectionError as e:
        print("Не удалось подключиться к серверу:", e)
        exit()
        
    soup = BeautifulSoup(response.text, 'html.parser')

    slides = soup.find_all('a', class_='poster-prev')

    list_of_features = dict()

    for slide in slides:
        title = slide.find('span').text.strip()
        link = slide['href']
        date = slide.find('p', class_='date').text.split(' - ')
        id_ = link.split('/')
        id_ = id_[3].split('-')
        id_ = id_[0]
        
        list_of_features[id_] = ({
            'title': title,
            'date': date,
            'link': url_base + link
        })

    return list_of_features