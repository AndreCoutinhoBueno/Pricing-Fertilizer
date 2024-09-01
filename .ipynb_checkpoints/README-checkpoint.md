# Precificar fertilizantes em estoque no Brasil  

Contrapõe a oferta e a demanda de fertilizantes, buscando quantificar vetores que incidem sobre o preço.  

Foco em grandes volumes.  

Em busca da maior precisão, paralelamente processa dados correlacionados com o consumo de fertilizantes, como a ocorrência de chuvas, ou as exportações de produtops agrícolas.  

Na atual fase, que é inicial, nos concetraremos apenas na [oferta](https://github.com/AndreCoutinhoBueno/Pricing-Fertilizer/blob/main/oferta/README.md). 


`
import requests
from bs4 import BeautifulSoup

# URL da página web que você quer extrair as imagens
url = 'https://anda.org.br/pesquisa_setorial/'

# Faz a requisição para obter o conteúdo da página
response = requests.get(url)
response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

# Analisa o conteúdo HTML da página
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra todas as tags <img> na página
imagens = soup.find_all('img')

# Lista para armazenar os URLs das imagens
urls_imagens = []

# Itera sobre as tags <img> e salva os URLs em uma lista
for img in imagens:
    url_imagem = img.get('src')
    if url_imagem:
        urls_imagens.append(url_imagem)

# Exibe os URLs das imagens
for i, url_imagem in enumerate(urls_imagens, 1):
    print(f"Imagem {i}: {url_imagem}")

# Se quiser, você pode salvar esses URLs em um arquivo .txt
with open('urls_imagens.txt', 'w') as file:
    for url_imagem in urls_imagens:
        file.write(f"{url_imagem}\n")

print("URLs das imagens foram salvos em 'urls_imagens.txt'.")
`