from api import getAllRating, getRating, getProductList
import json
from utils import save

category = 42

products = getProductList(category)
save(products, 'data', 'category_' + str(category) + '.json')
for product in products:
  id = product['id']
  pData = getAllRating(id)
  save(pData, 'data/category_' + str(category), 'product_' + str(id) + '.json')
