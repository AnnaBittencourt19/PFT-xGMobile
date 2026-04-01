print("Bill Split Calculator")
valor_conta = float(input())
porcentagem_gorjeta = float(input())
gorjeta = (porcentagem_gorjeta / 100) * valor_conta
valor_com_gorjeta = valor_conta + gorjeta
print(f"Total (including tip): ${valor_com_gorjeta}")
pessoas = int(input())
valor_por_pessoa = valor_com_gorjeta / pessoas
print(f"Each person pays: ${valor_por_pessoa}")