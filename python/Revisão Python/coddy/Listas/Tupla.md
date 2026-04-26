Uma tupla é uma coleção ordenada de elementos imutável (somente leitura). Ao contrário das listas, uma vez criadas, as tuplas não podem ser modificadas.

Crie uma tupla com parênteses:

```python
fruits = ("apple", "banana", "cherry")
```

Você também pode criar uma tupla sem parênteses:

```python
colors = "red", "green", "blue"
```

Acesse elementos de tuplas usando indexação (assim como listas):

```python
first_fruit = fruits[0]  # "apple"
```

Lembre-se, as tuplas são imutáveis, então você não pode modificar os elementos:

```python
# Isso causará um erro
# fruits[0] = "orange"
```

Uma tupla com um único elemento precisa de uma vírgula final:

```python
single_item = ("apple",)  # Esta é uma tupla
not_a_tuple = ("apple")   # Esta é uma string
```