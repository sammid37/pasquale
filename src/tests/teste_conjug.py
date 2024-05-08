# Construção de Compiladores I 
# Pasquale Compiler - Teste de conjugação de verbos com a biblioteca verbecc
# Enthony e Samantha

from verbecc import Conjugator

import json
def printjson(c):
  print(json.dumps(c, indent=4, ensure_ascii=False))

# Não funciona.
cg = Conjugator(lang='pt')

printjson(cg.conjugate('ser'))