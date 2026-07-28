A função `enumerate()` permite que você percorra uma sequência (como uma lista, tupla ou string) enquanto mantém o controle da posição do índice de cada item.

sem o `enumerate()`, acessaríamos tanto o índice quanto o valor da seguinte forma:

```python
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
```

`enumerate()` é uma maneira mais elegante de obter tanto o índice quanto o valor:

```python
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

Ambos os exemplos produzirão a seguinte saída:

```python
Index 0: apple
Index 1: banana
Index 2: orange
```