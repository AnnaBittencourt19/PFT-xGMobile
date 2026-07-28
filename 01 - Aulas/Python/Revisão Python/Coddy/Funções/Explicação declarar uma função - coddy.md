
Uma função é uma sequência de código que possui um nome. O propósito de uma função é reutilizar um pedaço de código várias vezes.

Por exemplo, dê uma olhada neste código:

```python
print("Welcome to Coddy")print("New session...")print("Welcome to Coddy")print("Another session...")print("Welcome to Coddy")
```

Usamos o mesmo código `print("Welcome to Coddy")` repetidamente. Outro problema com este código é que, se quiséssemos alterar a mensagem: `Welcome to Coddy` para algo diferente, como "`Welcome aboard`", teríamos que alterar 3 linhas diferentes de código. Para resolver esse problema, usaremos funções.

Para declarar uma função, usamos a seguinte sintaxe:

```python
def function_name():    code
```

Para o nosso exemplo, criaremos uma função chamada `greet` e ela ficará assim:

```python
def greet():    print("Welcome to Coddy")
```

Para usar/chamar/executar a função, escrevemos `greet()`:

```python
greet()print("New session...")greet()print("Another session...")greet()
```

Isso resultará na mesma saída de cima.

> **Importante!** O código da função **deve** vir antes de sua chamada
