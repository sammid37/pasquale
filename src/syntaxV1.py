# Construção de Compiladores I 
# Pasquale Compiler - Análise Sintática
# Enthony e Samantha

import csv

from termcolor import colored 

class Syntax:
    def __init__(self):
        self.tokens = []
        self.position = 0

    def t_word(self):
        """Retorna a palavra/valor de um token."""
        if self.position < len(self.tokens):
            return self.tokens[self.position].word
        else:
            return None

    def t_grammar_class(self):
        """Retorna a classe gramatical de um token."""
        if self.position < len(self.tokens):
            return self.tokens[self.position].grammar
        else:
            return None

    def next_word(self, grammar_class):
        """Avança para a próxima palavra."""
        if self.t_grammar_class() == grammar_class:
            self.position += 1
            return True
        else:
            return False

    # Regras sintáticas
    def r_texto(self):
        while True:
            self.r_sentenca()
            if self.t_word() == ".":
                print("Análise sintática concluída com sucesso!")
                break
            elif self.t_word() == ",":
                self.position += 1
            else:
                print(colored("Erro sintático: esperava '.', mas foi encontrado '{}'.", "red").format(self.t_word()))
                break

    def r_sentenca(self):
        self.r_sintagma_nominal()
        if self.t_grammar_class() == "VERB":
            self.r_sintagma_verbal()
        if self.t_grammar_class() == "CCONJ":
            print("Conjunção encontrada:", self.t_word())
            self.next_word("CCONJ")
            self.r_sentenca()

    def r_sintagma_nominal(self):
        if self.t_grammar_class() in ["NOUN", "PROPN"]:
            print("Substantivo encontrado:", self.t_word())
            self.next_word(self.t_grammar_class())
            if self.t_grammar_class() == "NOUN":
                print("Substantivo composto encontrado:", self.t_word())
                self.next_word("NOUN")
        elif self.t_grammar_class() == "DET":
            self.next_word("DET")
            if self.t_grammar_class() in ["NOUN", "PROPN"]:
                print("Artigo encontrado:", self.tokens[self.position - 1].word)
                print("Substantivo encontrado:", self.t_word())
                self.next_word(self.t_grammar_class())
                if self.t_grammar_class() == "ADJ":
                    print("Adjetivo encontrado:", self.t_word())
                    self.next_word("ADJ")
            else:
                print(colored("Erro sintático: esperava um substantivo após o artigo.", "red"))
        elif self.t_grammar_class() == "PRON":
            print("Pronome encontrado:", self.t_word())
            self.next_word("PRON")
        else:
            print(colored("Erro sintático: esperava um artigo, substantivo, adjetivo ou pronome.", "red"))

    def r_sintagma_verbal(self):
        if self.t_grammar_class() == "VERB":
            print("Verbo encontrado:", self.t_word())
            next_word = self.t_word()
            self.next_word("VERB")
            if self.t_grammar_class() == "VERB":
                next_word += " " + self.t_word()
                print("Locução verbal encontrada:", next_word)
                self.next_word("VERB")
            if self.t_grammar_class() == "ADV":
                print("Modificador verbal encontrado:", self.t_word())
                self.next_word("ADV")
            self.r_sintagma_objeto()
        else:
            print(colored("Erro sintático: esperava um verbo.", "red"))

    def r_sintagma_objeto(self):
        if self.t_grammar_class() in ["NOUN", "PROPN"]:
            print("Objeto direto encontrado:", self.t_word())
            self.next_word(self.t_grammar_class())
            if self.t_grammar_class() == "NOUN":
                print("Substantivo composto encontrado:", self.t_word())
                self.next_word("NOUN")
        elif self.t_grammar_class() == "DET":
            self.next_word("DET")
            if self.t_grammar_class() in ["NOUN", "PROPN"]:
                print("Artigo encontrado:", self.tokens[self.position - 1].word)
                print("Objeto direto encontrado:", self.t_word())
                self.next_word(self.t_grammar_class())
            else:
                print(colored("Erro sintático: esperava um substantivo após o artigo.", "red"))
        elif self.t_grammar_class() == "PRON":
            print("Pronome encontrado:", self.t_word())
            self.next_word("PRON")
        elif self.t_grammar_class() is None:
            pass  # Não há objeto direto, tudo bem
        else:
            print(colored("Erro sintático: esperava um objeto direto.", "red"))

    def modify_sentence(self):
        """Modifica a sentença de forma a reordenar as palavras"""
        subjects = []  # Aqui armazenamos os sujeitos da sentença
        verb = None    # Aqui armazenamos o verbo da sentença
        objects = []   # Aqui armazenamos os objetos diretos da sentença
        adjective = [] # Aqui armazenamos os adjetivos da sentença
        adverb = []    # Aqui armazenamos os advérbios da sentença

        # Iteramos sobre os tokens da sentença
        for token in self.tokens:
            if token.grammar in ["DET", "ADJ", "NOUN", "PROPN"]:
                # Se o token for um determinante, adjetivo, substantivo ou pronome próprio,
                # adicionamos sua palavra (em minúsculas) aos sujeitos
                subjects.append(token.word.lower())
            elif token.grammar == "VERB":
                # Se o token for um verbo, armazenamos sua palavra
                verb = token.word
            elif token.grammar == "ADJ":
                # Se o token for um adjetivo, armazenamos sua palavra
                adjective.append(token.word)
            elif token.grammar == "ADV":
                # Se o token for um advérbio, armazenamos sua palavra
                adverb.append(token.word)
            elif token.grammar in ["CCONJ", "ADP", "PRON"]:
                # Se o token for uma conjunção coordenativa, preposição ou pronome,
                # adicionamos sua palavra à lista de objetos
                objects.append(token.word)

        # Montamos a sentença modificada juntando o verbo (com a primeira letra em maiúscula),
        # os sujeitos (em minúsculas), os adjetivos, os advérbios e os objetos diretos, se houver
        modified_sentence = " ".join([verb.capitalize()] + subjects)
        if adjective:
            modified_sentence += " " + " ".join(adjective)
        if adverb:
            modified_sentence += " " + " ".join(adverb)
        if objects:
            modified_sentence += " " + " ".join(objects)
        return modified_sentence + "."

    def execute(self, tokens):
        """Realiza a análise sintática"""
        self.tokens = tokens
        print(colored("✅ Lexer", "green"))
        print(colored("🔍 Análise sintática iniciada...\n", "green"))
        self.r_texto()
        modified_sentence = self.modify_sentence()
        print("Sentença modificada:", modified_sentence)
        print(colored("🎉 Análise sintática concluída!", "green"))


