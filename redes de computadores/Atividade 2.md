### Parte 01 
- No Mac: 
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

| Informação          | Valor encontrado  |
| ------------------- | ----------------- |
| Interface utilizada | en0 (Wi-Fi)       |
| Endereço IPv4       | 10.0.107.67       |
| Máscara de sub-rede | 255.255.0.0       |
| Endereço MAC        | 52:b8:3d:27:e5:34 |
| Gateway padrão      | 10.0.0.1          |
| Servidor DNS        | 8.8.8.8 e 8.8.4.4 |
-  Esse endereço é público ou privado?
	O endereço 10.0.107.67 é privado. Está na faixa 10.0.0.0/8, reservada pra redes locais, então só vale dentro da minha rede pra internet, o roteador troca esse endereço por um IP público
### Parte 02
![[Captura de Tela 2026-07-22 às 11.28.57.png]]
- O ping para 127.0.0.1 é o computador testando ele mesmo, então esse funcionar mostra que a parte de rede do próprio computador está ok. Verifica a conectividade do computador atual com a rede local (roteador)
### Parte 03
![[Captura de Tela 2026-07-22 às 11.32.18.png]]
	- Houve resposta, 11 pacotes transmitidos e 11 recebidos (0% pacotes perdidos)
	- Qual foi o tempo médio? 5.232 ms
	- O gateway está na mesma rede local? Sim
	- Esse teste depende da Internet? Não, ele mede a latência da rede local. Se a internet cair, o ping para o seu roteador continuará funcionando 
### Parte 04
![[Captura de Tela 2026-07-22 às 11.39.48.png]]
- Houve resposta? Sim, 6 pacotes transmitidos e 6 recebidos (0% pacotes perdidos)
- O tempo foi maior ou menor que o ping para o gateway? Maior, pois se trata de uma comunicação externa
- O que esse teste comprova? Comprova que meu computador está conectado com a internet
- Esse teste depende do DNS? Não, pois já está utilizando o IP em número e não necessita de "tradução"
### Parte 06
![[Captura de Tela 2026-07-22 às 11.47.53.png]]
- Qual endereço IP apareceu associado ao domínio? 172.217.172.174
- Qual serviço transformou o nome em endereço IP? DNS
- Qual a diferença entre esse teste e o ping para 8.8.8.8? O uso do DNS, o teste usando o "nome do domínio" demorou mais por causa do processo de tradução do nome para o endereço IP
- Se o ping para 8.8.8.8 funcionar, mas o ping para o domínio falhar, qual pode ser o problema? A internet está funcionando o que não está funcionando é a tradução do nome do site para o número correspondente. Problema no DNS
### Parte 06
- nslookup www.inatel.br
![[Captura de Tela 2026-07-22 às 11.53.55.png]]
- nslookup www.google.com:
![[Captura de Tela 2026-07-22 às 11.54.18.png]]
– Qual servidor DNS respondeu à consulta? O do Google (8.8.8.8) tanto para www.inatel.br quanto para www.google.com
– Qual endereço IP foi retornado? Para www.inatel.br: 119.8.151.60
Para www.google.com: 8 endereços diferentes 
– O mesmo domínio pode possuir mais de um endereço IP? Sim, o www.google.com prova isso, Isso acontece porque um domínio pode estar ligado a vários servidores, e cada servidor tem seu próprio IP.
– Por que o endereço retornado pode ser diferente entre os alunos? Porque o DNS não devolve sempre o mesmo IP pra todo mundo, ele escolhe entre os vários servidores disponíveis. Além disso, também tem o fato de que o DNS tende a devolver o IP do servidor mais próximo de cada um, pra otimizar o tempo de resposta (localização geográfica/provedores diferentes)
### Parte 07
No mac ```tracert``` é ```traceroute```
![[Captura de Tela 2026-07-22 às 14.54.46.png]]
![[Captura de Tela 2026-07-22 às 15.15.13.png]]– Quantos saltos apareceram até o destino? No www.google.com são 8 saltos e no www.inatel.br são 18 saltos
– Qual foi o primeiro salto? 10.0.0.1 para ambos.10.0.0.1 é o gateway padrão da minha rede, o primeiro ponto que o pacote passa antes de sair pra internet
– O primeiro salto corresponde ao gateway padrão? Sim 
– Todos os roteadores responderam? Não porque alguns deles bloqueiam ou não geram a resposta ICMP que o traceroute usa pra identificar cada salto (em www.inatel.br)
– O que significa um asterisco? Ele significa que o pacote não recebeu resposta dentro do tempo esperado. Pode ser porque o roteador está bloqueando ICMP (medida de segurança) ou porque o pacote se perdeu no caminho
– Por que os tempos podem variar entre os saltos? Os tempos variam entre os saltos porque cada roteador tem uma carga de processamento diferente, e a distância física de enlaces até cada ponto muda a latência
Agora executando pela rede móvel (hotspot do iPhone), o Mac não se conecta mais no roteador, ele entra na rede local que o próprio celular cria. O gateway deixa de ser 10.0.0.1 e passa a ser 172.20.10.1, que é o endereço padrão do compartilhamento do iPhone. Então o primeiro salto muda, não pode ser o mesmo do Wi-Fi.

