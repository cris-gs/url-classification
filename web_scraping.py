import json
import multiprocessing
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from time import time

user_agent = {'User-agent':'Mozilla/5.0'}
data = pd.read_csv("URL_Dataset.csv")
page = {'link': [], 'text': []}
for i in data.iloc[:, 0]:
  page['link'].append(i)

def url2text(url):
  try: 
    page = requests.get(url, headers= user_agent) 
    html_code = page.content 
    soup = BeautifulSoup(html_code, "html.parser", from_encoding="iso-8859-1")
    tag = soup.body 
    texts = ''
    cont = 1;
    for string in tag.strings:
      texts = texts + string.replace("\n"," ") + " "
    texts = re.sub(r"[^a-zA-Z0-9 áéíóúÁÉÍÓÚ]","",texts)
    texts = re.sub(r"\s+"," ",texts)
    if(texts.strip() == ""):
      texts = "Invalid url"
    elif('404' in texts or 'Not Found' in texts):
      texts = "Invalid url"
    return texts
  except:
    return "Invalid url"

if __name__ == '__main__':
  start_time = time()

  pool = multiprocessing.Pool(processes=4)
  extract_text = pool.map(url2text, page['link'])
  page['text'] = extract_text

  elapsed_time = time() - start_time

  print("Tiempo Paralelo: %0.10f segundos." % elapsed_time)

  """ start_time2 = time()

  for i in data.iloc[:, 0]:
    url2text(i)

  elapsed_time2 = time() - start_time2

  print("Tiempo Secuencial: %0.10f segundos." % elapsed_time2) """

  with open('datos.json', 'w') as f:
    json.dump(page, f, indent= 4)
  
