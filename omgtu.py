import requests
from bs4 import BeautifulSoup

def parserOmgtu():
    url = 'https://www.omgtu.ru/general_information/faculties/?ysclid=lwnb9hv6nf235925504'
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.find('div', id='pagecontent')
    return block

def getFaculties():
    block = parserOmgtu()
    if block:
        faculties = block.find_all('a')
        faculty_names = [faculty.text.strip() for faculty in faculties]
        return faculty_names
    return []