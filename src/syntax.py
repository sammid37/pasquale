# Construção de Compiladores I 
# Pasquale Compiler - Análise Sintática
# Enthony e Samantha

from termcolor import colored

# FIXME
class Syntax:
  def __init__(self, tokens):
    self.tokens = tokens
    self.position = 0
    pass

  def t_word(self):
    """Retorna a palavra/valor de um token."""
    return self.tokens[self.posicao].word
  
  def t_grammar_class(self):
    """Retorna a classe gramatical de um token."""
    return self.tokens[self.posicao].grammar
  
  def next_word(self, grammar_class):
    """Avança para a próxima palavra."""
    if self.c_class() == grammar_class: 
      self.position += 1

  # TODO: implementação dos métodos/regras sintáticas
  def r_text(self):
    if self.t_word() == ".":
      print("Análise sintática concluída com sucesso!")
    else:
      print(colored("Erro sintático: esperava '.', mas foi encontrado x.", "red"))
    pass

  def r_sentenca(self):
    pass

  def r_substantivo(self): 
    pass

  def r_s_nominal(self):
    pass

  def r_s_verbal(self):
    pass

  def r_artigo(self):
    pass

  # TODO: implementar a execução do analisador sintático
  def execute():
    # recebe conjunto de frases (claim e suas variações) e passa pelo parsing
    pass
