import random
from typing import List
from termcolor import colored
from nltk.corpus import wordnet
from nltk import CFG, ChartParser

class SyntaxNew:
    def __init__(self):
        self.tokens = []
        
    def my_grammar(self) -> CFG:
        """Definição da gramática utilizando NLTK"""
        return CFG.fromstring(
            """Texto -> Sentenca PONTUACAO_FINAL | Sentenca PONTUACAO_FINAL Texto
            Sentenca -> SintagmaNominal SintagmaVerbal | SintagmaVerbal SintagmaNominal | SintagmaNominal | SintagmaVerbal | SintagmaNominal SintagmaVerbal Conjuncao SintagmaNominal SintagmaVerbal | SintagmaVerbal SintagmaNominal Conjuncao SintagmaVerbal SintagmaNominal | SintagmaNominal SintagmaVerbal Conkunção SintagmaNominal SintagmaVerbal | SintagmaNominal SintagmaVerbal Conjuncao SintagmaVerbal | SintagmaNominal SintagmaVerbal Pronome SintagmaVerbal
            SintagmaNominal -> Determinante Substantivo | Determinante Substantivo Adjetivo | Pronome | Determinante SubstantivoProprio | Determinante SubstantivoProprio Adjetivo | Determinante SubstantivoProprio Conjuncao Determinante SubstantivoProprio | Determinante Substantivo Conjuncao Determinante Substantivo | Objeto | Preposicao SubstantivoProprio | SubstantivoProprio | Substantivo | Numeral Substantivo | Numeral Substantivo Adjetivo | Preposicao Substantivo | Determinante Numeral | Numeral | Determinante Substantivo Preposicao SustantivoProprio
            SintagmaVerbal -> Verbo | Verbo Adjetivo | Verbo Adverbio | Verbo Objeto | Verbo Substantivo Numeral |  Verbo Objeto | Verbo Objeto Objeto Adverbio | Verbo SintagmaNominal Preposicao Determinante Substantivo | Verbo SintagmaNominal Preposicao Determinante Substantivo Adjetivo | Adverbio Verbo SintagmaNominal Preposicao Substantivo | Verbo Objeto | Verbo Objeto SintagmaNominal | Verbo Adverbio Objeto | Adverbio Verbo Objeto
            Objeto -> SintagmaNominal
            Determinante -> 'DET'
            Substantivo -> 'NOUN'
            Pronome -> 'PRON'
            Adjetivo -> 'ADJ'
            Verbo -> 'VERB' | 'AUX' | 'AUX' 'VERB' | VerboNegacao
            VerboNegacao -> Adverbio Verbo
            Adverbio -> 'ADV'
            Preposicao -> 'ADP'
            Conjuncao -> 'CCONJ' | 'SCONJ'
            Numeral -> 'NUM'
            VerboAuxiliar -> 'AUX'
            SubstantivoProprio -> 'PROPN'
            PONTUACAO_FINAL -> 'PUNCT'""")
    
    def display_tree(self, parser, token_list) -> None:
        """Exibe a árvore sintática."""
        for tree in parser.parse(token_list):
            print(tree)
            tree.pretty_print()
            return tree

    def find_subject(self, word_list, grammar_list):
        """Encontra o sujeito de uma frase."""
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
        """Encontra o predicado de uma frase."""
        found_verb = False
        predicate = []
        for word, grammar in zip(word_list, grammar_list):
            if grammar == 'VERB' or grammar == 'AUX' or (grammar == 'AUX' and 'VERB' in grammar_list):
                found_verb = True
            if found_verb and grammar != 'PUNCT':
                predicate.append(word)
        return ' '.join(predicate)

    def find_verbal_complement(self, word_list, grammar_list):
        """Encontra o complemento verbal de uma frase."""
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

    def modify_with_voz_passiva(self, sujeito, predicado, verbo, complemento_verbal):
        """Retorna uma nova frase por meio da voz passiva."""
        # Converte todas as palavras para minúsculas
        sujeito = sujeito.lower()
        predicado = predicado.lower()
        verbo = verbo.lower()
        complemento_verbal = complemento_verbal.lower()
        # Forma passiva do verbo
        verbo_passivo = f"foi {self.get_participle(verbo)}"
        sujeito_list = sujeito.split()
        sujeito_list = [palavra.lower() for palavra in sujeito_list]
        palavras_a_remover = ['a', 'o', 'as', 'os', 'um', 'uma', 'uns', 'umas']

        for palavra in palavras_a_remover:
            if palavra in sujeito_list:
                sujeito_list.remove(palavra)
        sujeito = " ".join(sujeito_list)

        # Adiciona a preposição "por" antes do sujeito
        sujeito_com_preposicao = f"pela {sujeito}"

        new_sentence = f"{complemento_verbal} {verbo_passivo} {sujeito_com_preposicao}".capitalize()
        return new_sentence
  
    def modify_with_synonyms(self, word_list):
        """Retorna uma nova frase a partir da original substituindo algumas palavras por sinônimos."""
        modified_text = []
        for word in word_list:
            if word.isalpha() and word != "pelo":  # Verifica se a palavra é alfabética e não é "pelo"
                synonyms = wordnet.synsets(word, lang='por')
                if synonyms:
                    new_word = random.choice(synonyms).lemmas(lang='por')[0].name()
                    if new_word != word:
                        modified_text.append(new_word)
                        continue
            modified_text.append(word)
        return modified_text

    def get_participle(self, verb):
        """Define a conjugação para o particípio de cada verbo que deseja suportar"""
        # Aqui define a conjugação para o particípio de cada verbo que deseja suportar
        participle = {
        
            "ou": "ado",
            "eu": "ido",
            "iu": "ido",
            "ôs": "osta",
            "fez": "feito",
            
            
            # Adicione outros verbos conforme necessário
        }
        
        # Verifica o final do verbo e constrói o particípio correspondente
        for ending, part in participle.items():
            if verb.endswith(ending):
                return verb[:-len(ending)] + part
        
        # Retorna o particípio encontrado ou o próprio verbo
        return verb

    def execute(self, tokens):
        """Realiza a execução da análise sintática através de uma GLC e cria variações da frase caso a frase original seja aceita."""
        self.tokens = tokens
        list_of_sentences = [] # lista vazia para armazenar as frases modificadas e a original
        grammar_list = [token.grammar for token in self.tokens]
        word_list = [token.word for token in self.tokens]

        grammar = self.my_grammar()
        parser = ChartParser(grammar)

        print(colored(f"🌳 Gerando árvore sintática...","blue"))
        tree = self.display_tree(parser, grammar_list)
        if tree:
            print(colored("✅ Análise sintática concluída!", "green"))
            sujeito = self.find_subject(word_list, grammar_list)
            predicado = self.find_predicate(word_list, grammar_list)
            complemento_verbal = self.find_verbal_complement(word_list, grammar_list)

            # print(f"\nSujeito: {sujeito}")
            # print(f"Predicado: {predicado}")
            # if 'AUX' in grammar_list:
            #     print(f"Verbo Auxiliar: {word_list[grammar_list.index('AUX')]}")
            # if 'VERB' in grammar_list:
            #     print(f"Verbo: {word_list[grammar_list.index('VERB')]}")
            # if 'VERB' not in grammar_list:
            #     pass
            # print(f"Complemento: {complemento_verbal}")


            print(colored(f"✍️  Gerando variações da frase original...","blue"))

            modified_order_1 = []
            if 'VERB' in grammar_list:
                modified_order_1.append(self.modify_with_voz_passiva(sujeito, predicado, word_list[grammar_list.index('VERB')], complemento_verbal))
            else:
                modified_order_1.append(self.modify_with_voz_passiva(sujeito, predicado, word_list[grammar_list.index('AUX')], complemento_verbal))
            print(colored("* Texto modificado 1:", "blue"), ' '.join(modified_order_1[0].split()))

            # Método 2 de modificação (sinônimos)
            modified_text = self.modify_with_synonyms(word_list)
            if 'VERB' in grammar_list:
                modified_text[grammar_list.index('VERB')] = word_list[grammar_list.index('VERB')]
            else:
                modified_text[grammar_list.index('AUX')] = word_list[grammar_list.index('AUX')]
            modified_order_2 = ' '.join(modified_text)
            print(colored("* Texto modificado 2:", "blue"), modified_order_2)

            # Método 3, alteração da ordem das palavras (voz passiva e sinônimos)
            modified_order_3 = []
            if 'VERB' in grammar_list:
                modified_order_3.append(self.modify_with_voz_passiva(sujeito, predicado, word_list[grammar_list.index('VERB')], complemento_verbal))
            else:
                modified_order_3.append(self.modify_with_voz_passiva(sujeito, predicado, word_list[grammar_list.index('AUX')], complemento_verbal))
            modified_order_with_synonyms = self.modify_with_synonyms(modified_order_3[0].split())
            print(colored("* Texto modificado 3:", "blue"), ' '.join(modified_order_with_synonyms))

            # Lista com os resultados dos métodos
            list_of_sentences.append(' '.join(modified_order_1))
            list_of_sentences.append(modified_order_2)
            list_of_sentences.append(' '.join(modified_order_with_synonyms))

            return list_of_sentences

        else:
            print(colored("❌ Análise sintática finalizada com erro.", "red"))
            return False