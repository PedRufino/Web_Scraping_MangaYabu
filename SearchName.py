from header import headers
from bs4 import BeautifulSoup
import requests
import json
import os

os.system('cls')
lists = []
while True:
    nome = input('Digite o nome do manga:\n>>> ')
    nome = nome.replace(" ","-").replace(".","-").replace("--","-")
    sima = nome.lower()

    os.system('cls')

    response = requests.get('https://mangayabu.top/api/show3.php', headers=headers)
    soupe = BeautifulSoup(response.text, 'html.parser').text
    slg = json.loads(str(soupe))
    num = len(slg)

    for x in range(num):
        mas = slg[x]['slug']
        lists.append(mas)

    str_match = list(filter(lambda x: sima in x, lists))
    qtd = len(str_match)

    if qtd > 11:
        print('ERRO: MUITOS MANGAS ENCONTRADOS\n')
        print('SEJA ESPECÍFICO\n')
    elif qtd > 1:
        os.system('cls')
        for x in range(qtd):
            print(f'{x} - {str_match[x]}')
        print('='*55)
        print(f'Total de Mangas encontrados: {qtd}\nEsolha um numero:')
        num = int(input('>>> '))
        mg_name = str_match[num]
        break
    else:
        mg_name = str_match[0]
        break

