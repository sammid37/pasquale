import nltk
from nltk.corpus import wordnet
from tokens import Tokens
import random

# É necessário fazer o download do corpus do WordNet da NLTK caso não tenha feito ainda
nltk.download('wordnet')

def sortear_palavras(frase):
    # Lista para armazenar as palavras sorteadas
    palavras_sorteadas = []
    
    # Definir as classes gramaticais que queremos sortear (substantivos, advérbios e adjetivos)
    classes_gramaticais = {'NOUN', 'ADV', 'ADJ'}
    
    # Iterar sobre as palavras da frase
    for palavra, classe_gramatical in frase:
        # Verificar se a classe gramatical da palavra está na lista de classes que queremos sortear
        if classe_gramatical in classes_gramaticais:
            # Adicionar a palavra à lista de palavras sorteadas
            palavras_sorteadas.append(palavra)
    
    return palavras_sorteadas

def obter_sinonimos(palavras):
    # Lista para armazenar os sinônimos
    sinonimos = []
    
    # Iterar sobre as palavras
    for palavra in palavras:
        # Obter a synset (conjunto de sinônimos) da palavra
        synsets = wordnet.synsets(palavra, lang='por')
        
        # Verificar se há synsets para a palavra
        if synsets:
            # Obter os sinônimos do primeiro synset (poderíamos escolher aleatoriamente também)
            syn = synsets[0]
            sinonimos_palavra = syn.lemmas(lang='por')
            sinonimos_palavra = [s.name() for s in sinonimos_palavra]
            
            # Adicionar os sinônimos à lista
            sinonimos.append((palavra, sinonimos_palavra))
        else:
            # Se não houver sinônimos, adicionar a própria palavra à lista
            sinonimos.append((palavra, [palavra]))
    
    return sinonimos

def sortear_sinonimos(sinonimos):
    # Lista para armazenar as palavras com seus sinônimos sorteados
    palavras_sorteadas = []
    
    # Iterar sobre as palavras e seus sinônimos
    for palavra, lista_sinonimos in sinonimos:
        # Sortear aleatoriamente um sinônimo da lista de sinônimos
        sinonimo_sorteado = random.choice(lista_sinonimos)
        
        # Adicionar a palavra e o sinônimo sorteado à lista
        palavras_sorteadas.append((palavra, sinonimo_sorteado))
    
    return palavras_sorteadas

# Frase de exemplo (lista de tokens)
frase_exemplo = [
    Tokens(word='casa',grammar='NOUN'),
    Tokens(word='bonita',grammar='ADJ'),
    Tokens(word='correu',grammar='VERB'),
    Tokens(word='rapidamente',grammar='ADV')
]

# Sortear palavras
palavras_sorteadas = sortear_palavras(frase_exemplo)
print("Palavras sorteadas:", palavras_sorteadas)

# Obter sinônimos
sinonimos = obter_sinonimos(palavras_sorteadas)
print("Sinônimos:", sinonimos)

# Sortear sinônimos
palavras_sorteadas_com_sinonimos = sortear_sinonimos(sinonimos)
print("Palavras com sinônimos sorteados:", palavras_sorteadas_com_sinonimos)
