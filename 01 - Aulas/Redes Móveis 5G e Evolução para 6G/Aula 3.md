- 5G Core: Mais flexível, modular e orientado a serviço
	- Network Functions (NF)
	- APIs
	- Slicing, QoS, redes privativas e edge
	- Várias funções (mais granular)
	- Base do 5G SA
	- Plano de controle e usuario bem separados
 ![[Captura de Tela 2026-08-03 às 08.35.56.png]]
 - UE, gNB e DN não fazem parte do Core mas estão relacionados a ele
## EPC (4G) x 5G Core
- EPC: entidades tradicionais de rede -> MME, SGW, PGW, HSS
- Modelo menos granular, interfaces ponto a ponto entre entidades
- Base do LTE e do 5G NSA
- 5GC: funções de rede (NF) -> AMF, SMF, UPF, UDM, AUSF, PCF
- Service-Based Architecture, suporte nativo a slicing e QoS Flow
- Base do 5G SA
- A diferença de fundo é o modelo: no EPC uma caixa fala com outra caixa por uma interface fixa, no 5GC uma função publica serviços que qualquer outra função autorizada pode consumir por API
- Isso favorece virtualização, escalabilidade e exposição controlada de serviços
## Elementos relacionados ao Core
- UE: equipamento do usuário (celular, modem, sensor)
	- Inicia registro, autenticação, solicitação de sessão PDU, envio e recebimento de dados
- gNB: conecta o UE ao Core, com duas conexões principais
	- N2 -> sinalização do plano de controle
	- N3 -> dados do plano de usuário
- DN (Data Network): rede acessada pela sessão PDU
	- Internet, rede corporativa, rede industrial privada, edge cloud, plataforma de serviços da operadora
## Funções principais do plano de controle
### AMF - Access and Mobility Management Function
- Principal porta de entrada do UE no plano de controle
- Registro do UE e gerenciamento da conexão
- Termina a sinalização NAS vinda do UE
- Coordena a autenticação (quem executa é a AUSF)
- Mobilidade e manutenção do contexto de acesso
- Seleciona o SMF e participa da seleção de slices
- Não transporta os dados da aplicação
### SMF - Session Management Function
- Gerencia as sessões PDU, que são o que permite o UE chegar numa Data Network
- Cria, modifica e libera sessões
- Seleciona a UPF e controla ela pela N4
- Gerencia parâmetros de QoS e define regras de encaminhamento
- Interage com a PCF para políticas
- Guarda informações como DNN e endereço do UE
- Configura o caminho dos dados, mas não encaminha pacote nenhum
### UDM e AUSF - identidade e autenticação
- UDM: gerencia dados de assinatura, identidades e serviços permitidos, fornece o perfil do assinante
- AUSF: conduz a autenticação junto com UDM e AMF, participa do 5G-AKA
- A diferença que confunde: a UDM é onde o dado do assinante mora, a AUSF é quem usa esse dado pra provar que o UE é quem diz ser
- SUPI: identificador permanente do assinante
- SUCI: versão cifrada do SUPI, é o que trafega para não expor a identidade permanente
- Autenticação confirma quem é o usuário, autorização define o que ele pode acessar
- Base pra segurança e roaming
### PCF - Policy Control Function
- Transforma requisito de serviço e de assinatura em política aplicável pela rede
- Fornece políticas de QoS e de controle de acesso para sessões e serviços
- Considera assinatura, aplicação e política da operadora
- Interage principalmente com a SMF, e em alguns cenários com AF e NEF
- Influencia o tratamento do serviço e a cobrança
## UPF - User Plane Function
- Única função de peso do plano de usuário
- Encaminha o tráfego entre a RAN e a rede de dados
- Aplica as regras que vêm do SMF pela N4
- Aplica tratamento de QoS, filtragem e medição de uso
- Faz contabilização (input pra cobrança)
- N3 -> troca dados com o gNB
- N6 -> conecta na Data Network
- N9 -> conecta em outra UPF
- Pode ficar centralizada ou ser empurrada pra perto do edge, e é essa mobilidade de posição que reduz latência
## SBA e descoberta de serviços
- Na SBA cada NF oferece e consome serviço das outras
- Fluxo: ![[Captura de Tela 2026-08-03 às 08.53.27.png]]
- Favorece modularidade e automação
- Em compensação aumenta a necessidade de segurança, observabilidade e controle
### NRF - Network Repository Function
- Funciona como catálogo dinâmico das NFs disponíveis
- Existe porque na SBA pode haver várias instâncias de AMF, SMF, PCF ao mesmo tempo, e alguém precisa saber quem está de pé
- Quando uma instância sobe, ela manda o perfil de NF pro NRF:
	- tipo de NF, identificação, endereços
	- quais serviços oferece e como acessar
	- em quais regiões ou slices atua
	- capacidade e situação operacional
