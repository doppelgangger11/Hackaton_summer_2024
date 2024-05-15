from bs4 import BeautifulSoup
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

def main():
    url_base = 'https://gatob.kz/'

    url = f'{url_base}#tab05_2024/'

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        html_content = response.text
    else:
        print('Ошибка при получении страницы:', response.status_code)

    soup = BeautifulSoup(html_content, 'html.parser')

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