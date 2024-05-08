# Construção de Compiladores I 
# Pasquale Compiler - Arquivo Principal
# Enthony e Samantha

import re
import os

import sys
sys.path.append('src')

from lexer import Lexer
from scraping import Scraping
from syntaxnew import SyntaxNew
from termcolor import colored

if __name__ == "__main__":
    print(colored("Pasquale Compiler", "blue"))
    print(colored("Compilador da Língua Portuguesa\n", "blue"))

    while True:
        lexer_output = "src/output/lexer_output.csv"
        input_phrase = input("Digite a frase a ser analisada (ou 'sair' para encerrar): ")

        if input_phrase.lower() == "sair":
            break

        # Chamada do Léxico
        print(input_phrase)
        lexer = Lexer()
        lexer.set_phares(input_phrase)
        lexer.set_output_file(lexer_output)
        tokens = lexer.execute()

        print("Resultado da tokenização: ")
        for token in tokens:
            print(token.word, token.grammar)

        # Chamada do Sintático
        syntax_analyzer = SyntaxNew()
        syntax_result = syntax_analyzer.execute(tokens)

        # Caso o sintático tenha retornado as frases modifcadas, realiza busca
        if syntax_result:
            queries = syntax_result 
            queries.append(input_phrase)
      
            # Disparar requisições da frase original e novas queries para o Google
            scraper = Scraping(queries)
            queries_result = scraper.do_searches()
            scraper.display_snippets()