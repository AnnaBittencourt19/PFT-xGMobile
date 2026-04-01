A função `range()` em Python gera uma sequência de números, que é comumente usada com laços `for` para repetir código um número específico de vezes.

Crie um range que começa em 0 e termina em 4:

```python
for i in range(5):  
	print(i)
```

Isso produzirá a saída:

```python
0
1
2
3
4
```

Você também pode especificar um valor inicial:

```python
for i in range(2, 6):
	print(i)
```

Isso produzirá a saída:

```python
2
3
4
5
```

E você pode especificar um valor de passo (incremento):

```python
for i in range(1, 10, 2):
	print(i)
```

Isso produzirá a saída:

```python
1
3
5
7
9
```

**Contando para Trás (Ordem Decrescente):**

Você também pode usar um valor de **passo negativo** para contar para trás. Ao usar um passo negativo, o valor inicial deve ser maior que o valor final:

```python
for i in range(10, 0, -1):
	print(i)
```

Isso produzirá a saída:

```python
10
9
8
7
6
5
4
3
2
1
```

Você também pode usar passos negativos maiores:

```python
for i in range(20, 9, -2):
	print(i)
```

Isso produzirá a saída:

```python
20
18
16
14
12
10
```

Observe que `10` está incluído na saída mesmo que o valor final seja `9`. Isso ocorre porque o valor final é **exclusivo** — o loop continua enquanto o valor atual for **maior que** o valor final. Como `10 > 9`, ele é impresso. O próximo passo seria `8`, que não é maior que `9`, então o loop para.

**Ponto Principal:** Ao usar um passo negativo, o valor inicial deve ser **maior que** o valor final. O valor final ainda é exclusivo (não incluído).

![](https://coddy.tech/icons/challenge-white.svg)

Desafio

Iniciante

Escreva um loop for que imprime números usando a função `range()`. Seu programa deve:

1. Ler três números como entrada: `start`, `end` e `step`
2. Usar um loop for com `range(start, end, step)` para imprimir todos os números de `start` até `end` (não incluindo `end`) com o incremento `step` dado
3. Imprimir cada número em uma nova linha

**Instruções:**

- O código de leitura de entrada já está fornecido
- Substitua o comentário pelo seu loop for
- Use `range(start, end, step)` no seu loop

- No range com step positivo analisa se o numero é menor que end, no negativo é se é maior
