Às vezes, ao programar, é necessário realizar a mesma operação ou quase a mesma operação algumas vezes.

Para evitar escrever a mesma coisa repetidamente, podemos usar **laços**.

O laço `for` tem a seguinte sintaxe:

```python
for i in range(start, end):  
  code
```

O `range(start, end)` determina qual é o valor de `start` e qual é o valor de `end`. O `i` receberá todos os valores de `start` até `end` (**não incluindo** `end`) sequencialmente. Por exemplo:

```python
for i in range(0, 5):   
 print(i)
```

Ele executará a instrução print 5 vezes:

```python
0
1
2
3
4
```

> Podemos simplificar o `range(0, 5)` para `range(5)`:
> 
> ```python
> for i in range(5):  
>   print(i)
> ```

Você também pode combinar `i` com outro texto usando uma **f-string**. Coloque um `f` antes da string e use `{i}` dentro dela para inserir o valor de `i`:

```python
for i in range(1, 4):    
	print(f"Item number: {i}")
```

Isso imprimirá:

```python
Item number: 1
Item number: 2
Item number: 3
```

Os laços têm muitos casos de uso. Por exemplo, vamos somar todos os números de 1 a 100:

```python
sum_numbers = 0
for i in range(1, 101):    
	sum_numbers += iprint(sum_numbers)
```

Isso primeiro percorrerá todos os números entre 1 e 101 (não incluindo 101) e somará todos eles. Depois, imprimirá a variável `sum_numbers`.

Ou seja, o for em Python pode percorrer uma lista
Uma coisa que é muito confusa em Python é o for percorrer as letras de uma string mas as strings são basicamente uma lista de caracteres (então cada caracter será percorrido), percorre qualquer qualquer iterável
