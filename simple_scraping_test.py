import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

link = "https://www.google.com/search?client=firefox-b-d&q=nvdc34"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
requisição = requests.get(link, headers=headers)
cont = 0
cotação = []
tempo = []
cotasATT = {}

while True:
    site = BeautifulSoup(requisição.text, "html.parser")
    value = site.find("span", class_="IsqQVc NprOob wT3VGc")
    value = value.get_text()

    cotação.append(value)
    tempo.append(datetime.now())
    print(cotação)

    cont += 1
    
    if cont == 20:
        cotasATT['NVDC34'] = cotação
        cotasATT['HORÁRIO'] = tempo
        print(cotasATT)
        cota_df = pd.DataFrame(cotasATT)
        print(cota_df)
        cota_df.to_excel('cota.xlsx', index = False)
        break
    else:
        time.sleep(600)
