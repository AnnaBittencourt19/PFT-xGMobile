# Tudo explicado - Atividade de redes

Esse arquivo explica o porque de cada resposta da atividade, parte por parte, com o conceito por trás de cada uma.
## Parte 1 - Descobrindo os dados da minha rede

### ifconfig
No Mac não existe o comando ipconfig /all do Windows, o equivalente é o ifconfig. Ele lista todas as interfaces de rede do computador (Wi-Fi, Ethernet, loopback etc) e mostra, pra cada uma, o endereço IP, a máscara de rede e o endereço MAC. Uso ele porque preciso ver os dados da interface que está ativa, no meu caso a en0, que é o Wi-Fi

### route -n get default
Esse comando pergunta pro sistema qual é a rota padrão, ou seja, pra onde o computador manda um pacote quando o destino não está na rede local. Essa rota padrão aponta pro gateway, que no meu caso é 10.0.0.1. Todo pacote que não é pra alguém dentro da minha própria rede passa primeiro por esse endereço antes de sair pra internet

### scutil --dns
Mostra os servidores DNS configurados no computador. O DNS é o serviço que traduz nome de site (como google.com) pro endereço IP correspondente, porque a internet funciona com números, não com nomes. Sem essa tradução o navegador não saberia pra qual IP mandar a requisição

### Por que tem dois DNSs?
Um é o principal e o outro é reserva. Toda vez que acesso um site, o DNS traduz o nome pro IP correspondente. Se o primeiro servidor estiver fora do ar ou demorar demais pra responder, o computador tenta o segundo. É uma garantia de redundância, pra não ficar refém de um único servidor: se ele cair, ainda consigo navegar

## Parte 2 - IP, máscara de rede e a operação AND

O conceito central dessa parte é entender como o computador descobre se outro endereço está na mesma rede local ou não, sem precisar perguntar pra ninguém. Ele faz isso comparando o próprio IP com o IP do outro através da máscara de rede

Um endereço IPv4 tem 32 bits, divididos em 4 blocos de 8 bits (octetos). A máscara de rede também tem 32 bits, e ela funciona como um filtro: os bits em 1 dizem qual parte do IP identifica a rede, e os bits em 0 dizem qual parte identifica o host (o dispositivo dentro dessa rede). A máscara 255.255.0.0 em binário é 11111111.11111111.00000000.00000000, ou seja, os dois primeiros octetos são fixos (identificam a rede) e os dois últimos variam (identificam cada dispositivo)

A operação AND bit a bit entre o IP e a máscara "apaga" a parte de host e deixa só a parte de rede. Pra cada bit: 1 AND 1 = 1, 1 AND 0 = 0, 0 AND qualquer coisa = 0. Fazendo isso com o meu IP (10.0.107.98) e com o IP do gateway (10.0.0.1), usando a mesma máscara 255.255.0.0, os dois resultados dão 10.0.0.0. Esse resultado é o endereço de rede

### O computador e o gateway pertencem à mesma rede local?
Sim. Como os dois chegam no mesmo endereço de rede (10.0.0.0) depois do AND com a máscara, eles pertencem à mesma rede local. Isso importa na prática porque, quando dois dispositivos estão na mesma rede, eles conseguem se enviar pacotes diretamente, sem precisar passar por um roteador no meio. Se estivessem em redes diferentes, o pacote precisaria ser roteado

## Parte 3 - Os quatro pings

Ping é um comando que usa o protocolo ICMP pra mandar um pacote pequeno (echo request) pra um endereço e esperar uma resposta (echo reply). Ele serve pra testar se existe conectividade até aquele destino e pra medir quanto tempo a resposta demora (RTT). Cada um dos quatro pings testa uma camada diferente do caminho até a internet:

- ping 127.0.0.1: é o endereço de loopback, testa a própria pilha de rede do computador, sem sair pra rede nenhuma
- ping no gateway: testa se o computador consegue falar com o roteador, ou seja, se a rede local está funcionando
- ping 8.8.8.8: testa se existe conectividade até um endereço fora da rede local, na internet, usando só o número do IP
- ping google.com: testa a mesma coisa, mas usando o nome do site, o que acrescenta a etapa de resolução DNS antes de mandar o pacote

Fazer os quatro em sequência é uma forma de isolar em qual camada um problema está acontecendo, que é exatamente o que a Parte 4 usa

## Parte 4 - Diagnóstico rápido

A lógica dessa parte é: cada ping testa uma camada, então o primeiro ping que falha aponta onde está o problema, seguindo a ordem 127.0.0.1 → gateway → 8.8.8.8 → google.com

### Situação A: ping 127.0.0.1 funciona, ping gateway falha
O 127.0.0.1 é o computador testando ele mesmo, então esse funcionar mostra que a placa de rede e a pilha TCP/IP do próprio computador estão ok. O que falha é chegar até o gateway, que é o roteador que conecta a rede local. Se nem o roteador responde, o problema está entre o computador e ele: cabo desconectado, Wi-Fi caído, ou o próprio roteador desligado

### Situação B: ping gateway funciona, ping 8.8.8.8 falha
Aqui o roteador responde, o que já mostra que a rede local está funcionando. O que falha é chegar num endereço lá fora, na internet. Como a rede local está ok e mesmo assim não chega na internet, o problema não é do computador, é do roteador pra fora: provavelmente a internet do provedor caiu

### Situação C: ping 8.8.8.8 funciona, ping google.com falha
O computador chega na internet quando usa o endereço em números (8.8.8.8), então a conectividade está funcionando de ponta a ponta. Só falha quando usa o nome do site. A única diferença entre os dois comandos é a etapa de tradução de nome pra número, então o problema só pode estar aí: no DNS

