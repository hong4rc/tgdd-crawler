from api import getAllRating, getAllAccessory, getProductList
import json
from utils import save

def saveCategory (cateId, data):
  save(data, 'data', 'category_' + str(cateId) + '.json')
  for product in data:
    id = product['id']
    print(id, 'crawling...')
    pData = getAllRating(id)
    save(pData, 'data/category_' + str(cateId), 'product_' + str(id) + '.json')

def crawlCategory(cateId):
  products = getProductList(cateId)
  if len(products) == 0:
    print(cateId, 'is not exist!!!')
    return
  saveCategory(cateId, products)

# save accessory to right cagotery
data = {}
for product in getAllAccessory():
  cateId = product['category']
  if not(cateId in data):
    data[cateId] = []
  data[cateId].append(product)

for cateId in data:
  saveCategory(cateId, data[cateId])

# todo: crawl list of category

MAX_CATEGORY = 8000
i = 0
while i < MAX_CATEGORY:
  crawlCategory(i)
  i += 1
