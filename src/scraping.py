import tabulate
from typing import List
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
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

class Scrapping:
  def __init__(self, queries:List[str]) -> None:
    self.queries = queries
    self.qtd_query_results = []
    self.snippets_results = {} # dicionário para armazenar a lista de snippets de uma query
    self.driver = webdriver.Chrome()

  def display_qtd_results(results:List[str]) -> None:
    print("Quantidade de resultados para as queries:")
    for r in results:
      print(r)

  # TODO: futura implementação referente a exibição de snippets
  def display_snippets(results: dict) -> None:
    """Realiza a impressão da query(claim) e seus respectivos snippets 
    acompanhando da quantidade total de resultados encontrados
    do claim pesquisado"""
    print(colored("Resultado da consulta", "magenta"))
    for q, r in results.items():
      print(f"\n**Consulta:** {q}")
      table_data = [
          ["Quantidade de resultados:", r["quantidade_resultados"]],
          ["Snippets:", r["snippets"]]
      ]
      print(tabulate.tabulate(table_data, tablefmt="fancy"))

  def do_searches(self) -> List[str]:
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

        # self.snippets_results[q] = {
        #     "quantidade_resultados": el_qtd_results.text,
        #     "snippets": snippets
        # }
      except NoSuchElementException as e:
        print(colored(f"Elemento não encontrado para a consulta '{q}': {e}"))

    self.driver.quit()
    return self.qtd_query_results

# Exemplo de uso
scraper = Scrapping(["Filme que marca o centenário da Disney", "Ash finalmente ganha a liga pokemon."])
print(scraper.queries)
queries_result = scraper.do_searches()