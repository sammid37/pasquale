# Construção de Compiladores I 
# Pasquale Compiler - Utilitário
# Enthony e Samantha

import spacy
import random
from tokens import Tokens
from typing import List
from nltk.corpus import wordnet
from termcolor import colored


# TODO: mover funções de modificações(que estão no sintático) para esta classe
# Objetivo: limpeza de código

class TextModifier:
  def __init__(self):
    self.nlp = spacy.load("pt_core_news_sm")
    self.synonyms = {
        'NOUN': {},
        'ADJ': {},
        'VERB': {},
        'ADV': {}
    }
    
  # FIXME: analisar
  def get_synonyms(self, word:str, pos:str):
    synonyms = []
    if pos in ['NOUN', 'ADJ', 'VERB', 'ADV']:  # Verifica se a classe gramatical está na lista desejada
      for syn in wordnet.synsets(word, lang='por'):
        for lemma in syn.lemmas("por"):
          # Comparação direta com a classe gramatical
          if lemma.synset().pos() == pos[0].lower():  
            synonyms.append(lemma.name())

    return list(set(synonyms))
  
  def modify_with_synonyms(self, tokenized_words:Tokens):
    """Método 1: criar nova frase a partir da original, 
    mas substituindo palavras por sinônimos"""
    modified_words = []
    
    for w in tokenized_words:
      # Verifica se há sinônimos disponíveis antes de escolher aleatoriamente
      if w.grammar in self.synonyms and self.synonyms[w.grammar] and self.synonyms[w.grammar][w.word]:
        new_word = random.choice(self.synonyms[w.grammar][w.word.lower()])
        modified_words.append(new_word)
        self.sorted_synonyms[w.grammar] = new_word
        print(f"Palavra salva: {self.sorted_synonyms[w.grammar]}")
      else:
        modified_words.append(w.word)
        self.sorted_synonyms[w.grammar] = w.word
        print(f"Palavra original: {self.sorted_synonyms[w.grammar]}")
    print(f"M1: {type(modified_words)}")
    return modified_words

  def modify_change_order(self, tokenized_words:Tokens):
    """Método 2: criar nova frase a partir da original,
    mas modificando a ordem das palavras"""
    subjects = []
    verb = None
    objects = []
    adjective = []
    adverb = []

    print(type(tokenized_words))

    # Iteramos sobre os tokens da sentença
    for w in tokenized_words:
      print(colored(f"Palavra atual: {w.word}({w.grammar})", "green"))
      if w.grammar in ["DET", "NOUN", "PROPN"]:
        # Se o token for um determinante, adjetivo, substantivo ou pronome próprio,
        # adicionamos sua palavra (em minúsculas) aos sujeitos
        subjects.append(w.word.lower())
      elif w.grammar == "VERB":
        verb = w.word
      elif w.grammar == "ADJ":
        adjective.append(w.word)
      elif w.grammar == "ADV":
        adverb.append(w.word)
      elif w.grammar not in ["VERB", "ADJ", "ADV", "NOUN"]:
        # Se o token for uma conjunção coordenativa, preposição ou pronome,
        # adicionamos sua palavra à lista de objetos
        objects.append(w.word)

    # Montamos a sentença modificada juntando o verbo (com a primeira letra em maiúscula),
    # os sujeitos (em minúsculas), os adjetivos, os advérbios e os objetos diretos, se houver
    modified_sentence = " ".join([verb.capitalize()] + subjects)
    if adjective:
      modified_sentence += " " + " ".join(adjective)
    if adverb:
      modified_sentence += " " + " ".join(adverb)
    if objects:
      modified_sentence += " " + " ".join(objects)

    print(f"M2: {type(modified_sentence)}")
    return modified_sentence

  def modify_with_synonyms_and_change_order(self):
    """Método 3: criar nova frase a partir da original, 
    mas substituindo palavras por sinônimos e trocando a ordem delas"""

    print(type(self.sorted_synonyms))

    for x in self.sorted_synonyms:
      print(self.sorted_synonyms[x]) 

    # modified_sentence = self.modify_change_order(self.sorted_synonyms)
    # print(f"M3: {type(modified_sentence)}")
    
    # return modified_sentence

  def analyze_and_modify(self, text):
    tokenized_words = []
    doc = self.nlp(text)
    for p in doc:
      tokenized_words.append(Tokens(p.text, p.pos_))
      if p.pos_ not in ['NOUN', 'ADJ', 'VERB', 'ADV']:
        continue
      else:
        synonyms = self.get_synonyms(p.text, p.pos_)
        self.synonyms[p.pos_][p.text.lower()] = synonyms
    return tokenized_words

# Testando os métodos
text = "O gato arranhou a porta grande."
text_modifier = TextModifier()
# Obter sinônimos da frase


words_in_text = text_modifier.analyze_and_modify(text)

print(f"Texto Modificado com Sinônimos: {text_modifier.modify_with_synonyms(words_in_text)}")
print(f"Texto Modificado Alterando a Ordem: {(text_modifier.modify_change_order(words_in_text))}")
print(f"Texto Modificado com Sinônimos e Alterando a Ordem: {text_modifier.modify_with_synonyms_and_change_order()}")