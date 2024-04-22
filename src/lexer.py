# Construção de Compiladores I 
# Pasquale Compiler - Análise Léxica
# Enthony e Samantha

import os
import time
import nltk
import spacy

from tokens import Tokens
from termcolor import colored
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

# Limpando o terminal após exibir situação de download dos pacotes importados
time.sleep(2)
os.system('clear')  # clear -> Unix, cls -> Windows

class Lexer:
  def __init__(self):
    self.phrase = None
    self.grammar_file = None
    self.tokens = []

  def set_output_file(self, output_file):
    self.grammar_file = output_file

  def set_phares(self, phrase):
    self.phrase = phrase

  def execute(self):
    # TODO: chamada de método que re-organiza a frase
    # TODO: passar frases para a análise léxica
    try:
      nlp = spacy.load("pt_core_news_sm")
      doc = nlp(self.phrase)

      for w in doc:
        self.tokens.append(Tokens(w.text, w.pos_))
    except Exception as e:
      print(colored(e,"red"))
    print(colored("✅ Lexer","green"))
    return self.tokens
    