Listas possuem muitos métodos (funcionalidades). Para acessar um método, escreva:

```python
some_list.method()
```

Aqui está uma lista dos métodos básicos:

- `append(element)` - adiciona **um único elemento** ao final da lista
- `clear()` - remove todos os elementos da lista

- `pop(index)` - remove um elemento no índice especificado
- `reverse()` - inverte a ordem da lista
- `sort()` - ordena a lista em ordem crescente

**Nota Importante:** O método `append()` adiciona um único elemento. Se você tentar anexar uma lista inteira, ela será adicionada como uma lista aninhada, o que geralmente não é o que você deseja. Por exemplo:

```python
lst1 = [1, 2]
lst2 = [3, 4]
lst1.append(lst2)  # Abordagem incorreta para mesclar
print(lst1)  # Saída: [1, 2, [3, 4]] - lst2 está aninhada dentro!
```

Para combinar elementos de duas listas, use um loop para anexar elementos individuais em vez disso.

Aqui está um exemplo de como usar o método `append` corretamente:

```python
my_list = ["orange", "banana", "apple"]
my_list.append("strawberry")
print(my_list)
```

Isso resultará em `["orange", "banana", "apple", "strawberry"]`.

Exemplo do método `clear`:

```python
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)
```

Isso resultará em `[]`.

Exemplo do método `sort`:

```python
my_list = [1, 9, 2, 3]
my_list.sort()
print(my_list)
```