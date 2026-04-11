### Sistema adaptativo de Saneamento de Dados (SASD)
- Criar próprio conjunto de dados brutos (com imperfeições) 
- Resultado final: DataFrame de Pandas (para integração de NumPy e Scikit-Learn)
#### Fase 1 - Fundamentos e extração
- Remover caracteres indesejados, normalizar e fatiar (slice)
- Coleção de dados:
	- Listas para coisas temporários (alteráveis)
	- Tuplas para registros imutáveis
	- Conjuntos para eliminar duplicatas
	- Dicionário para mapeamento chave-valor
	- Lógico de fluxo: For, while, if, elif, else para filtrar dados inválidos e descartar registros irrelevantes 
	- Tirar números
#### Fase 2 - Fundamentos e extração
- Não ter arquivos extensos
- Tratamentos de exceções: try/except e usar raise
- Funções lambda (processamento funcional): map (valor total da compra, calcular_total) e filter ()
	- return sum(map(lambda item: precos.get(item, 0), lista_compras)): O total de uma compra. O map vai percorrer cada item da lista_compras (lista que vai entrar como parametro), e pegar (get) o preço do item em precos (parametro passado para ser o dicionario produto: preco), item,0 atribui o valor 0 para o item que não tiver preço, o map vai basicamente pegar os preços, o lambda percorrer a lista de itens e preços e o sum vai somar todos os preços que o map retornou (resumindo: a função lambda (anônima) tenta buscar o preço do item no dicionário precos e soma todos os precos)
	- return list(filter(lambda item: item not in nao_essenciais, lista)): O filter vai percorrer a lista (parametro) e verifica se o item não está na lista nao_essenciais (parametro), se o item não estiver em 'não essenciais' ele permanece na lista e se ele estiver será removido
- Função para gerar dataframes: 
	- df = pd.DataFrame(lista, columns=\['Produto']): Cria uma coluna chamada Produto usando os itens da lista (parametro da função) 
	- df\['Preço'] = df\['Produto'].map(precos): o map vai olhar cada nome na coluna produto e vai ao dicionario preços e pega o valor correspondente 
	- print(f"Total: R${df\['Preço'].sum():.2f}"): Soma todos os preços da coluna 
- Tratamentos de erros:
	- O usuario digita quanto tem de dinheiro - > valida a compra original - > compra sem não essenciais -> erro final (se não passar em nenhuma validação)
	- se usuario digitar um valor inválido (tipo letras) o programa retorna um valueError
	- float(input(...)): Tenta converter a entrada do usuario para float
	- o primeiro try tenta criar um dataframe e calcular o total da compra 
	- o segundo tenta ver se o dinheiro de entrada (que o usuario tem) é suficiente para realizar a compra (por meio de um if) (retorna 'Compra realizada com sucesso!') e se não tiver a quantidade retorna um erro 'Dinheiro insuficiente na primeira tentativa' 
	- já no 

- OBSERVAÇÕES: 
	- Adicionar um item em uma lista é append()
	- Capitalize() deixa a primeira letra maiuscula
	- Strip() tira espaços
	- Para formatar uma lista ou conjunto tem que percorrer item por item e colocar o método (só daria para colocar o método direto se fosse só uma string)
	- Módulo: Unidade de código independente e reutilizável com uma tarefa específica. Agrupamento de funcionalidades relacionadas a um componente de um software
	- Lista: \[\]
	- tupla: ()
	- conjunto: set (nome_lista)
	- isdigit(): se é numero
	- .get()


- 

-