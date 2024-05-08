from verbecc import Conjugator

import json
def printjson(c):
  print(json.dumps(c, indent=4, ensure_ascii=False))

cg = Conjugator(lang='pt')

printjson(cg.conjugate('ser'))