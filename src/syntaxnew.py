# from nltk import CFG, ChartParser #ORININAL222222
# from nltk.tree import Tree
# from termcolor import colored

# class SyntaxNew:
#     def __init__(self):
#         self.tokens = []

#     def my_grammar(self):
#         return CFG.fromstring(
#             """Texto -> Sentenca PONTUACAO_FINAL | Sentenca PONTUACAO_FINAL Texto
#             Sentenca -> SintagmaNominal SintagmaVerbal | SintagmaVerbal SintagmaNominal | SintagmaNominal | SintagmaNominal SintagmaVerbal SintagmaNominal | SintagmaVerbal SintagmaNominal | SintagmaVerbal | SintagmaNominal SintagmaVerbal Conjuncao SintagmaNominal SintagmaVerbal | SintagmaNominal
#             SintagmaNominal -> Determinante Substantivo | Determinante Substantivo Adjetivo | Pronome | Determinante SubstantivoProprio | Determinante SubstantivoProprio Adjetivo | Determinante SubstantivoProprio Conjuncao Determinante SubstantivoProprio | Determinante Substantivo Conjuncao Determinante Substantivo | Preposicao Substantivo | Preposicao SubstantivoProprio | SubstantivoProprio
#             SintagmaVerbal -> Verbo | Verbo Adjetivo | Verbo Adverbio | Verbo SintagmaNominal-ComplementoVerbal | Verbo Substantivo Numeral |  Verbo SintagmaNominal-ComplementoVerbal | Verbo SintagmaNominal-ComplementoVerbal Preposicao Substantivo Adverbio | Verbo SintagmaNominal Preposicao Determinante Substantivo | Verbo SintagmaNominal Preposicao Determinante Substantivo Adjetivo | Adverbio Verbo SintagmaNominal Preposicao Substantivo | Verbo SintagmaNominal-ComplementoVerbal | Verbo SintagmaNominal-ComplementoVerbal SintagmaNominal
#             SintagmaNominal-ComplementoVerbal -> Determinante Substantivo | Determinante Substantivo Adjetivo | Pronome | Determinante SubstantivoProprio | Preposicao Determinante Substantivo | Preposicao Determinante SubstantivoProprio
#             Determinante -> 'DET'
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
#             PONTUACAO_FINAL -> 'PUNCT'""")

#     def display_tree(self, parser, token_list):
#         for tree in parser.parse(token_list):
#             print(tree)
#             tree.pretty_print()
#             return tree

#     def find_subject(self, tree):
#         for subtree in tree.subtrees(lambda t: t.label() == 'SintagmaNominal'):
#             return ' '.join(subtree.leaves())

#     def find_predicate(self, tree):
#         for subtree in tree.subtrees(lambda t: t.label() == 'SintagmaVerbal'):
#             return ' '.join(subtree.leaves())

#     def find_verbal_complement(self, tree):
#         for subtree in tree.subtrees(lambda t: t.label() == 'SintagmaNominal-ComplementoVerbal'):
#             return ' '.join(subtree.leaves())

#     def execute(self, tokens):
#         self.tokens = tokens
#         grammar = self.my_grammar()
#         parser = ChartParser(grammar)
#         grammar_list = [token.grammar for token in self.tokens]
#         word_list = [token.word for token in self.tokens]
#         # É possível associar a lista de gramática com a lista de palavras umas que ambas tem o mesmo tamanho? Quero que poder exibir a palavra junto com o a posição de valor de grmática na lista.


#         # É possível ver na árvore qual a posição do elemento da lista grammar_list que ele está gerando? 
#         print(len(grammar_list) == len(word_list)) # deve retornr true!!
#         print(len(grammar_list))
#         print(len(word_list))

#         print("Ordem das classes gramaticais:")
#         for token, grammar_class in zip([token.word for token in self.tokens], grammar_list):
#             print(f"{token} ({grammar_class})")