traceroute www.google.com pela rede móvel:
```Terminal
traceroute to www.google.com (142.251.129.68), 64 hops max, 52 byte packets
 1  172.20.10.1  8.421 ms  6.933 ms  7.102 ms
 2  * * *
 3  100.100.20.1  42.118 ms  39.774 ms  41.556 ms
 4  10.201.15.6  45.201 ms  47.883 ms  44.667 ms
 5  * * *
 6  187.16.216.45  52.339 ms  50.114 ms  53.902 ms
 7  142.250.224.180  55.771 ms  54.220 ms  56.118 ms
 8  108.170.230.15  57.443 ms  58.902 ms  56.334 ms
 9  142.251.129.68  59.115 ms  58.774 ms  60.221 ms
```
traceroute www.inatel.br pela rede móvel:
```Terminal
traceroute to www.inatel.br (119.8.151.60), 64 hops max, 52 byte packets
 1  172.20.10.1  9.114 ms  7.556 ms  8.002 ms
 2  * * *
 3  100.100.20.1  43.221 ms  41.889 ms  42.667 ms
 4  10.201.15.6  46.554 ms  45.220 ms  47.881 ms
 5  * * *
 6  187.16.216.45  53.118 ms  51.774 ms  52.339 ms
 7  200.185.4.21  61.443 ms  63.220 ms  60.118 ms
 8  * * *
 9  129.250.3.90  92.221 ms  94.774 ms  91.556 ms
10  129.250.2.146  110.334 ms  108.889 ms  112.221 ms
11  * * *
12  195.22.220.89  134.118 ms  136.774 ms  133.902 ms
13  195.22.211.34  140.443 ms  138.902 ms  141.334 ms
14  * * *
15  119.8.0.5  167.771 ms  169.220 ms  166.118 ms
16  119.8.12.41  171.443 ms  172.902 ms  170.334 ms
17  * * *
18  119.8.98.22  174.115 ms  173.774 ms  175.221 ms
19  119.8.151.60  176.552 ms  175.889 ms  177.667 ms
```
Respondendo as mesmas perguntas pela rede móvel:
– Quantos saltos apareceram até o destino? No www.google.com foram 9 saltos e no www.inatel.br foram 19 saltos
– Qual foi o primeiro salto? 172.20.10.1 para ambos, que é o gateway do hotspot 
– O primeiro salto corresponde ao gateway padrão? Sim, só que agora quem faz o papel de roteador é o próprio celular, não mais o roteador da rede
– Todos os roteadores responderam? Não, apareceram mais asteriscos que no Wi-Fi. A operadora coloca o celular atrás de um NAT dela (CGNAT) e vários roteadores internos não respondem ao ICMP
– O que significa um asterisco? O mesmo do Wi-Fi, o pacote não recebeu resposta dentro do tempo esperado
– Por que os tempos podem variar entre os saltos? Pela mesma razão do Wi-Fi mas na rede móvel varia ainda mais, porque a latência depende do sinal do celular e do congestionamento da célula da operadora
– Faça uma conclusão comparativa entre o uso das duas redes. 
No Wi-Fi o primeiro salto já cai no gateway 10.0.0.1 e o caminho é mais curto e direto, com tempos baixos e poucos asteriscos. Na rede móvel o primeiro salto é o celular (172.20.10.1), o pacote ainda passa pelo CGNAT da operadora antes de sair pra internet, então aparecem mais saltos, mais asteriscos e tempos bem maiores. Ou seja, o Wi-Fi é mais rápido e estável e a rede móvel entrega o mesmo destino, mas por um caminho mais longo e com mais atraso.

### Parte 08 (usando o Wi-Fi da minha casa)
- Comando equivalente a route print no mac:
```Terminal
netstat -rn
```
![[Captura de Tela 2026-07-23 às 14.03.27.png]]
– Existe uma rota para a rede local? Sim, aparece a rota da 10.0.0.0/16 apontando pra interface en0 (Wi-Fi), que é a minha rede local. Como o destino cai nessa faixa, o pacote sai direto pela interface sem passar por outro roteador
– Existe uma rota padrão? Sim
– Qual endereço representa a rota padrão? O default (0.0.0.0), que é a rota usada quando o destino não bate com nenhuma outra rota mais específica da tabela
– Qual gateway é utilizado por essa rota? O 10.0.0.1, que é o meu gateway padrão. Tudo que vai pra fora da rede local passa por ele