# VERSAO ANTIGA

# class Syntax:
#     def __init__(self):
#         self.tokens = []
#         self.position = 0

#     def t_word(self):
#         """Retorna a palavra/valor de um token."""
#         if self.position < len(self.tokens):
#             return self.tokens[self.position].word
#         else:
#             return None

#     def t_grammar_class(self):
#         """Retorna a classe gramatical de um token."""
#         if self.position < len(self.tokens):
#             return self.tokens[self.position].grammar
#         else:
#             return None

#     def next_word(self, grammar_class):
#         """Avança para a próxima palavra."""
#         if self.t_grammar_class() == grammar_class: 
#             self.position += 1
#             return True
#         else:
#             return False

#     # Regras sintáticas
#     def r_texto(self):
#         while True:
#             self.r_sentenca()
#             if self.t_word() == ".":
#                 print("Análise sintática concluída com sucesso!")
#                 break
#             elif self.t_word() == ",":
#                 self.position += 1
#             else:
#                 print(colored("Erro sintático: esperava '.', mas foi encontrado '{}'.", "red").format(self.t_word()))
#                 break

#     def r_sentenca(self): 
#         self.r_sintagma_nominal()
#         if self.t_grammar_class() == "VERB":
#             self.r_sintagma_verbal()
#         if self.t_grammar_class() == "CCONJ":
#             print("Conjunção encontrada:", self.t_word())
#             self.next_word("CCONJ")
#             self.r_sentenca()

#     def r_sintagma_nominal(self): 
#         if self.t_grammar_class() in ["NOUN", "PROPN"]:
#             print("Substantivo encontrado:", self.t_word())
#             self.next_word(self.t_grammar_class())
#             if self.t_grammar_class() == "ADJ":
#                 print("Adjetivo encontrado:", self.t_word())
#                 self.next_word("ADJ")
#         elif self.t_grammar_class() == "DET":
#             self.next_word("DET")
#             if self.t_grammar_class() in ["NOUN", "PROPN"]:
#                 print("Artigo encontrado:", self.tokens[self.position - 1].word)
#                 print("Substantivo encontrado:", self.t_word())
#                 self.next_word(self.t_grammar_class())
#                 if self.t_grammar_class() == "ADJ":
#                     print("Adjetivo encontrado:", self.t_word())
#                     self.next_word("ADJ")
#             else:
#                 print(colored("Erro sintático: esperava um substantivo após o artigo.", "red"))
#         elif self.t_grammar_class() == "PRON":
#             print("Pronome encontrado:", self.t_word())
#             self.next_word("PRON")
#         else:
#             print(colored("Erro sintático: esperava um artigo, substantivo, adjetivo ou pronome.", "red"))

