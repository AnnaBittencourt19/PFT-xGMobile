print("Bill Split Calculator")
valor_conta = float(input())
porcentagem_gorjeta = float(input())
gorjeta = (porcentagem_gorjeta / 100) * valor_conta
valor_com_gorjeta = valor_conta + gorjeta
print(valor_com_gorjeta)