#         tree = self.display_tree(parser, grammar_list)
#         if tree:
#             print(colored("✅ Análise sintática concluída!", "green"))
#             sujeito = self.find_subject(tree)
#             predicado = self.find_predicate(tree)
#             complemento_verbal = self.find_verbal_complement(tree)

#             print(f"\nSujeito: {sujeito}")
#             print(f"Predicado: {predicado}")
#             print(f"Objeto direto: {complemento_verbal}")

#             return True
#         else:
#             print(colored("⚠ Análise sintática finalizada com erro.", "red"))
#             return False
    #TODO Try Catch para capturar exceções de análise sintática


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# from nltk import CFG, ChartParser MAIS COMPLETO ATE O MOMENTO.
# from termcolor import colored

# class SyntaxNew:
#     def __init__(self):
#         self.tokens = []

#     def my_grammar(self):
#         return CFG.fromstring(
#             """Texto -> Sentenca PONTUACAO_FINAL | Sentenca PONTUACAO_FINAL Texto
#             Sentenca -> SintagmaNominal SintagmaVerbal | SintagmaVerbal SintagmaNominal | SintagmaNominal | SintagmaNominal SintagmaVerbal SintagmaNominal | SintagmaVerbal SintagmaNominal | SintagmaVerbal | SintagmaNominal SintagmaVerbal Conjuncao SintagmaNominal SintagmaVerbal | SintagmaNominal
#             SintagmaNominal -> Determinante Substantivo | Determinante Substantivo Adjetivo | Pronome | Determinante SubstantivoProprio | Determinante SubstantivoProprio Adjetivo | Determinante SubstantivoProprio Conjuncao Determinante SubstantivoProprio | Determinante Substantivo Conjuncao Determinante Substantivo | SintagmaNominal-ComplementoVerbal | Preposicao SubstantivoProprio | SubstantivoProprio
#             SintagmaVerbal -> Verbo | Verbo Adjetivo | Verbo Adverbio | Verbo SintagmaNominal-ComplementoVerbal | Verbo Substantivo Numeral |  Verbo SintagmaNominal-ComplementoVerbal | Verbo SintagmaNominal-ComplementoVerbal SintagmaNominal-ComplementoVerbal Adverbio | Verbo SintagmaNominal Preposicao Determinante Substantivo | Verbo SintagmaNominal Preposicao Determinante Substantivo Adjetivo | Adverbio Verbo SintagmaNominal Preposicao Substantivo | Verbo SintagmaNominal-ComplementoVerbal | Verbo SintagmaNominal-ComplementoVerbal SintagmaNominal
#             SintagmaNominal-ComplementoVerbal -> Determinante Substantivo | Determinante Substantivo Adjetivo | Pronome | Determinante SubstantivoProprio | Preposicao Determinante Substantivo | Preposicao Determinante SubstantivoProprio | Preposicao Substantivo
#             Determinante -> 'DET'
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
#             PONTUACAO_FINAL -> 'PUNCT'""")

#     def display_tree(self, parser, token_list):
#         for tree in parser.parse(token_list):
#             print(tree)
#             tree.pretty_print()
#             return tree

#     def find_subject(self, word_list, grammar_list):
#         subject = ""
#         found_det = False
#         found_pron = False
#         for word, grammar in zip(word_list, grammar_list):
#             if grammar == 'DET' and not found_det and not found_pron:
#                 subject += word + " "
#                 found_det = True
#             elif grammar == 'PRON' and not found_det and not found_pron:
#                 subject += word + " "
#                 found_pron = True
#             elif grammar in ['NOUN', 'PROPN'] and (found_det or found_pron):
#                 subject += word + " "
#                 break  # Stop adding to the subject after the first noun is found
#         return subject.strip()

#     def find_predicate(self, word_list, grammar_list):
#         found_verb = False
#         predicate = []
#         for word, grammar in zip(word_list, grammar_list):
#             if grammar == 'VERB':
#                 found_verb = True
#             if found_verb and grammar != 'PUNCT':
#                 predicate.append(word)
#         return ' '.join(predicate)

