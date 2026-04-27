Fatiamento de Listas Parte 1

O fatiamento (slicing) nos permite extrair partes de uma lista usando a seguinte sintaxe: `lst[start:stop]`. Por exemplo, considere esta lista:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Obtendo uma parte da lista:

```python
print(numbers[2:6])
# Saída: [2, 3, 4, 5]
```

Isso obtém elementos do índice 2 (inclusive) ao índice 6 (exclusive)

Omitindo o parâmetro de início:

```python
print(numbers[:5])
# Saída: [0, 1, 2, 3, 4]
```

Quando start é omitido, slice começa a partir do índice 0

Omitindo o parâmetro stop:

```python
print(numbers[5:])
# Saída: [5, 6, 7, 8, 9]
```

Quando o stop é omitido, o slice vai até o final