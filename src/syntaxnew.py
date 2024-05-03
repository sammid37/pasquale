from nltk import CFG, ChartParser
from nltk.tree import Tree

class SyntaxNew:
  def __init__(self):
    self.tokens = []

  def my_grammar(self):
    return CFG.fromstring("""
    Texto -> Sentenca PONTUACAO_FINAL | Sentenca PONTUACAO_FINAL Texto
    Sentenca -> Sujeito Predicado
    Sujeito -> Artigo Substantivo | Substantivo 
    Predicado -> Verbo                                           
    Artigo -> 'DET'
    Adjetivo -> 'ADJ'                     
    Substantivo -> 'NOUN'
    Verbo -> 'VERB'
    Adverbio -> 'ADV'
    PONTUACAO_FINAL -> 'PUNCT'
  """)

  def display_tree(self, parser, token_list):
    for tree in parser.parse(token_list):
      tree.pretty_print()
      return 1
    return 0

  def execute(self, tokens):
    self.tokens = tokens
    grammar = self.my_grammar()
    parser = ChartParser(grammar)
    grammar_list = [token.grammar for token in self.tokens]

    print("Ordem das classes gramaticiais: ")
    print(grammar_list)
    for tree in parser.parse(grammar_list):
      tree.pretty_print()
    # tree = self.display_tree(parser, grammar_list)
    # if tree:
    #   print("Análise sintática concluída!")
    # else:
    #   print("Análise sintática finalizada com erro.")