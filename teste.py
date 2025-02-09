Python 3.12.9 (tags/v3.12.9:fdb8142, Feb  4 2025, 15:27:58) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================================ RESTART: Shell ================================
import csv
from datetime import datetime
from collections import defaultdict

class ProdutoDTO:
    def __init__(self, ativo, quantidade, preco, data, descricao, peso):
        self.ativo = ativo          # Booleano
        self.quantidade = quantidade # Inteiro
        self.preco = preco          # Float
        self.data = data            # String
        self.descricao = descricao  # String
        self.peso = peso            # Float

# Exemplo de dados
produtos = [
    ProdutoDTO(True, 100, 10.5, "2024-12-01", "Produto A", 1.5),
    ProdutoDTO(False, 50, 20.0, "2024-12-01", "Produto B", 2.0),
    ProdutoDTO(True, 200, 30.5, "2024-12-02", "Produto C", 3.5),
    ProdutoDTO(False, 30, 40.0, "2024-12-02", "Produto A", 4.0)
]

... def produto_to_list(produto):
...     return [produto.ativo, produto.quantidade, produto.preco, produto.data, produto.descricao, produto.peso]
... 
... def gerar_csv_dinamico(produtos, nome_arquivo):
...     # Converter a lista de objetos em uma lista de listas
...     lista_valores = [produto_to_list(produto) for produto in produtos]
... 
...     # Definir os títulos (nomes dos campos)
...     titulos = ["Ativo", "Quantidade", "Preco", "Data", "Descricao", "Peso"]
... 
...     with open(nome_arquivo, mode='w', newline='') as file:
...         writer = csv.writer(file)
...         writer.writerow(titulos)  # Escrever o cabeçalho
... 
...         # Escrever as linhas dos valores
...         for valores in lista_valores:
...             writer.writerow(valores)
...             # Debug print para verificar o que está sendo escrito
...             print(f"Escrevendo linha: {valores}")
... 
...     print(f"Arquivo CSV '{nome_arquivo}' gerado com sucesso!")
... 
... def gerar_csv_por_mes(produtos):
...     produtos_por_mes = defaultdict(list)
...     for produto in produtos:
...         mes = datetime.strptime(produto.data, '%Y-%m-%d').strftime('%Y-%m')
...         produtos_por_mes[mes].append(produto)
... 
...     for mes, items in produtos_por_mes.items():
...         gerar_csv_dinamico(items, f'produtos_{mes}.csv')
... 
... # Gerar o arquivo CSV com dados de produtos
... print("Gerando arquivo CSV por dia...")
... gerar_csv_dinamico(produtos, 'produtos.csv')
... 
... # Gerar o arquivo CSV agrupado por mês
... print("Gerando arquivos CSV por mês...")
... gerar_csv_por_mes(produtos)
