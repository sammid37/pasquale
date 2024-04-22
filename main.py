# Construção de Compiladores 
# Arquivo principal 
# Enthony e Samantha

import os
import sys
import csv

sys.path.append('src')

from lexer import Lexer
from tokens import Tokens
# from syntax import Syntax
from termcolor import colored

def search(claim):
  # returna snippets
  pass

if __name__ == "__main__":
  print(colored("Pasquale Compiler","blue"))
  print(colored("Compilador da Língua Portuguesa\n","blue"))

  lexer_output = "src/output/lexer_output.csv"
  input_phrase = "O gato caiu da mesa assustado."
  alternative_phrase = "Assustado caiu o gato da mesa."

  # TODO: chamada do Léxico
  print(input_phrase)
  lexer = Lexer()
  lexer.set_phares(input_phrase)
  lexer.set_output_file(lexer_output)
  lexer.execute()

  os.makedirs(os.path.dirname(lexer_output), exist_ok=True)
  with open(lexer.grammar_file, 'a', newline='') as csvfile:
    fieldnames = ['Word', 'Grammar Class']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Cabeçalho do CSV
    for token in lexer.tokens:
      writer.writerow({
        'Word': token.word, 
        'Grammar Class': token.grammar, 
        # 'Line': token.line
      })

  # TODO: chamada do Sintático
  # TODO: disparar requisições da frase original e novas frases para o Google
  # TODO: exibir snippets a partir de claims