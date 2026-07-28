Um `while` loop é diferente do `for` loop. Um `for` loop permite iterar sobre um `range` específico, enquanto um `while` loop permite continuar iterando enquanto uma determinada **condição** for atendida.

Para usar um `while` loop, escreva:

```python
while condition:   
	code
```

O código será executado apenas se a condição for `True`.

A **condição** é tipicamente formada usando **operadores de comparação** como `<=` (menor ou igual a), `>=` (maior ou igual a), `<` (menor que), `>` (maior que) ou `==` (igual a). O loop continua rodando enquanto essa comparação avaliar para `True`, e para assim que se torna `False`.  
  
Dentro do corpo do loop, você geralmente precisa **atualizar** a variável que está sendo verificada. Isso é feito com **operadores de atribuição aumentada** como `+=` (adicionar e atribuir), `-=` (subtrair e atribuir), `*=` (multiplicar e atribuir) ou `/=` (dividir e atribuir). Por exemplo, `x *= 2` é uma forma abreviada de `x = x * 2`. Sem atualizar a variável, a condição nunca mudaria e o loop rodaria para sempre.

Há muitos casos de uso onde um `while` resolveria o problema, mas o `for` loop não.

Por exemplo, considere este problema:

Encontre a menor potência de 2 que é maior que um número dado.

Para resolvê-lo, usaremos um `while` loop que multiplicará repetidamente a potência atual de 2 por 2 até que ela se torne maior que o número dado:

```python
number = 27
power_of_two = 1
while power_of_two <= number:
	power_of_two *= 2
	print(power_of_two)
```

Aqui, `power_of_two <= number` é a condição usando um operador de comparação, e `power_of_two *= 2` atualiza a variável a cada iteração usando um operador de atribuição aumentada. Uma vez que `power_of_two` exceda `number`, a condição se torna `False` e o loop para.

### Diferença break e continue:
A declaração `continue` interrompe a iteração atual e continua para a próxima iteração. Por exemplo:

```python
for i in range(3, 9):    if i == 5:        continue    print(i)
```

O loop iterará pelos números de `3` a `8`, e quando chegar a `i=5` pulará essa iteração e continuará para a próxima. A saída é:

```python
34678
```

Observe que o número 5 não está na saída.

A instrução `break` para o loop imediatamente quando é encontrada.

Por exemplo,

```python
for i in range(10): 
    if i == 6:
	    break    
	print(i)
```

No exemplo a seguir, o loop itera normalmente até alcançar o número 6. Então, o programa entra na instrução `if` e executa a instrução `break`. Isso **sai** do loop imediatamente. A saída é:

```python
0
1
2
3
4
5
```

- No break aquela iteração será a ultima e no continue ela será pulada e bora pra próxima