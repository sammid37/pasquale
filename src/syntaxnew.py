from nltk import CFG, ChartParser
from nltk.tree import Tree
from termcolor import colored

class SyntaxNew:
  def __init__(self):
    self.tokens = []

  def my_grammar(self):
    return CFG.fromstring(
      """Texto -> Sentenca PONTUACAO_FINAL | Sentenca PONTUACAO_FINAL Texto
      Sentenca -> SintagmaNominal SintagmaVerbal | SintagmaVerbal SintagmaNominal | SintagmaNominal | SintagmaNominal SintagmaVerbal SintagmaNominal | SintagmaVerbal SintagmaNominal | SintagmaVerbal | SintagmaNominal SintagmaVerbal Conjuncao SintagmaNominal SintagmaVerbal | SintagmaNominal  
      SintagmaNominal -> Determinante Substantivo | Determinante Substantivo Adjetivo | Pronome | Determinante SubstantivoProprio | Determinante SubstantivoProprio Adjetivo | Determinante SubstantivoProprio Conjuncao Determinante SubstantivoProprio | Determinante Substantivo Conjuncao Determinante Substantivo | Preposicao Substantivo | Preposicao SubstantivoProprio | Determinante 
      SintagmaVerbal -> Verbo | SintagmaNominal | Verbo Adjetivo| Verbo Adverbio | Verbo Pronome | Verbo Substantivo Numeral | Verbo Determinante Substantivo Adjetivo | Verbo Determinante Substantivo Adjetivo Sintagma Nominal | Verbo Determinante Substantivo Preposicao Substantivo Averbio | Verbo SintagmaNominal Preposicao Determinante Substantivo | Verbo SintagmaNominal Preposicao Determinante Substantivo Adjetivo | Adverbio Verbo Determinante Substantivo Preposicao Substantivo 
      Determinante -> 'DET'
      Substantivo -> 'NOUN'
      Pronome -> 'PRON'
      Adjetivo -> 'ADJ'                     
      Verbo -> 'VERB' | 'AUX' | 'AUX' 'VERB'
      Adverbio -> 'ADV'
      Preposicao -> 'ADP'
      Conjuncao -> 'CCONJ'
      Interjeicao -> 'INTJ'
      Numeral -> 'NUM'
      VerboAuxiliar -> 'AUX'
      SubstantivoProprio -> 'PROPN'
      Numeral -> 'NUM'
      PONTUACAO_FINAL -> 'PUNCT'""")

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
    # for tree in parser.parse(grammar_list):
    #   tree.pretty_print()
    tree = self.display_tree(parser, grammar_list)
    if tree:
       print(colored("✅ Análise sintática concluída!", "green"))
    else:
        print(colored("⚠ Análise sintática finalizada com erro.","red"))
    #TODO Try Catch para capturar exceções de análise sintática






# Texto -> Sentenca PONTUACAO_FINAL TextoAux
#         TextoAux -> | Sentenca PONTUACAO_FINAL TextoAux
#         Sentenca -> SintagmaNominal SintagmaVerbal | SintagmaVerbal SintagmaNominal | SintagmaNominal SintagmaNominal | SintagmaNominal SintagmaVerbal SintagmaNominal | SintagmaVerbal SintagmaNominal SintagmaNominal  | SintagmaVerbal SintagmaNominal SintagmaNominal SintagmaNominal| SintagmaNominal SintagmaVerbal Conjuncao SintagmaNominal SintagmaVerbal
#         SintagmaNominal -> Substantivo SintagmaNominalAux | Artigo Substantivo SintagmaNominalAux | Pronome Substantivo SintagmaNominalAux | Pronome Adjetivo Substantivo SintagmaNominalAux | SubstantivoProprio SintagmaNominalAux | Preposicao SubstantivoProprio SintagmaNominalAux | Preposicao Substantivo SintagmaNominalAux | Preposicao Substantivo Preposicao Substantivo SintagmaNominalAux | Preposicao Substantivo Preposicao SubstantivoProprio SintagmaNominalAux | Preposicao Artigo Substantivo SintagmaNominalAux
#         SintagmaNominalAux -> | Adjetivo SintagmaNominalAux | Adjetivo Adjetivo SintagmaNominalAux
#         SintagmaVerbal -> Verbo SintagmaVerbalAux | VerboAuxiliar Verbo SintagmaVerbalAux
#         SintagmaVerbalAux -> | Adverbio SintagmaVerbalAux | Adjetivo SintagmaVerbalAux  | Adjetivo Adverbio SintagmaVerbalAux
#         Artigo -> 'DET'  
#         Substantivo -> 'NOUN'
#         Pronome -> 'PRON'
#         Adjetivo -> 'ADJ'
#         Verbo -> 'VERB' | 'AUX' 'VERB'
#         Adverbio -> 'ADV'
#         Preposicao -> 'ADP'
#         Conjuncao -> 'CCONJ'
#         Numeral -> 'NUM'
#         VerboAuxiliar -> 'AUX'  
#         SubstantivoProprio -> 'PROPN'
#         PONTUACAO_FINAL -> 'PUNCT'

# VERSAO ORIGINAL:

# Texto -> Sentenca PONTUACAO_FINAL | Sentenca PONTUACAO_FINAL Texto
#             Sentenca -> SintagmaNominal SintagmaVerbal | SintagmaVerbal SintagmaNominal | SintagmaNominal SintagmaNominal | SintagmaNominal SintagmaVerbal SintagmaNominal | SintagmaVerbal SintagmaNominal SintagmaNominal | SintagmaVerbal SintagmaNominal SintagmaNominal SintagmaNominal | SintagmaNominal SintagmaVerbal Conjuncao SintagmaNominal SintagmaVerbal
#             SintagmaNominal -> Substantivo | Artigo Substantivo | Pronome Substantivo | Substantivo Adjetivo | Pronome Adjetivo Substantivo | Substantivo Adjetivo Adjetivo | Pronome Adjetivo Adjetivo Substantivo | SubstantivoProprio | Preposicao SubstantivoProprio | Preposicao Substantivo | Preposicao Substantivo Preposicao Substantivo | Preposicao Substantivo Preposicao SubstantivoProprio | Preposicao Artigo Substantivo | 
#             SintagmaVerbal -> Verbo | Verbo Adverbio | Verbo Adjetivo | Verbo Adjetivo Adverbio | Verbo Adverbio Adjetivo | Verbo Adverbio Adjetivo Adverbio | VerboAuxiliar | VerboAuxiliar Verbo Adverbio | VerboAuxiliar Verbo Adjetivo | VerboAuxiliar Verbo  Adjetivo Adverbio | VerboAuxiliar Verbo Adverbio Adjetivo | VerboAuxiliar Verbo Adverbio Adjetivo Adverbio
#             Artigo -> 'DET'
#             Substantivo -> 'NOUN'
#             Pronome -> 'PRON'
#             Adjetivo -> 'ADJ'                     
#             Verbo -> 'VERB' | 'AUX' | 'AUX' 'VERB'
#             Adverbio -> 'ADV'
#             Preposicao -> 'ADP'
#             Conjuncao -> 'CCONJ'
#             Interjeicao -> 'INTJ'
#             Numeral -> 'NUM'
#             VerboAuxiliar -> 'AUX'
#             SubstantivoProprio -> 'PROPN'
#             PONTUACAO_FINAL -> 'PUNCT'
#   """)