- Python é uma linguagem fortemente tipada ou seja não precisa declarar o tipo da variável (atribuição dinamica)
- Em Python não se usa chaves ( '{' '}' ) e sim tabulação para indicar que uma coisa está dentro de um if ou de um for por exemplo
- Não se usa ; 
### Comentários:
```Python
#Uma única linha
"""Multiplas linhas
Mais de uma linha comentada """
```
### Imprimir no terminal
```Python
print()
```
### Entrada de dados
```Python
tal_coisa = input("Digite tal coisa: ")

#O python entende que todos os inputs são strings então é preciso converter o tipo
#se for para o usuario entrar com um dado que é float:
altura = float(input("Digite sua altura: "))
#um inteiro:
idade = int(input("Idade: "))
```
### Operadores
- Os únicos que são diferentes de outras linguagens são:
	-  ** potência
	- / divisão
	- // divisão inteira (resultado inteiro na divisão)
- Operadores de comparação são iguais de outras linguagens
- Operadores lógicos são: and (&& em outras linguagens), or (|| em outras linguagens) e not (negação (! em outras linguagens))
### Estrutura do If / elif e else
```Python
nota = 7

if nota >= 9:
    print("Excelente")

elif nota >= 7:
    print("Bom")

else:
    print("Reprovado")
```
- Usasse ':' após a condição
- é pela tabulação que dizemos o que está dentro de um if ou não (até prefiro que não fica aquela chatice de ver se fechou a chaves kkkk)
### Estrutura while
```Python
x = 0
while x < 5:
    print(x)
    x += 1
#Executa enquanto x menor que 5
```
### Estrutura for
```Python
for i in range(5):
    print(i)
```
- Em Python é muito comum utilizar range no for, nesse caso ``i in range(5)`` significa que i vai de 0 até 4
	- Estrutura completa do range:
	```Python
	range(inicio, fim, passo)
	
	for i in range(2, 10, 2): #vai começar no 2 e vai até 9 (o ultimo numero não aparece) de 2 em 2
	    print(i)
	#print vai ser: 2, 4, 6, 8
	```
### Funções são definidas por:
```Python
def nome_funcao(parametros):
	oq ela vai fazer
	return ou sem return
```