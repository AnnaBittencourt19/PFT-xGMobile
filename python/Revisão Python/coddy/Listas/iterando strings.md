Iterando sobre Strings Parte 1

Semelhante a listas, você pode iterar sobre strings:

```python
text = "Hey"
for char in text:
    print(char)
```

Saída:

```python
H
e
y
```

Usando o índice:

```python
for i in range(len(text)):
    print(f"position {i}: {text[i]}")
```

Saída:

```python
position 0: H
position 1: e
position 2: y
```

Iterando sobre Strings Parte 2

A divisão de strings permite que você divida uma string em uma lista, enquanto a junção permite combinar itens de uma lista em uma string.

O método `split()` divide uma string em uma lista de substrings com base em um delimitador.

Dividir por espaço em branco:

```python
text = "apple banana cherry"
fruits = text.split()
print(fruits)
# ['apple', 'banana', 'cherry']
```

Dividir com um delimitador específico:

```python
data = "john,25,new york"
data = data.split(',')
print(data)
# ['john', '25', 'new york']
```

O método `join()` combina elementos de um iterável em uma única string.

Junção básica:

```python
words = ['Hello', 'World', 'Python']
text = ' '.join(words)
print(text)
# "Hello World Python"
```

Limpar lista:
```python
nome_lista.clear()
```