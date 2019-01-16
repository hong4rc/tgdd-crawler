from api import getAllRating, getRating, getProductList
import json
from utils import save

def crawlCategory(category):
  products = getProductList(category)
  if len(products) == 0:
    print(category, 'is not exist!!!')
    return
  save(products, 'data', 'category_' + str(category) + '.json')
  for product in products:
    id = product['id']
    print(id, 'crawling...')
    pData = getAllRating(id)
    save(pData, 'data/category_' + str(category), 'product_' + str(id) + '.json')

MAX_CATEGORY = 200
i = 0
while i < MAX_CATEGORY:
  crawlCategory(i)
  i += 1
