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
	- o segundo try tenta ver se o dinheiro de entrada (que o usuario tem) é suficiente para realizar a compra (por meio de um if) (retorna 'Compra realizada com sucesso!') e se não tiver a quantidade retorna um erro 'Dinheiro insuficiente na primeira tentativa' 
	- já no except (do segundo try): Faz a remoção dos itens não essenciais (chama a função filtrar_nao_essenciais) e cria uma nova lista, depois chama a função calcular_total usando a nova_lista e o dicionario dos valores, após fazer isso tem um if/else onde se o novo_total continua sendo maior que o valor que o usuario tem retorna um erro "Mesmo após remover não essenciais dinheiro insuficiente! Necessário: R\${novo_total:.2f} Disponível: R\${dinheiro:.2f}" e caso o dinheiro seja suficiente cria um novo dataframe que se chama df_filtrado (sem os não essenciais e com o novo valor final)
### Fase 3 - Engenharia com POO 

- Classes: 
	- A classe SaneadorBase: Padroniza todos os saneadores (define o padrão), abstrata
		- ABC (Abstract Base Class), a classe herda de ABC e se torna uma classe abstrata
		- A classe SaneadorBase não é instanciada diretamente, ela é apenas um molde
		-  @abstractmethod indica que o método limpar é obrigatório para qualquer classe que herde de SaneadorBase
		- Garante que qualquer novo tipo de saneador de dados criado no futuro (por exemplo, um SaneadorFinanceiro) obrigatoriamente terá que implementar a sua própria versão do método limpar
	-  A classe SaneadorDados: Polimorfismo, SaneadorDados herda de SaneadorBase. SaneadorBase exige a implementação do método limpar, a classe SaneadorDados fornece a implementação real desse método, aplicando as regras de formatação 
		- \_init_: método construtor, executado quando o objeto é criado
		- limpar: obrigado pela classe abstrata, remove espaços (strip), coloca tudo em minusculo (lower) e coloca a primeira letra maiúscula (capitalize)
	- A classe ValidadorPreco: Descriptor (validar valores), o preço é administrado pela classe ValidadorPreco, ao declarar um valor para preco o codigo chama o \_set_(self, instance, value) e verifica se o valor é menor que 0 ou maior que 100 e retorna que deve ser entre 0 e 100 e se estiver válido salva o valor
- Métodos:
	- De instância (\_init_ e limpar), recebem self como primeiro parâmetro, operam sobre uma instância do objeto (o objeto faz algo com ele mesmo)
		- O \_init_ é o construtor, chamado quando criamos um novo objeto SaneadorDados(meus_dados)
	- Estático: 
		- @staticmethod não recebe self nem cls, independente, recebe uma lista de fora na classe, remover_numeros é estático 
			- remover_numeros: recebe uma lista e devolve outra
	 - De classe: 
		 - recebe cls (classe inteira)
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
	- Um objeto é uma instância da classe
		exemplo:
		```Python
		saneador = SaneadorDados([" Arroz ", "Feijão", "7", "Leite"])
		# Objeto = classe (Atributos)
		```
	- SaneadorBase: Classe mãe
	- SaneadorDados: Classe filha (herda limpar)
	- \_set_name_ : Descobre o nome do atributo 
	- \_get_: Lê

