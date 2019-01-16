import os, errno, json

def save(obj, dir, name):
  mkdir(dir)
  file = open(os.path.join(dir, name), 'wb')
  output = json.dumps(obj, indent=2, ensure_ascii=False).encode('utf8')
  file.write(output)
  file.close()

def mkdir(dir):
  try:
    os.makedirs(dir)
  except OSError as e:
    if e.errno != errno.EEXIST:
      raise