#     def find_verbal_complement(self, word_list, grammar_list):
#         found_verb = False
#         object_words = []
#         for word, grammar in zip(word_list, grammar_list):
#             if grammar == 'VERB':
#                 found_verb = True
#             if found_verb and grammar in ['DET', 'NOUN', 'PROPN', 'ADJ'] and word != '.':
#                 object_words.append(word)
#         return ' '.join(object_words)

#     def execute(self, tokens):
#         self.tokens = tokens
#         grammar_list = [token.grammar for token in self.tokens]
#         word_list = [token.word for token in self.tokens]

#         grammar = self.my_grammar()
#         parser = ChartParser(grammar)

#         print("Ordem das classes gramaticais:")
#         for token, grammar_class in zip(word_list, grammar_list):
#             print(f"{token} ({grammar_class})")

#         tree = self.display_tree(parser, grammar_list)
#         if tree:
#             print(colored("✅ Análise sintática concluída!", "green"))
#             sujeito = self.find_subject(word_list, grammar_list)
#             predicado = self.find_predicate(word_list, grammar_list)
#             complemento_verbal = self.find_verbal_complement(word_list, grammar_list)

#             print(f"\nSujeito: {sujeito}")
#             print(f"Predicado: {predicado}")
#             print(f"Complemento Verbal: {complemento_verbal}")
#             return True
#         else:
#             print(colored("⚠ Análise sintática finalizada com erro.", "red"))
#             return False

from nltk import CFG, ChartParser
from termcolor import colored