Juntando tudo: se o ping 127.0.0.1 falha, o problema é no próprio computador. Se o ping no gateway falha, o problema é na rede local (cabo, Wi-Fi ou o roteador). Se o ping 8.8.8.8 falha (mas o gateway responde), o problema é na internet do provedor. Se o ping google.com falha mas o 8.8.8.8 funciona, o problema é no DNS

## Parte 5 - Perguntas sobre os próprios resultados

### Qual é o endereço IP da máquina, e é público ou privado?
O IP é 10.0.107.98, e é privado. Existem faixas de IP reservadas só pra uso dentro de redes locais, que nunca aparecem circulando na internet pública: 10.0.0.0/8, 172.16.0.0/12 e 192.168.0.0/16. A minha máquina está na primeira faixa. Isso existe porque IPv4 tem endereços limitados, então em vez de cada dispositivo do mundo ter um IP público único, os dispositivos dentro de uma rede local usam IPs privados repetidos (várias redes diferentes podem ter uma máquina com 10.0.107.98), e o roteador troca esse IP privado por um IP público só na hora de sair pra internet, através do NAT

### Qual é o gateway padrão, e o computador está na mesma rede que ele?
O gateway é 10.0.0.1, e sim, ele está na mesma rede que o meu computador, pelo mesmo motivo explicado na Parte 2: aplicando a máscara 255.255.0.0 nos dois IPs, os dois chegam no endereço de rede 10.0.0.0. Isso é o que permite eles conversarem direto, sem precisar de outro roteador no meio

### Qual interface está sendo utilizada?
en0, que no Mac é o nome da interface Wi-Fi. Cada forma de conexão (Wi-Fi, cabo Ethernet, hotspot) aparece como uma interface diferente pro sistema, e cada uma tem seu próprio IP, gateway e configuração

### RTT até o gateway e até um servidor externo, e por que o externo costuma ser maior
O RTT (round-trip time) é o tempo que um pacote leva pra ir até o destino e a resposta voltar, contado em milissegundos. Até o gateway ficou em torno de 4,4 ms, e até um servidor externo (8.8.8.8) ficou em torno de 10 ms. A diferença existe porque o gateway está a um salto de distância, dentro da própria rede local, enquanto o servidor externo está vários saltos além: o pacote passa pelo roteador de casa, pela rede do provedor, e por outros roteadores no caminho até chegar no destino. Cada salto (cada roteador que o pacote atravessa) soma um pouco de atraso, então quanto mais distante o destino, maior tende a ser o RTT

### O que é testado ao usar ping 8.8.8.8, e o que muda com ping google.com
O ping pro 8.8.8.8 testa só a conectividade de rede: se o pacote consegue sair da minha rede, atravessar a internet e chegar num destino externo usando diretamente o número do IP. Já o ping google.com testa a mesma conectividade, mas acrescenta uma etapa antes: a resolução DNS, que é a tradução do nome google.com pro IP correspondente. Se o DNS estiver com problema, esse segundo ping falha mesmo com a internet funcionando normalmente, porque o computador nem descobre pra qual IP mandar o pacote

## Parte 6 - Wi-Fi contra rede móvel (hotspot)

### O endereço IP mudou?
Sim, de 10.0.107.98 no Wi-Fi para 10.20.4.114 na rede móvel. Isso acontece porque o hotspot do celular cria a própria rede local, separada da rede Wi-Fi de casa, e distribui IPs dessa nova faixa pros dispositivos que se conectam nele

### O gateway mudou?
Sim, de 10.0.0.1 para 10.20.4.203. No Wi-Fi, quem faz o papel de roteador (gateway) é o roteador de casa. No hotspot, quem assume esse papel é o próprio celular, então o gateway muda junto com a rede

### O RTT ficou maior ou menor, e a rede móvel teve desempenho parecido com o Wi-Fi?
Ficou maior, e bem maior: até o 8.8.8.8 subiu de 10 ms pra 59 ms, e até o google.com subiu de 20 ms pra 60 ms. Ou seja, não teve desempenho parecido, o RTT quase sextuplicou num caso e triplicou no outro. Isso acontece porque o caminho até a internet via rede móvel normalmente passa por mais infraestrutura da operadora (antena, torre, núcleo da rede celular) antes de sair pra internet, comparado com uma conexão de banda larga fixa, e isso soma atraso

### O endereço IP da rede móvel é privado ou público?
Privado. O 10.20.4.114 também está dentro da faixa 10.0.0.0/8, reservada pra redes locais, só que dessa vez a rede local é a que o próprio celular cria pra distribuir internet via hotspot. Assim como no Wi-Fi de casa, o celular faz NAT pra traduzir esse IP privado num IP público na hora de sair pra internet

### Por que dá erro ao tentar pingar de um notebook pro outro, cada um numa rede móvel diferente?
Cada celular, ao compartilhar internet por hotspot, cria a própria rede local isolada. Isso significa que o meu notebook e o notebook da Dani ficam em redes diferentes, cada uma com seu próprio gateway, mesmo que os dois estejam usando dados móveis. Além disso, as operadoras de celular costumam colocar os aparelhos atrás de um NAT delas também, chamado CGNAT (carrier-grade NAT): o IP que o celular da Dani mostra pro notebook dela é só o IP dentro da rede do hotspot, e esse endereço não é alcançável de fora daquela rede, nem mesmo pela própria operadora. Sem uma rota entre as duas redes e sem um IP público de fato alcançável, o pacote do ping sai do meu notebook mas não encontra caminho até o 10.186.110.92, e cada tentativa estoura o tempo de espera, resultando em timeout pra todos os pacotes e 100% de perda
