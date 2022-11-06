from SearchName import mg_name
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import requests
import json
import re
import os
os.system('cls')

while True:
    try:
        response = requests.get(f'https://mangayabu.top/manga/{mg_name}')
        soupe = BeautifulSoup(response.text, 'html.parser')
        script_id = soupe.find('script', {'id': 'manga-info'}).text
    except AttributeError:
        print('MANGA NÃO ENCONTRADO!!')
    else:
        break
script_id = json.loads(script_id)
manga = script_id["chapter_name"]
manga = manga.replace(" ", "_").replace(":", "").replace(".", "")
genre = script_id["genres"]
sinopse = script_id["description"]

# Cria uma pasta com o nome do mangá formatado
# se essa pasta existir o processo para
try:
    manga_name = script_id["chapter_name"]
    os.mkdir(f'{manga}')
except Exception as erro:
    if erro.__class__ == FileExistsError:
        print(f'O Arquivo {manga} já Existe')
        exit
else:
    # Gera um arquivo de texto com o nome do mangá
    with open(f'{manga}/1#{manga}.txt', 'a', encoding='utf8')as file:
        file.write(f'Nome do mangá: {manga_name}\n\nGênero: ')

    # Ira gerar no mesmo arquivo de texto o gênero do manga e a sinopse
    def SinopGen():
        cont = len(genre)
        for c in range(cont):
            genres = genre[c]
            with open(f'{manga}/1#{manga}.txt', 'a', encoding='utf8')as file:
                file.write(f'{genres}, ')
        with open(f'{manga}/1#{manga}.txt', 'a', encoding='utf8') as file:
            file.write(f'\n\nSinopse: \n\n{sinopse}')

    # Faz o download da capa do mangá
    def capa():
        img_class = soupe.find('div', {'class': 'single-manga-bg'})
        img_class = re.findall(r'(https:[//\w\.-]+)', str(img_class))[0]
        binary_image = requests.get(f'{img_class}')
        file_image = Image.open(BytesIO(binary_image.content))
        image_object = file_image
        image_object.save(f'{manga}/{manga}.jpg')
    
    # def DownloadCap():
    #     count = 0
    #     caps_num = script_id['allposts'][0]['num']
    #     try:
    #         while True:
    #             # [::-1] inverte a ordem dos numeros ex: [3,2,1] para [1,2,3]
    #             caps = script_id['allposts'][::-1][count]['num']
    #             os.mkdir(f'{manga}/Capitulo-{caps}')
    #             for x in range(200):
    #                 binary_image = requests.get(f'https://cdn.mangayabu.top/mangas/{mg_name}/capitulo-{caps}/{x:02d}.jpg')
    #                 if binary_image.status_code == 404:
    #                     print(f'ok')
    #                     break
    #                 else:
    #                     file_image = Image.open(BytesIO(binary_image.content))
    #                     image_object = file_image
    #                     image_object.convert('RGB').save(f'{manga}/Capitulo-{caps}/Pagina-{x:02d}.jpg')
    #             if count == caps_num:
    #                 break
    #             count += 1
    #     except Exception as erro:
    #         if erro.__class__ == IndexError:
    #             print(f'CAPITULO-{caps} BAIXADO COM SUCESSO')
    #     else:
    #         print(f'CAPITULO-{caps} BAIXADO COM SUCESSO')


    # SinopGen()
    capa()
    # DownloadCap()