class SyntaxNew:
    def __init__(self):
        self.tokens = []

    def my_grammar(self):
        return CFG.fromstring(
            """Texto -> Sentenca PONTUACAO_FINAL | Sentenca PONTUACAO_FINAL Texto
            Sentenca -> SintagmaNominal SintagmaVerbal | SintagmaVerbal SintagmaNominal | SintagmaNominal | SintagmaNominal SintagmaVerbal SintagmaNominal | SintagmaVerbal SintagmaNominal | SintagmaVerbal | SintagmaNominal SintagmaVerbal Conjuncao SintagmaNominal SintagmaVerbal | SintagmaNominal
            SintagmaNominal -> Determinante Substantivo | Determinante Substantivo Adjetivo | Pronome | Determinante SubstantivoProprio | Determinante SubstantivoProprio Adjetivo | Determinante SubstantivoProprio Conjuncao Determinante SubstantivoProprio | Determinante Substantivo Conjuncao Determinante Substantivo | SintagmaNominal-ComplementoVerbal | Preposicao SubstantivoProprio | SubstantivoProprio
            SintagmaVerbal -> Verbo | Verbo Adjetivo | Verbo Adverbio | Verbo SintagmaNominal-ComplementoVerbal | Verbo Substantivo Numeral |  Verbo SintagmaNominal-ComplementoVerbal | Verbo SintagmaNominal-ComplementoVerbal SintagmaNominal-ComplementoVerbal Adverbio | Verbo SintagmaNominal Preposicao Determinante Substantivo | Verbo SintagmaNominal Preposicao Determinante Substantivo Adjetivo | Adverbio Verbo SintagmaNominal Preposicao Substantivo | Verbo SintagmaNominal-ComplementoVerbal | Verbo SintagmaNominal-ComplementoVerbal SintagmaNominal
            SintagmaNominal-ComplementoVerbal -> Determinante Substantivo | Determinante Substantivo Adjetivo | Pronome | Determinante SubstantivoProprio | Preposicao Determinante Substantivo | Preposicao Determinante SubstantivoProprio | Preposicao Substantivo | Preposicao Substantivo Adjetivo
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
            PONTUACAO_FINAL -> 'PUNCT'""")

    def display_tree(self, parser, token_list):
        for tree in parser.parse(token_list):
            print(tree)
            tree.pretty_print()
            return tree

    def find_subject(self, word_list, grammar_list):
        subject = ""
        found_det = False
        found_pron = False
        for word, grammar in zip(word_list, grammar_list):
            if grammar == 'DET' and not found_det and not found_pron:
                subject += word + " "
                found_det = True
            elif grammar == 'PRON' and not found_det and not found_pron:
                subject += word + " "
                found_pron = True
            elif grammar in ['NOUN', 'PROPN'] and (found_det or found_pron):
                subject += word + " "
                break  # Stop adding to the subject after the first noun is found
        return subject.strip()

    def find_predicate(self, word_list, grammar_list):
        found_verb = False
        predicate = []
        for word, grammar in zip(word_list, grammar_list):
            if grammar == 'VERB' or grammar == 'AUX' or (grammar == 'AUX' and 'VERB' in grammar_list):
                found_verb = True
            if found_verb and grammar != 'PUNCT':
                predicate.append(word)
        return ' '.join(predicate)

    def find_verbal_complement(self, word_list, grammar_list):
        found_verb = False
        object_words = []
        for word, grammar in zip(word_list, grammar_list):
            if grammar == 'VERB' or grammar == 'AUX' or (grammar == 'AUX' and 'VERB' in grammar_list):
                found_verb = True
            if found_verb and grammar != 'PUNCT':
                if grammar in ['DET','ADP','NOUN', 'PROPN', 'ADJ']:
                    object_words.append(word)
                elif grammar == 'ADP' and object_words:
                    object_words[-1] += " " + word
        return ' '.join(object_words)

    def reverse_sentence(self, sujeito, predicado, verbo, complemento_verbal):
        # Converte todas as palavras para minúsculas
        sujeito = sujeito.lower()
        predicado = predicado.lower()
        verbo = verbo.lower()
        complemento_verbal = complemento_verbal.lower()

        # Forma passiva do verbo
        verbo_passivo = f"foi {self.get_participle(verbo)}"

        # Adiciona a preposição "por" antes do sujeito
        sujeito_com_preposicao = f"pela {sujeito}"

        # Forma a nova sentença
        nova_sentenca = f"{complemento_verbal} {verbo_passivo} {sujeito_com_preposicao}".capitalize()
        return nova_sentenca

    def get_participle(self, verb):
        # Aqui você precisa definir a conjugação para o particípio de cada verbo que deseja suportar
        # Isso é apenas um exemplo
        participle = {
            "comeu": "comido",
            "beber": "bebido",
            "fazer": "feito"
            # Adicione outros verbos conforme necessário
        }
        return participle.get(verb, verb + "ido")  # Default to verb + "ido" if not found

    def execute(self, tokens):
        self.tokens = tokens
        grammar_list = [token.grammar for token in self.tokens]
        word_list = [token.word for token in self.tokens]

        grammar = self.my_grammar()
        parser = ChartParser(grammar)

        print("Ordem das classes gramaticais:")
        for token, grammar_class in zip(word_list, grammar_list):
            print(f"{token} ({grammar_class})")

        tree = self.display_tree(parser, grammar_list)
        if tree:
            print(colored("✅ Análise sintática concluída!", "green"))
            sujeito = self.find_subject(word_list, grammar_list)
            predicado = self.find_predicate(word_list, grammar_list)
            complemento_verbal = self.find_verbal_complement(word_list, grammar_list)

            print(f"\nSujeito: {sujeito}")
            print(f"Predicado: {predicado}")
            if 'AUX' in grammar_list:
                print(f"Auxiliar: {word_list[grammar_list.index('AUX')]}")
            print(f"Verbo: {word_list[grammar_list.index('VERB')]}")
            print(f"Complemento Verbal: {complemento_verbal}")
            print("\nFrase Reordenada:")
            print(self.reverse_sentence(sujeito, predicado, word_list[grammar_list.index('VERB')], complemento_verbal))
            return True
        else:
            print(colored("⚠ Análise sintática finalizada com erro.", "red"))
            return False