- Motivos de uma instância nova subir: rede inicializada, aumento de capacidade, substituição de instância que falhou, escalabilidade automática
- As NFs mantêm o catálogo atualizado: atualizam perfil, informam mudança de capacidade, enviam indicação de disponibilidade, removem o registro ao desligar
- Exemplo de catálogo:
```
NRF
├── AMF 2 — disponível
├── SMF 1 — atende S-NSSAI A
├── SMF 2 — atende S-NSSAI B
└── PCF 1 — disponível
```
- Consulta: a AMF precisa de uma SMF compatível com o slice e a rede de dados que o UE pediu, então manda critérios (tipo de NF, slice, região, serviço, condição de operação) e o NRF devolve uma ou mais instâncias candidatas
- Depois disso a AMF fala direto com a SMF
- O NRF participa da descoberta mas não executa nem processa o serviço solicitado

## Funções de apoio
### NSSF - Network Slice Selection Function
- Auxilia a rede a escolher os slices permitidos e as AMFs capazes de atender o UE
- Usa S-NSSAI, assinatura e área de registro
- Fluxo: UE solicita S-NSSAI -> gNB/AMF consulta informação de seleção -> NSSF avalia slices e área -> retorna slices permitidos e AMFs candidatas
- Não cria nem orquestra a infraestrutura do slice, depende de slice já planejado e disponibilizado
### NEF - Network Exposure Function
- Deixa aplicação externa usar capacidade do 5GC de forma controlada
- Expõe capacidades, informações e eventos por API
- Ponto de entrada único, verifica autorização e protege as NFs internas
- Traduz identificador entre o domínio externo e o interno
- Pode encaminhar requisito da aplicação pra funções como a PCF
- Evita que aplicação externa acesse NF interna diretamente
### AF - Application Function
- Representa as necessidades da aplicação perante o Core
- Informa requisitos e características da aplicação
- Pode influenciar política de QoS e roteamento de tráfego
- Pode solicitar eventos e informações da rede
- Pode ser da operadora (interna, confiável) ou externa
- Aplicação externa normalmente chega no Core passando pela NEF
### NWDAF - Network Data Analytics Function
- Coleta dado de NFs, gerenciamento, serviços e desempenho dos UEs
- Produz estatística, tendência e previsão
- Fornece analytics pra outras funções consumidoras
- Apoia otimização de carga, mobilidade, QoS e slices
- Só fornece a análise, a decisão final é da NF que consome
## Plano de controle x plano de usuário
- Controle: AMF, SMF, UDM, AUSF, PCF, NRF, NSSF
	- Define quem é o usuário e o que ele pode fazer
	- Cria sessões, políticas e regras
	- Não carrega o tráfego pesado da aplicação
- Usuário: principalmente a UPF
	- Carrega os pacotes IP da aplicação
	- Aplica as regras recebidas do controle
	- Pode ser deslocado pra borda pra reduzir latência
## Data Network e DNN
- DN: rede acessada pela sessão PDU
- DNN: identificador usado pra selecionar a DN que o UE pediu
- DNN e network slice são conceitos diferentes, mas são usados juntos
- A SMF seleciona e configura a UPF que conecta o UE na DN
## Interfaces

| Interface | Conecta | Protocolo/tráfego | Função |
| --- | --- | --- | --- |
| N1 | UE–AMF (lógica) | NAS | Registro, autenticação, mobilidade e sessão |
| N2 | gNB-CU-CP–AMF | NGAP sobre SCTP/IP | Controle entre NG-RAN e 5GC |
| N3 | gNB-CU-UP–UPF | GTP-U sobre UDP/IP | Dados do usuário entre RAN e Core |
| N4 | SMF–UPF | PFCP sobre UDP/IP | Configuração e controle da UPF |
| N6 | UPF–DN | IP ou Ethernet | Conexão com internet, rede corporativa, MEC |
| N9 | UPF–UPF | Geralmente GTP-U | Dados entre UPFs diferentes |

- N1: não é enlace físico, é comunicação lógica de controle entre UE e AMF, transportando as mensagens NAS de registro, autenticação, segurança, mobilidade e gerenciamento de sessão PDU
- N2: participa do estabelecimento do contexto do UE, mobilidade, transporte das mensagens NAS, configuração de recursos pra sessão e liberação do contexto
- N3: cria túneis GTP-U pra transportar os pacotes das sessões PDU
- N4: por ela o SMF cria e remove regra na UPF, define encaminhamento, configura QoS, pede relatório de uso e controla sessão no plano de usuário
- N9: usada quando tem mais de uma UPF no caminho, apoia distribuição geográfica do plano de usuário, encaminhamento entre UPFs, mobilidade, acesso local/edge e topologia com UPF intermediária e âncora
## Segurança na SBA
- A flexibilidade da SBA cobra o preço em proteção de API, identidade e NF
- NFs se autenticam mutuamente e autorizam acesso aos serviços
- Identidade permanente do assinante protegida por SUPI/SUCI
- APIs exigem criptografia, controle de acesso, auditoria e monitoramento
- Slicing e virtualização exigem isolamento, atualização segura e governança
- A operação precisa atender requisito legal e regulatório
## Fechando
- AMF -> porta de entrada do controle, registro, NAS, mobilidade
- SMF -> gerencia sessão PDU e controla a UPF pela N4
- UPF -> encaminha pacote, é o plano de usuário
- UDM -> dado do assinante; AUSF -> autenticação
- PCF -> política de QoS e cobrança
- NRF -> catálogo das NFs, base da descoberta na SBA
- NSSF -> escolhe slice permitido e AMF candidata
- NEF -> porta pra aplicação externa; AF -> voz da aplicação
- NWDAF -> analytics, mas quem decide é quem consome
## Dicionário de siglas

