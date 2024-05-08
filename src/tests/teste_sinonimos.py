# Construção de Compiladores I 
# Pasquale Compiler - Teste para obter sinônimos
# Enthony e Samantha

import spacy
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')

# Carregar modelo em português
nlp = spacy.load("pt_core_news_sm")

# Função para obter sinônimos de uma palavra
def get_synonyms(word):
  synonyms = []
  for syn in wordnet.synsets(word,lang='por'):
    for lemma in syn.lemmas(lang='por'):
      synonyms.append(lemma.name())
  return synonyms

# Exemplo de uso
lista_palavras = ["cantou", "linda"]

for palavra in lista_palavras:
  synonyms = get_synonyms(palavra)
  print("Sinônimos de", palavra + ":", synonyms)
