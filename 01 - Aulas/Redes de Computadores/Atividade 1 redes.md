### Parte 1
- No Mac 
- Comando equivalente ao ipconfig all: (Interface a Endereço MAC)
```Terminal
ifconfig 
```
- Comando para achar o Gateway padrão:
```Terminal
route -n get default
```
- Comando para achar DNS:
```Terminal
scutil --dns
```

- Tabela:

| Informação          | Valor encontrado    |
| ------------------- | ------------------- |
| Interface utilizada | en0 (Wi-Fi)         |
| Endereço IPv4       | 10.0.107.98         |
| Máscara de rede     | 255.255.0.0         |
| Endereço MAC        | 52:b8:3d:27:e5:34   |
| Gateway padrão      | 10.0.0.1            |
| Servidor DNS        | `8.8.8.8` e 8.8.4.4 |
- Por que tem dois DNSs?
	Um é o principal e o outro é reserva. Toda vez que um site é acessado, o DNS traduz o nome para o IP correspondente. Se o primeiro estiver fora do ar ou demorar pra responder, o computador usa o segundo. É só uma garantia pra não depender de um só
### Parte 2
- IP do computador: 10.0.107.98
- IP do gateway: 10.0.0.1
- Mascara de rede: 255.255.0.0
- Comparando:

| IP do computador                     | 00001010 | 00000000 | 01101011 | 01100010 |
| ------------------------------------ | -------- | -------- | -------- | -------- |
| Máscara de rede (em binário)         | 11111111 | 11111111 | 00000000 | 00000000 |
| IP do computador AND máscara de rede | 00001010 | 00000000 | 00000000 | 00000000 |
| Máscara de rede (em decimal)         | 255      | 255      | 0        | 0        |
| IP do computador (em decimal)        | 10       | 0        | 107      | 98       |

| IP do gateway                     | 00001010 | 00000000 | 00000000 | 00000001 |
| --------------------------------- | -------- | -------- | -------- | -------- |
| Máscara de rede (em binário)      | 11111111 | 11111111 | 00000000 | 00000000 |
| IP do gateway AND máscara de rede | 00001010 | 00000000 | 00000000 | 00000000 |
| Máscara de rede (em decimal)      | 255      | 255      | 0        | 0        |
| IP do gateway (em decimal)        | 10       | 0        | 0        | 1        |

- O computador e o gateway pertencem à mesma rede local?
	Sim. Quando é usada a operação AND entre o IP e a máscara de rede nos dois casos, chego ao mesmo endereço de rede: 10.0.0.0. O computador (10.0.107.98) e o gateway (10.0.0.1) compartilham os dois primeiros octetos (10.0), que é justamente a parte que a máscara 255.255.0.0 reserva para identificar a rede. Como esse endereço é idêntico para os dois, eles estão na mesma rede local e conseguem conversar diretamente, sem precisar passar por outro roteador
### Parte 3
##### ping 127.0.0.1
![[Captura de Tela 2026-07-21 às 18.23.05.png]]
##### ping <IP_DO_GATEWAY>
![[Captura de Tela 2026-07-21 às 18.25.24.png]]
##### ping 8.8.8.8
![[Captura de Tela 2026-07-21 às 18.26.57.png]]
##### ping google.com
![[Captura de Tela 2026-07-21 às 18.27.41.png]]
### Parte 4 - Diagnóstico rápido
- Situação A
	ping 127.0.0.1 → funciona
	ping gateway → falha
	O ping para 127.0.0.1 é o computador testando ele mesmo, então esse funcionar mostra que a parte de rede do próprio computador está ok. O que falha é chegar até o gateway, que é o aparelho que conecta a rede local (o roteador). Ou seja, o computador está funcionando, mas não consegue falar com o roteador. Provavelmente é uma questão de conexão: cabo desconectado ou Wi-Fi caído 
- Situação B
	ping gateway → funciona
	ping 8.8.8.8 → falha
	Aqui o computador consegue falar com o roteador (o gateway responde), então a rede está funcionando. O que falha é chegar num endereço lá fora na internet. Isso indica que o problema não é do computador, e sim do roteador para fora: a internet do provedor deve estar fora do ar
- Situação C
	ping 8.8.8.8 → funciona
	ping google.com → falha
	O computador consegue chegar na internet quando usa o endereço em números (8.8.8.8), mas falha quando usa o nome do site (google.com). A internet está funcionando o que não está funcionando é a tradução do nome do site para o número correspondente. Problema no DNS
