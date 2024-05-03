# Construção de Compiladores 
# Arquivo principal 
# Enthony e Samantha

import re
import os
import sys
import csv
import requests
# from bs4 import BeautifulSoup

sys.path.append('src')

from lexer import Lexer
from syntaxnew import SyntaxNew
from termcolor import colored

def search(claim):
    # retorna snippets
    pass

# def get_search_results(query):
#     """
#     Realiza requisição HTTP a página de pesquisa do buscador Google 
#     e extrai o trecho desejado do HTML referente a quantidade de
#     resultados encontrados contendo a query
#     """
#     # Construa a URL de pesquisa do Google com a consulta fornecida
#     url = f"https://www.google.com/search?q={query}"

#     # Faça a requisição HTTP para a URL
#     response = requests.get(url)

#     # Verifique se a requisição foi bem-sucedida
#     if response.status_code == 200:
#         # Use BeautifulSoup para analisar o HTML da página
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Encontre o elemento <div> com o id "result-stats"
#         result_stats_div = soup.find('div', {'id': 'result-stats'})

#         # Se o elemento for encontrado, extraia o texto dentro dele
#         if result_stats_div:
#             result_stats_text = result_stats_div.get_text()
#             # Use expressão regular para extrair o número de resultados
#             num_results = re.search(r'\d+', result_stats_text)
#             if num_results:
#                 print("Número de resultados:", num_results.group())
#             else:
#                 print("Número de resultados não encontrado.")
#         else:
#             print("Elemento <div id='result-stats'> não encontrado.")
#     else:
#         print("Erro ao fazer a requisição:", response.status_code)

if __name__ == "__main__":
    print(colored("Pasquale Compiler", "blue"))
    print(colored("Compilador da Língua Portuguesa\n", "blue"))

    lexer_output = "src/output/lexer_output.csv"
    input_phrase = "O gato morreu."
  
    # Chamada do Léxico
    print(input_phrase)
    lexer = Lexer()
    lexer.set_phares(input_phrase)
    lexer.set_output_file(lexer_output)
    tokens = lexer.execute()

    print("Ordem da tokenização: ")
    for token in tokens:
        print(token.word, token.grammar)


    # os.makedirs(os.path.dirname(lexer_output), exist_ok=True)
    # with open(lexer.grammar_file, 'a', newline='') as csvfile:
    #     fieldnames = ['Word', 'Grammar Class']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #     writer.writeheader()  # Cabeçalho do CSV
    #     for token in tokens:
    #         writer.writerow({
    #             'Word': token.word,
    #             'Grammar Class': token.grammar,
    #             # 'Line': token.line
    #         })

    # Chamada do Sintático
    
    
    syntax_analyzer = SyntaxNew()
    syntax_analyzer.execute(tokens)
  
    # Disparar requisições da frase original e novas frases para o Google
    # Exibir snippets a partir de claims  
    # frase = "mico+leão+dourado+está+em+extinção"
    # get_search_results(frase)