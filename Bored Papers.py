import requests
from bs4 import BeautifulSoup
from random import randint
import pyperclip

try:
    r = requests.get('https://en.wikipedia.org/wiki/Portal:Science/Categories_and_Main_topics')
except:
    print('Erro ao conectar com a internet')
try:
    soup = BeautifulSoup(r.text, "html5lib")
except:
    print('Erro ao analisar arquivo\nConfira se as dependências: BeautifulSoup e html5lib estão instaladas na máquina e tente novamente.')

subjects = soup.find_all('a')
def random_subjects():
    # Subjects starts at 14
    random_a = randint(14, len(subjects))
    print(f'Tópico escolhido: {subjects[random_a].text}')
    return subjects[random_a].text

def fmted_url(sbjct):
    # Google's schoolar base url
    url = 'https://scholar.google.com.br/scholar?hl=eng&as_sdt=0%2C5&q={}&oq='
    final_url = url.format(sbjct)
    return final_url

try:
    pyperclip.copy(fmted_url(random_subjects()))
    print('Link copiado !')
except:
    print('Erro ao copiar\nCópia manual necessária:')
    print(f'Link: {fmted_url(random_subjects())}')
