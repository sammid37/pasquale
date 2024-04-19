# Rascunho

import spacy
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')

# Carregar modelo em português
nlp = spacy.load("pt_core_news_sm")

# Processar texto
texto = "Um gato preto está sobre a mesa."
doc = nlp(texto)

lista_tokens = []
# Iterar sobre as palavras do texto
for token in doc:
  # print(token.text, token.pos_)
  lista_tokens.append((token.text,token.pos_))

print(lista_tokens)

# Função para obter sinônimos de uma palavra
def get_synonyms(word):
  synonyms = []
  for syn in wordnet.synsets(word,lang='por'):
    for lemma in syn.lemmas(lang='por'):
      synonyms.append(lemma.name())
  return synonyms

# Exemplo de uso
word = "feliz"
synonyms = get_synonyms(word)
print("Sinônimos de", word + ":", synonyms)

import random

def reorder_sentence(sentence):
  # Divide a frase em uma lista de palavras
  words = sentence.split()

  # Embaralha a ordem das palavras
  random.shuffle(words)

  # Reconstrói a frase com as palavras reordenadas
  reordered_sentence = ' '.join(words)

  return reordered_sentence

# Exemplo de uso
original_sentence = "O gato preto está sobre a mesa."
reordered_sentence = reorder_sentence(original_sentence)
print("Frase original:", original_sentence)
print("Frase reordenada:", reordered_sentence)
