import json
import multiprocessing
from time import time
from keywords import search_keywords;

if __name__ == '__main__':
  with open('datos.json') as file:
    data = json.load(file)

    start_time = time()

    pool = multiprocessing.Pool(processes=4)
    keywords_categories = pool.map(search_keywords, data['text'])
    data['keywords'] = keywords_categories

    elapsed_time = time() - start_time

    print("Tiempo Paralelo: %0.10f segundos." % elapsed_time)
  
    with open('datos.json', 'w') as f:
      json.dump(data, f, indent= 4)
    

