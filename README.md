markdown
# Gerador de Arquivos CSV de Produtos

Este projeto contém um script em Python que gera arquivos CSV a partir de uma lista de objetos `ProdutoDTO`. O script cria dois tipos de arquivos CSV: um com todos os dados dos produtos e outro conjunto de CSVs agrupados por mês.

## Estrutura da Classe ProdutoDTO

A classe `ProdutoDTO` possui os seguintes atributos:

- `ativo` (booleano): Indica se o produto está ativo.
- `quantidade` (inteiro): Quantidade do produto.
- `preco` (float): Preço do produto.
- `data` (string): Data em que o produto foi adicionado (no formato `YYYY-MM-DD`).
- `descricao` (string): Descrição do produto.
- `peso` (float): Peso do produto.

## Funcionalidades

### 1. Gerar CSV Dinâmico

A função `gerar_csv_dinamico` cria um arquivo CSV com todos os produtos fornecidos. O arquivo gerado possui as seguintes colunas:

- `Ativo`
- `Quantidade`
- `Preco`
- `Data`
- `Descricao`
- `Peso`

Exemplo de uso:

```python
# Gerar o arquivo CSV com dados de produtos
gerar_csv_dinamico(produtos, 'produtos.csv')
2. Gerar CSV por Mês
A função gerar_csv_por_mes agrupa os produtos por mês e gera um arquivo CSV separado para cada mês. O nome do arquivo segue o formato produtos_YYYY-MM.csv, onde YYYY é o ano e MM é o mês.

Exemplo de uso:

python
# Gerar arquivos CSV por mês
gerar_csv_por_mes(produtos)
Como Executar o Script
Certifique-se de ter o Python instalado em sua máquina.

Salve o código do script em um arquivo, por exemplo, gerar_csv.py.

Execute o script a partir do terminal ou prompt de comando:

sh
python gerar_csv.py
O script gerará um arquivo produtos.csv com todos os dados dos produtos e arquivos separados para cada mês (por exemplo, produtos_2024-12.csv).

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

