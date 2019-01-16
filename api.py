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
    print(i)
    i += 1
    data += arr
  print(len(data))
  return data
