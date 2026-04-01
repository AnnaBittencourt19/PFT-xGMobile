num = int(input())
resultado = 1

for i in range(1,(num+1)):
    resultado*=i
print(resultado)

#Esse num + 1 é necessário porque a função range() não inclui o número final, ou seja, ela gera uma sequência de números que vai de 1 até num, mas não inclui num. Portanto, para incluir num na sequência, precisamos usar num + 1 como o número final.