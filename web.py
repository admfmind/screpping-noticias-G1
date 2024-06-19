# web screpoimg de notícias -> G1

#bibliotecas para instalar:
####requests
####bs4

import requests
from bs4 import BeautifulSoup

# cores
cor1 = "\033[30;44m" #azull
null = "\033[m"      # tirar cor

#meu headers:
with open("headers.txt", "r") as navegador:
    headers_eu = navegador.read()
headers = {"User-Agent":headers_eu}

# site G1 e BBC
link_G1 = "https://g1.globo.com/" # G1

#screpping G1
resposta_G1 = requests.get(link_G1, headers)
site_G1 = BeautifulSoup(resposta_G1.text, "html.parser")

#    dado
dados_G1 = site_G1.find("a", class_="gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext")

print(f"\n{cor1}NOTÍCIA G1\n")
#    extarir link
print("LINK: ",dados_G1["href"])
dados_href_G1 = dados_G1["href"]
print()
#    extrair texto da tag a
print("NOTÍCIA: ",dados_G1.get_text())
print()
#        extair dados do link da motícia
resposta_href_G1 = requests.get(dados_href_G1, headers)
href_G1 = BeautifulSoup(resposta_href_G1.text, "html.parser")

dado_href_G1 = href_G1.find("h2", class_="content-head__subtitle")
print(dado_href_G1.get_text())
print(null)
