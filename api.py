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

__super_max__ = 5000

idRex = r"\/Images\/(?P<cago>[0-9]*)\/(?P<id>[0-9]*)(?:\/)"
def getInfo (src):
  res = re.search(idRex, src)
  return {
    'id': res.group('id'),
    'cago': res.group('cago')
  }

def getProductList(category):
  r = requests.post('https://www.thegioididong.com/aj/CategoryV5/Product',
    data = {
      'Category': category,
      'PageSize': __super_max__,
      'PageIndex': 0
    })
  return formatProduct(r.text)

def getAllAccessory ():
  r = requests.post('https://www.thegioididong.com/aj/AccessoryV4/Product',
    data = {
      'Size': __super_max__,
      'Index': 0
    })
  return formatProduct(r.text)

def formatProduct (text):
  arr = []
  cr = pq(text)
  for elem in cr('ul:not(.emptystate)>li'):
    img = cr(elem).find('a img')[0]
    src = img.get('data-original') or img.get('src')
    info = getInfo(src)
    res = {
      'id': info['id'],
      'category': info['cago'],
      'name': cr(elem).find('h3').text(),
      'price': cr(elem).find('.price strong, img+strong').text(),
      'fake_price': cr(elem).find('strong+span').text(),
      'promo': cr(elem).find('.promo p').text(),
      'start': len(cr(elem).find('.ratingresult .icontgdd-ystar')),
    }
    arr.append(res)
  return arr
