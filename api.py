import re
import requests
from pyquery import PyQuery as pq

__null__ = []

def __toData (a):
  return 0

def getRating(id, page):
  r = requests.post('https://www.thegioididong.com/aj/ProductV4/RatingCommentList/',
    data = {
      'productid': id,
      'page': page,
      'score': 0
    })
  arr = []
  if r.text == '':
    return __null__
  cr = pq(r.text)
  for elem in cr('.par'):
    res = {
      'id': elem.attrib['id'],
      'name': cr(elem).find('.rh span').text(),
      'start': len(cr(elem).find('.rc i.iconcom-txtstar')),
      'comment': cr(elem).find('.rc span+i').text(),
      'timestamp': cr(elem).find('.ra .cmtd').text()
    }
    arr.append(res)
  
  return arr

def getAllRating(id):
  i = 1
  data = []
  while True:
    arr = getRating(id, i)
    if arr == __null__:
      break
    i += 1
    data += arr
  return data

__super_max__ = 50000

idRex = r"\/Images\/[0-9]*\/(?P<id>[0-9]*)(?:\/)"
def getId (src):
  return re.search(idRex, src).group('id')

def getProductList(category):
  r = requests.post('https://www.thegioididong.com/aj/CategoryV5/Product',
    data = {
      'Category': category,
      'PageSize': __super_max__,
      'PageIndex': 0
    })
  arr = []
  cr = pq(r.text)
  for elem in cr('.homeproduct>li'):
    img = cr(elem).find('a img')[0]
    src = img.get('data-original') or img.get('src')
    res = {
      'id': getId(src),
      'name': cr(elem).find('h3').text(),
      'price': cr(elem).find('.price strong').text(),
      'fake_price': cr(elem).find('.price span').text(),
      'promo': cr(elem).find('.promo p').text(),
      'start': len(cr(elem).find('.ratingresult .icontgdd-ystar')),
    }
    arr.append(res)
  return arr
