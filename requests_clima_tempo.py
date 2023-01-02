import requests
from bs4 import BeautifulSoup


html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/229/ananindeua-pa').content

soup = BeautifulSoup(html, 'html.parser')

temp_min = soup.find(id='min-temp-1')
temp_max = soup.find(id='max-temp-1')
resumo = soup.find(class_='col-md-6 col-sm-12')

print(f' A temperatura mínima é: {temp_min.text}')
print(f'A temperatura máxima é : {temp_max.text} ')
print(f'Resumo: {resumo.text}')
