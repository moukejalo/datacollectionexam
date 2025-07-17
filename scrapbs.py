# import des packages
import pandas as pd
from requests import get
from bs4 import BeautifulSoup as bs

baseUlr = "https://sn.coinafrique.com"

# fetch all the containers
def fetchData(url, page_count):
  containers_of_page = []
  for p in range(1, page_count + 1) :
    # récuperation du code html
    code_html = get(url + str(p))
    # stocker le code html dans un object beautifulsoup
    soup = bs(code_html.content, 'html.parser')
    # récupérer les containers
    containers = soup.find_all('div', class_ = 'col s6 m4 l3')
    containers_of_page.extend(containers)
    # print(len(containers_of_page))

  data = []
  for container in containers_of_page:
    try:
      nom = container.find('p', class_ = 'ad__card-description').find('a').text
      image_lien = baseUlr + container.find('a', class_ = 'card-image ad__card-image waves-block waves-light')['href']
      adresse = container.find('p', class_ = 'ad__card-location').find('span').text
      prix = container.find('p', class_ = 'ad__card-price').find('a').text.replace('Prix sur demande', '').replace(' ', '').replace('CFA', '')
      dic= {
        'nom':nom,
        'prix': prix,
        'adresse': adresse,
        'image_lien': image_lien
      }
      data.append(dic)
    except:
      pass

  df = pd.DataFrame(data)
  # print(df.head())
  return df
  # df.to_csv('data.csv', index=False)
    

# df_chiens = fetchData("https://sn.coinafrique.com/categorie/chiens?page=", 1)
# df_moutons = fetchData("https://sn.coinafrique.com/categorie/moutons?page=", 1)
# df_volailes = fetchData("https://sn.coinafrique.com/categorie/poules-lapins-et-pigeons?page=", 1)
# df_volailes.rename(columns={'nom': 'details'}, inplace=True)
# df_autres = fetchData("https://sn.coinafrique.com/categorie/autres-animaux?page=", 1)

# print(df_chiens.head())
# print(df_moutons.head())
# print(df_volailes.head())
# print(df_autres.head())

