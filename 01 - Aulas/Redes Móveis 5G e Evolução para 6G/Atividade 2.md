## Etapa 1 — Montagem da arquitetura
	
	UE --Uu--> RU --fronthaul--> DU
Da DU para cima o caminho se divide
	``controle: DU --F1-C--> CU-CP --N2--> AMF``
	``usuário:  DU --F1-U--> CU-UP --N3--> UPF --N6--> DN --> servidor``
E1 liga CU-CP e CU-UP. É controle a CU-CP usa ela para configurar como a CU-UP vai tratar os dados
- Delimitação do gNB
	- dentro: RU, DU, CU-CP, CU-UP
	- fora: UE (é o outro lado da interface rádio), AMF, UPF, DN
- Interfaces

| Interface | Liga | Plano |
| --- | --- | --- |
| Uu | UE - RU | os dois |
| F1-C | DU - CU-CP | controle |
| F1-U | DU - CU-UP | usuário |
| E1 | CU-CP - CU-UP | controle |
| N2 | CU-CP - AMF | controle |
| N3 | CU-UP - UPF | usuário |
| N6 | UPF - DN | usuário |
| Xn | gNB - gNB | controle e encaminhamento no handover |

- Transporte
	- fronthaul: RU até DU
	- midhaul: DU até CU, é onde correm F1-C e F1-U
	- backhaul: CU até o Core, carrega N2 e N3 juntos
- RU - DU - CU: gNB
## Etapa 2 — Caminho do controle
UE -> RU -> DU -> CU-CP -> AMF
- UE: liga, procura o SSB, sincroniza, faz random access e pede a conexão RRC. É ele que inicia o registro
- RU: parte de rádio, converte o sinal. Transmite a mensagem
- DU: fica com RLC, MAC e PHY, é a parte sensível a tempo. Entrega a sinalização à CU-CP pela F1-C
- CU-CP: Fica o RRC e o PDCP de controle. Termina a conexão RRC com o UE e encaminha as mensagens NAS para o Core. Repassa
- AMF: registra o UE, cuida da conexão e da mobilidade, coordena a autenticação junto com AUSF e UDM, e seleciona o SMF que vai montar a sessão PDU
Por que os dados da aplicação não passam pelo AMF?
	Porque o AMF é uma função só de controle. Ele existe para registrar o usuário, autenticar, aplicar política e preparar a sessão e para isso troca sinalização com a CU-CP pela N2. Quem carrega pacote de aplicação é a N3, que vai da CU-UP direto para a UPF. Se o tráfego do usuário passasse pelo AMF jogaria fora a separação entre os planos, o AMF viraria gargalo e não daria para escalar controle e usuário de forma independente, que é justamente o que o 5G quis fazer separando CU-CP de CU-UP
## Etapa 3 — Caminho dos dados do usuário
UE -> RU -> DU -> CU-UP -> UPF -> DN -> servidor de streaming
- CU-UP: fica com SDAP e PDCP do plano de usuário. O SDAP faz o mapeamento QoS Flow <-> DRB, ou seja, decide em qual bearer de rádio cada fluxo vai andar. O PDCP cifra, comprime cabeçalho e ordena. A CU-UP é configurada pela CU-CP pela E1
- UPF: encaminha os pacotes, aplica as regras que o SMF definiu, trata QoS, contabiliza tráfego e serve de ponto de ancoragem da sessão. É ela que conecta o usuário à Data Network
O vídeo é quase todo downlink, então o caminho que pesa é servidor -> DN -> UPF -> CU-UP -> DU -> RU -> UE
## Etapa 4 — Identificação do transporte
| Trecho | Enlace |
| --- | --- |
| UE - RU | Uu, interface rádio |
| RU - DU | fronthaul, CPRI/eCPRI sobre fibra |
| DU - CU | midhaul, F1-C e F1-U |
| CU - Core | backhaul, N2 e N3 |
| UPF - DN | N6 |
| gNB - gNB | Xn |

O mais rigoroso é o fronthaul com split baixo o processamento fica concentrado na DU/CU e o que trafega ali é informação muito próxima do sinal físico então a banda necessária é enorme e quase não depende do tráfego real do usuário. Além disso HARQ e escalonamento têm prazo fixo para responder, se o quadro atrasa o ciclo se perde e em TDD as células precisam estar sincronizadas entre si. Aí não é só latência baixa, é latência baixa e previsível mais sincronismo de tempo e frequência e isso é bem mais difícil de garantir do que a capacidade que o backhaul pede
## Etapa 5 — Desafio de handover
Interface Xn, direto entre gNB A e gNB B, sem passar pelo Core na fase de preparação
1. UE mede A e B com a configuração de medição que o gNB A mandou
2. UE envia o MeasurementReport ao gNB A
3. gNB A decide o handover olhando medição, política de mobilidade, carga da célula e recursos
4. gNB A pede pela Xn que o gNB B prepare a recepção. O B faz controle de admissão, reserva recurso de rádio, recebe o contexto do UE e devolve a configuração que o UE vai usar
5. gNB A manda a ordem de handover ao UE numa RRCReconfiguration, com identificação da célula, nova configuração de rádio e parâmetros de segurança
6. UE sincroniza com B, acessa a nova célula e responde RRCReconfigurationComplete
7. gNB B pede ao AMF a mudança de caminho, o Core atualiza a UPF e a N3 passa a apontar para B
8. gNB A libera o que estava guardado
Depois do handover a origem libera recursos de rádio reservados ao UE, contexto e configurações, buffers, bearers e túneis temporários e recursos de processamento. Só que isso não é imediato, enquanto o Core ainda não trocou o caminho o gNB A continua recebendo pacote pela N3 antiga e encaminha para o B pela Xn, senão o usuário perderia dados no meio da troca. A liberação vem depois da confirmação do path switch
## Qual é a diferença entre gNB lógico e equipamentos físicos do site?
gNB lógico é a função: CU, DU, RU, os protocolos, as interfaces, os dois planos. Site físico é gabinete, energia, bateria, climatização, antena, cabo, SFP, transmissão. Um gNB lógico pode estar espalhado em vários sites, com a CU num datacenter e as DUs distribuídas e um mesmo site pode hospedar mais de um gNB
## Por que N2 e N3 não devem ser confundidas?
São planos diferentes. N2 leva sinalização da RAN ao AMF (registro, mobilidade, sessão, segurança). Já o N3 leva pacote IP do usuário da RAN à UPF
## Que funções tendem a ficar mais próximas do rádio?
As sensíveis a tempo: PHY, MAC com o HARQ e RLC. Ficam na DU porque têm prazo curto de resposta e não sobrevivem a um transporte longo
## Por que fronthaul é mais exigente que backhaul em alguns cenários?
Porque o que passa nele ainda não foi processado. Quanto mais baixo o split, mais perto do sinal físico é a informação que o transporte carrega e aí a banda cresce, a tolerância a atraso cai e o sincronismo aperta. No backhaul o dado já veio processado e agregado, o requisito é mais de capacidade e disponibilidade do que de tempo
## Como infraestrutura física afeta disponibilidade da rede?
 Banco de bateria mantém o site de pé na falta de energia, climatização e monitoramento evitam que o equipamento degrade ou desligue por temperatura, gabinete protege contra intempérie e vandalismo. Se a fibra do fronthaul rompe ou o retificador queima, não importa o quanto a RAN é bem projetada aquela célula sai do ar
