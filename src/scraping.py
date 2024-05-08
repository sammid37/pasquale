from typing import List
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

RESULT_STATS = "result-stats"
ARTICLE_SESSION = "N54PNb BToiNc cvP2Ce"
SEARCH_TTL = 20

class ElementosNaoEncontradosException(Exception):
  def __init__(self, message="Os elementos não foram encontrados"):
    self.message = message
    super().__init__(self.message)

class Scraping:
  def __init__(self, queries:List[str]) -> None:
    self.queries = queries
    self.qtd_query_results = []
    self.snippets_results = {}  # dicionário para armazenar a lista de snippets de uma query
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')  # Define o nível de log para "SEVERE"
    self.driver = webdriver.Chrome(options=chrome_options)    

  def display_snippets(self) -> None:
    """Realiza a impressão da query(claim) e seus respectivos snippets 
    acompanhando da quantidade total de resultados encontrados
    do claim pesquisado"""
    print(colored("🔎 Resultado da consulta", "blue"))
    for q, r in self.snippets_results.items():
      print(colored(f"Query: ", "blue"), end="")
      print(f"\"{q}\"")
      for snippet in r.values():
        print(snippet)
    print()
      # table_data = [
      #     ["Quantidade de resultados:", r["quantidade_resultados"]],
      #     # TODO: futura implementação referente a exibição de snippets
      # ]
      # print(tabulate.tabulate(table_data, tablefmt="fancy"))

  def do_searches(self) -> None:
    """Realiza a busca no Google e retorna a quantidade de resultados totais."""
    for q in self.queries:
      snippets = []
      try:
        self.driver.get("https://www.google.com/search?q=\"" + q + "\"")

        wait = WebDriverWait(self.driver, SEARCH_TTL) # tempo limite para a busca
        
        el_qtd_results = wait.until(EC.presence_of_element_located((By.ID, RESULT_STATS)))
        self.qtd_query_results.append(el_qtd_results.text)

        # TODO: futura implementação de incluir trechos que contém o claim 
        #  el_snippets_with_query = self.driver.find_elements(By.CSS_SELECTOR, ".N54PNb.BToiNc")
        # for el_snippet_with_query in el_snippets_with_query:
        #   snippets.append(el_snippet_with_query.text)

        self.snippets_results[q] = {
            "quantidade_resultados": el_qtd_results.text,
            # "snippets": snippets
        }
      except NoSuchElementException as e:
        print(colored(f"Elemento não encontrado para a consulta '{q}': {e}"))

    self.driver.quit()