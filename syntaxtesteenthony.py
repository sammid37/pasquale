# Construção de Compiladores 
# Pasquale Compiler - Análise Sintática
# Enthony e Samantha

# Construção de Compiladores 
# Pasquale Compiler - Análise Sintática
# Enthony e Samantha

import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser
from nltk.tokenize import word_tokenize

class Syntax:
    def __init__(self):
        # Definindo a gramática
        self.grammar = CFG.fromstring("""
            Texto -> Sentenca '.' | Sentenca '.' Texto
            Sentenca -> SintagmaNominal SintagmaVerbal
            SintagmaNominal -> Substantivo | Artigo Substantivo
            SintagmaVerbal -> Verbo | Verbo SintagmaVerbal
            Artigo -> 'o' | 'a' | 'os' | 'as'| 'um' | 'uma' | 'uns' | 'umas'
            Substantivo -> 'gato' | 'cachorro' | 'pássaro' 
            Verbo -> 'corre' | 'voa' | 'late'
        """)
        self.parser = RecursiveDescentParser(self.grammar)

    def execute(self, tokens):
        # Parse da frase
        parsed = self.parse_sentence(tokens)

        if parsed:
            print("Frase válida!")
        else:
            print("Frase inválida!")

    def parse_sentence(self, tokens):
        # Transforma os tokens em uma lista de palavras
        words = [token.word.lower() for token in tokens]

        # Parse da frase
        try:
            parsed = list(self.parser.parse(words))
            return parsed
        except ValueError as e:
            print("Erro de parsing:", e)
            return None

if __name__ == "__main__":
    from lexer import Lexer

    # Frase digitada pelo usuário
    input_phrase = input("Digite uma frase: ")

    # Chamada do Léxico
    lexer = Lexer()
    lexer.set_phares(input_phrase)
    tokens = lexer.execute()

    # Chamada do Sintático
    syntax_analyzer = Syntax()
    syntax_analyzer.execute(tokens)



# import nltk
# from nltk import CFG
# from nltk.parse import RecursiveDescentParser
# from nltk.tokenize import word_tokenize

# class Syntax:
#     def __init__(self):
#         # Definindo a gramática
#         self.grammar = CFG.fromstring("""
#             Texto -> Sentenca PONTUACAO_FINAL | Sentenca PONTUACAO_FINAL Texto
#             Sentenca -> SintagmaNominal SintagmaVerbal
#             SintagmaNominal -> Artigo Substantivo
#             SintagmaVerbal -> Verbo
#             Artigo -> 'DET'
#             Substantivo -> 'NOUN'
#             Verbo -> 'VERB'
#             PONTUACAO_FINAL -> 'PUNCT'
#         """)
#         self.parser = RecursiveDescentParser(self.grammar)

#     def execute(self, tokens):
#         # Parse da frase
#         parsed = self.parse_sentence(tokens)

#         if parsed:
#             print("Frase válida!")
#         else:
#             print("Frase inválida!")

#     def parse_sentence(self, tokens):
#         # Transforma os tokens em uma lista de palavras
#         words = [self.map_grammar(token.grammar) for token in tokens]

#         # Parse da frase
#         try:
#             parsed = list(self.parser.parse(words))
#             return parsed
#         except ValueError as e:
#             print("Erro de parsing:", e)
#             return None

#     def map_grammar(self, tag):
#         if tag == 'DET':
#             return 'Artigo'
#         elif tag == 'NOUN':
#             return 'Substantivo'
#         elif tag == 'VERB':
#             return 'Verbo'
#         elif tag == 'PUNCT':
#             return 'PONTUACAO_FINAL'
#         else:
#             return tag