Ou seja, se o ping 127.0.0.1 falha, o problema no próprio computado, se o ping gateway falha  p problema está na rede local (cabo, Wi-Fi ou conexão com o roteador), já se o ping 8.8.8.8 falha o problema é na internet (provedor) e se ping google.com falha (mas 8.8.8.8 funciona) problema no DNS
### Parte 5
1. Qual é o endereço IP da máquina? 
	10.0.107.98
2. Esse endereço é público ou privado?
	É privado. Está na faixa 10.0.0.0/8, reservada pra redes locais, então só vale dentro da minha rede pra internet, o roteador troca esse endereço por um IP público
3. Qual é o gateway padrão?
	10.0.0.1
4. O computador e o gateway estão na mesma rede?
	Sim. Como visto na parte 2, aplicando a máscara 255.255.0.0 nos dois endereços se chega no mesmo endereço de rede 10.0.0.0, então eles não passam por outro roteador
5. Qual interface está sendo utilizada?
	en0 (Wi-Fi)
6. Qual foi o RTT até o gateway?
	Na média de 4,4 ms, variando entre 2,8 e 7,4 ms
7. Qual foi o RTT até um servidor externo?
	Até o 8.8.8.8 ficou em torno de 10 ms, variando entre 7,6 e 12,4 ms
8. Por que o RTT externo costuma ser maior?
	Porque o pacote passa por mais saltos até chegar lá fora. Pro gateway é só um salto, dentro da própria rede, mas pro servidor externo o pacote passa pelo roteador, pelo provedor e por outros roteadores pelo caminho até a internet
9. O que é testado ao usar ping 8.8.8.8?
	Se consigo chegar na internet usando só o número do IP, sem depender de tradução de nome. Se funcionar, a conexão com a internet está ok
10. O que é acrescentado ao usar ping google.com
	Entra a resolução de DNS: o nome precisa ser traduzido pro IP correspondente antes do pacote ser enviado, então esse teste mostra se o DNS está funcionando
### Parte 6
| Informação          | Valor encontrado    | Valor encontrado     |
| ------------------- | ------------------- | -------------------- |
| Interface utilizada | en0 (Wi-Fi)         | Rede móvel (Hotspot) |
| Endereço IPv4       | 10.0.107.98         | 10.20.4.114          |
| RTT até 8.8.8.8     | 10 ms               | 59 ms                |
| RTT até google.com  | 20 ms               | 60 ms                |
| Gateway padrão      | 10.0.0.1            | 10.20.4.203          |
| Servidor DNS        | `8.8.8.8` e 8.8.4.4 | 10.20.4.203          |
Print pingando usando rede móvel:
![[Captura de Tela 2026-07-21 às 19.17.30.png]]
• Responda:
	– O endereço IP mudou?
	Sim. No Wi-Fi era 10.0.107.98 e na rede móvel passou a ser 10.20.4.114, porque agora o celular criou uma rede local diferente pro notebook se conectar
	– O gateway mudou?
	Sim. Foi de 10.0.0.1 para 10.20.4.203, já que agora quem faz o papel de roteador é o próprio celular, não mais o roteador 
	– O RTT ficou maior ou menor?
	Maior. Até o 8.8.8.8 subiu de 10 ms para 59 ms, e até o google.com subiu de 20 ms para 60 ms
	– A rede móvel apresentou desempenho semelhante ao Wi-Fi?
	Não, ficou bem mais lenta. O RTT quase sextuplicou até o 8.8.8.8 e triplicou até o google.com, o que mostra que o caminho pela rede móvel tem mais atraso que o Wi-Fi 
	– O endereço IP é privado ou pública? 
	Privado. O 10.20.4.114 também está na faixa reservada pra redes locais, só que dessa vez é a rede local criada pelo hotspot do celular
### Print tentando pingar do meu notebook usando roteamento do celular no notebook da Dani usando o roteamento do celular dela
![[Captura de Tela 2026-07-21 às 18.57.25.png]]
- Por que dá erro?
	Cada celular cria a própria rede local quando compartilha internet por hotspot, então meu notebook e o da Dani ficam em redes diferentes, cada uma com seu próprio gateway. Além disso, a operadora normalmente coloca os celulares atrás de um NAT dela (CGNAT), então o IP que o celular da Dani mostra pro notebook dela nem é alcançável de fora daquela rede. Sem uma rota entre as duas redes, o pacote do ping sai do meu notebook mas não acha caminho até o 10.186.110.92, e o request sempre estoura o tempo, dando timeout em todos os pacotes

