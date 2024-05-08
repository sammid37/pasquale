import random
from typing import List
from termcolor import colored
from nltk.corpus import wordnet
from nltk import CFG, ChartParser

class SyntaxNew:
    def __init__(self):
        self.tokens = []
        self.new_sentences = [] # armazena a frase original e suas variações

    def my_grammar(self):
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
    
    def get_new_sentences(self, list_of_sentences) -> List[str]:
        self.new_sentences = list_of_sentences
        return self.new_sentences

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

    def modify_voz_passiva(self, sujeito, predicado, verbo, complemento_verbal):
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
        #sujeito_com_preposicao = f"pela {sujeito}"
        # sujeito_sem_det = sujeito.split(' ', 1)[-1]  # Remove o determinante do sujeito
        sujeito_com_preposicao = f"pela {sujeito}"

        # Forma a nova sentença
        nova_sentenca = f"{complemento_verbal} {verbo_passivo} {sujeito_com_preposicao}".capitalize()
        return nova_sentenca

    def get_participle(self, verb):
        # Aqui define a conjugação para o particípio de cada verbo que deseja suportar
        participle = {
        
            "ou": "ado",
            "eu": "ido",
            "iu": "ido",
            "ôs": "osta",
            
            # Adicione outros verbos conforme necessário
        }
        
        # Verifica o final do verbo e constrói o particípio correspondente
        for ending, part in participle.items():
            if verb.endswith(ending):
                return verb[:-len(ending)] + part
        
        # Retorna o particípio encontrado ou o próprio verbo
        return verb

    def modify_with_synonyms(self, word_list):
        modified_text = []
        for word in word_list:
            if word.isalpha():
                synonyms = wordnet.synsets(word, lang='por')
                if synonyms:
                    new_word = random.choice(synonyms).lemmas(lang='por')[0].name()
                    if new_word != word:
                        modified_text.append(new_word)
                        continue
            modified_text.append(word)
        return modified_text

    def change_word_order(self, word_list):
        random.shuffle(word_list)
        return word_list

    def execute(self, tokens):
        self.tokens = tokens
        list_of_sentences = [] # lista vazia para armazenar as frases modificadas e a original
        grammar_list = [token.grammar for token in self.tokens]
        word_list = [token.word for token in self.tokens]

        grammar = self.my_grammar()
        parser = ChartParser(grammar)

        tree = self.display_tree(parser, grammar_list)
        if tree:
            print(colored("✅ Análise sintática concluída!", "green"))
            sujeito = self.find_subject(word_list, grammar_list)
            predicado = self.find_predicate(word_list, grammar_list)
            complemento_verbal = self.find_verbal_complement(word_list, grammar_list)

            print(f"\nSujeito: {sujeito}")
            print(f"Predicado: {predicado}")
            if 'AUX' in grammar_list:
                print(f"Verbo Auxiliar: {word_list[grammar_list.index('AUX')]}")
            if 'VERB' in grammar_list:
                print(f"Verbo: {word_list[grammar_list.index('VERB')]}")
            if 'VERB' not in grammar_list:
                pass
            print(f"Complemento: {complemento_verbal}")

            # Método 1 de modificação (voz passiva)
            print("\nMétodo 1 de modificação(voz passiva):")
            modified_order_1 = []
            if 'VERB' in grammar_list:
                modified_order_1.append(self.modify_voz_passiva(sujeito, predicado, word_list[grammar_list.index('VERB')], complemento_verbal))
            else:
                modified_order_1.append(self.modify_voz_passiva(sujeito, predicado, word_list[grammar_list.index('AUX')], complemento_verbal))
            print(colored("Texto modificado 1:", "yellow"), ' '.join(modified_order_1[0].split()))

            # Método 2 de modificação (sinônimos)
            print("\nMétodo 2 de modificação (sinônimos):")
            modified_text = self.modify_with_synonyms(word_list)
            if 'VERB' in grammar_list:
                modified_text[grammar_list.index('VERB')] = word_list[grammar_list.index('VERB')]
            else:
                modified_text[grammar_list.index('AUX')] = word_list[grammar_list.index('AUX')]
            modified_order_2 = ' '.join(modified_text)
            print(colored("Texto modificado 2:", "magenta"), modified_order_2)

            # Método 3, alteração da ordem das palavras (voz passiva e sinônimos)
            print("\nMétodo 3, alteração da ordem das palavras (voz passiva e sinônimos):")
            modified_order_3 = []
            if 'VERB' in grammar_list:
                modified_order_3.append(self.modify_voz_passiva(sujeito, predicado, word_list[grammar_list.index('VERB')], complemento_verbal))
            else:
                modified_order_3.append(self.modify_voz_passiva(sujeito, predicado, word_list[grammar_list.index('AUX')], complemento_verbal))
            modified_order_with_synonyms = self.modify_with_synonyms(modified_order_3[0].split())
            print(colored("Texto modificado 3:", "blue"), ' '.join(modified_order_with_synonyms))

            # Lista com os resultados dos métodos
            list_of_sentences.append(' '.join(modified_order_1))
            list_of_sentences.append(modified_order_2)
            list_of_sentences.append(' '.join(modified_order_with_synonyms))
            print (list_of_sentences)
            return list_of_sentences

        else:
            print(colored("⚠ Análise sintática finalizada com erro.", "red"))
            return False