| Sigla   | Significado                                           | O que é                                                   |
| ------- | ----------------------------------------------------- | --------------------------------------------------------- |
| 5GC     | 5G Core                                               | Núcleo da rede 5G, baseado em serviços                    |
| 5G-AKA  | 5G Authentication and Key Agreement                   | Procedimento de autenticação do 5G                        |
| AF      | Application Function                                  | Representa as necessidades da aplicação no Core           |
| AMF     | Access and Mobility Management Function               | Registro, NAS, conexão e mobilidade do UE                 |
| API     | Application Programming Interface                     | Interface pela qual as NFs se comunicam na SBA            |
| AUSF    | Authentication Server Function                        | Executa a autenticação do assinante, UDM comunica com ela |
| CU-CP   | Central Unit – Control Plane                          | Parte de controle da unidade central do gNB               |
| CU-UP   | Central Unit – User Plane                             | Parte de usuário da unidade central do gNB                |
| DN      | Data Network                                          | Rede acessada pela sessão PDU                             |
| DNN     | Data Network Name                                     | Identificador da DN solicitada pelo UE                    |
| EPC     | Evolved Packet Core                                   | Núcleo do 4G/LTE                                          |
| gNB     | Next Generation NodeB                                 | Estação rádio base do 5G                                  |
| GTP-U   | GPRS Tunnelling Protocol – User Plane                 | Protocolo de túnel dos dados do usuário (N3, N9)          |
| HSS     | Home Subscriber Server                                | Base de assinantes do EPC, equivalente à UDM              |
| MEC     | Multi-access Edge Computing                           | Computação na borda da rede                               |
| MME     | Mobility Management Entity                            | Controle de mobilidade do EPC, equivalente à AMF          |
| NAS     | Non-Access Stratum                                    | Sinalização direta entre UE e Core                        |
| NEF     | Network Exposure Function                             | Expõe capacidades da rede a aplicações externas           |
| NF      | Network Function                                      | Função de rede do 5GC                                     |
| NGAP    | NG Application Protocol                               | Protocolo de controle da N2                               |
| NG-RAN  | Next Generation Radio Access Network                  | Rede de acesso rádio do 5G                                |
| NRF     | Network Repository Function                           | Catálogo e descoberta de NFs                              |
| NSA     | Non-Standalone                                        | 5G apoiado no núcleo 4G                                   |
| NSSF    | Network Slice Selection Function                      | Seleção de network slice                                  |
| NWDAF   | Network Data Analytics Function                       | Coleta e análise de dados da rede                         |
| PCF     | Policy Control Function                               | Políticas de QoS, acesso e cobrança                       |
| PDU     | Protocol Data Unit                                    | Unidade de dados, dá nome à sessão PDU                    |
| PFCP    | Packet Forwarding Control Protocol                    | Protocolo da N4, entre SMF e UPF                          |
| PGW     | Packet Data Network Gateway                           | Gateway de saída do EPC                                   |
| QoS     | Quality of Service                                    | Qualidade de serviço                                      |
| RAN     | Radio Access Network                                  | Rede de acesso rádio                                      |
| SA      | Standalone                                            | 5G com núcleo 5G próprio                                  |
| SBA     | Service-Based Architecture                            | Arquitetura baseada em serviços                           |
| SCTP    | Stream Control Transmission Protocol                  | Transporte usado na N2                                    |
| SGW     | Serving Gateway                                       | Gateway de serviço do EPC                                 |
| SMF     | Session Management Function                           | Gerencia sessões PDU e controla a UPF                     |
| S-NSSAI | Single Network Slice Selection Assistance Information | Identificador de um network slice                         |
| SUCI    | Subscription Concealed Identifier                     | Versão cifrada do SUPI                                    |
| SUPI    | Subscription Permanent Identifier                     | Identificador permanente do assinante                     |
| UDM     | Unified Data Management                               | Dados de assinatura e identidades                         |
| UE      | User Equipment                                        | Equipamento do usuário                                    |
| UPF     | User Plane Function                                   | Encaminhamento de pacotes no plano de usuário             |
![[Pasted image 20260803101954.png]]