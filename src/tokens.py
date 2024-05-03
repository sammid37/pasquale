# Construção de Compiladores I 
# Pasquale Compiler - Representação de Tokens
# Enthony e Samantha

class Tokens:
  def __init__(self, word, grammar):
    self.word = word
    self.grammar = grammar

  def __iter__(self):
    return iter(self.tokens)