#     def r_sintagma_verbal(self):
#         if self.t_grammar_class() == "VERB":
#             print("Verbo encontrado:", self.t_word())
#             self.next_word("VERB")
#             if self.t_grammar_class() == "ADJ":
#                 print("Adjetivo encontrado:", self.t_word())
#                 self.next_word("ADJ")
#             self.r_sintagma_objeto()
#             if self.t_grammar_class() == "VERB":
#                 print("Locução verbal encontrada:", self.tokens[self.position - 1].word, self.t_word())
#                 self.next_word("VERB")
#                 if self.t_grammar_class() == "ADJ":
#                     print("Adjetivo encontrado:", self.t_word())
#                     self.next_word("ADJ")
#                 self.r_sintagma_objeto()
#         else:
#             print(colored("Erro sintático: esperava um verbo.", "red"))

#     def r_sintagma_objeto(self):
#         if self.t_grammar_class() in ["NOUN", "PROPN"]:
#             print("Objeto direto encontrado:", self.t_word())
#             self.next_word(self.t_grammar_class())
#         elif self.t_grammar_class() == "DET":
#             self.next_word("DET")
#             if self.t_grammar_class() in ["NOUN", "PROPN"]:
#                 print("Artigo encontrado:", self.tokens[self.position - 1].word)
#                 print("Objeto direto encontrado:", self.t_word())
#                 self.next_word(self.t_grammar_class())
#             else:
#                 print(colored("Erro sintático: esperava um substantivo após o artigo.", "red"))
#         elif self.t_grammar_class() == "PRON":
#             print("Pronome encontrado:", self.t_word())
#             self.next_word("PRON")
#         elif self.t_grammar_class() is None:
#             pass  # Não há objeto direto, tudo bem
#         else:
#             print(colored("Erro sintático: esperava um objeto direto.", "red"))

#     def modify_sentence(self):
#         """Modifica a sentença de forma a reordenar as palavras"""
#         subjects = []  # Aqui armazenamos os sujeitos da sentença
#         verb = None    # Aqui armazenamos o verbo da sentença
#         objects = []   # Aqui armazenamos os objetos diretos da sentença
#         adjective = [] # Aqui armazenamos os adjetivos da sentença

#         # Iteramos sobre os tokens da sentença
#         for token in self.tokens:
#             if token.grammar in ["DET", "ADJ", "NOUN", "PROPN"]:
#                 # Se o token for um determinante, adjetivo, substantivo ou pronome próprio,
#                 # adicionamos sua palavra (em minúsculas) aos sujeitos
#                 subjects.append(token.word.lower())
#             elif token.grammar == "VERB":
#                 # Se o token for um verbo, armazenamos sua palavra
#                 verb = token.word
#             elif token.grammar == "ADJ":
#                 # Se o token for um adjetivo, armazenamos sua palavra
#                 adjective.append(token.word)
#             elif token.grammar in ["CCONJ", "ADP", "PRON", "ADV"]:
#                 # Se o token for uma conjunção coordenativa, preposição, pronome ou advérbio, 
#                 # adicionamos sua palavra à lista de objetos
#                 objects.append(token.word)

#         # Montamos a sentença modificada juntando o verbo (com a primeira letra em maiúscula),
#         # os sujeitos (em minúsculas), os adjetivos e os objetos diretos, se houver
#         modified_sentence = " ".join(subjects + [verb.capitalize()])
#         if adjective:
#             modified_sentence += " " + " ".join(adjective)
#         if objects:
#             modified_sentence += " " + " ".join(objects)
#         return modified_sentence + "."

#     def execute(self, tokens):
#         """Realiza a análise sintática"""
#         self.tokens = tokens
#         print(colored("✅ Lexer", "green"))
#         print(colored("🔍 Análise sintática iniciada...\n", "green"))
#         self.r_texto()
#         modified_sentence = self.modify_sentence()
#         print("Sentença modificada:", modified_sentence)
#         print(colored("🎉 Análise sintática concluída!", "green"))
