## Identificadores do assinante
- Conhecer as funções não basta, o que mostra como elas atuam juntas são os procedimentos
- Antes dos procedimentos vêm os identificadores, porque é com eles que a rede reconhece, protege e roteia o usuário
### SUPI - identidade permanente
- Subscription Permanent Identifier, identifica permanentemente a assinatura
- É o número de cadastro definitivo do assinante na operadora
- A rede precisa dele para:
	- localizar o perfil do assinante na UDM
	- executar a autenticação
	- verificar serviços e slices autorizados
	- aplicar política e cobrança
	- reconhecer o mesmo assinante mesmo que ele troque de aparelho ou de área
- Não deve trafegar em claro pela interface rádio
### SUCI - identidade protegida
- Subscription Concealed Identifier, representação protegida do SUPI
- Permite o UE dizer quem é sem expor a identidade permanente no rádio
- Usado quando:
	- o UE ainda não tem identidade temporária válida
	- a rede precisa descobrir quem é o assinante
	- é o primeiro registro, ou um novo registro em certas situações
- Quem desfaz a proteção e recupera o SUPI é a SIDF (Subscription Identifier De-concealing Function), associada à UDM
### 5G-GUTI - identidade temporária
- 5G Globally Unique Temporary Identifier, atribuído pela AMF depois que o UE é autenticado e registrado
- Passa a ser usado nas comunicações seguintes, evitando o UE ficar mandando SUPI ou SUCI novo toda hora
- Serve para:
	- identificar temporariamente o UE
	- proteger a privacidade
	- permitir a rede localizar o contexto do UE
	- encaminhar a sinalização para a AMF responsável
	- dificultar rastreamento prolongado
- Precisa ser renovado, senão o rastreamento volta a ser possível
- Sequência: primeiro contato UE -> SUCI -> rede; depois do registro a rede atribui o 5G-GUTI; contatos seguintes UE -> 5G-GUTI -> rede
### GPSI e PEI
- GPSI: Generic Public Subscription Identifier, identidade pública pela qual o assinante é conhecido por aplicações ou por outros usuários, tipicamente o número de telefone
- SUPI identifica a assinatura por dentro, GPSI representa o assinante por fora
- PEI: Permanent Equipment Identifier, identifica o equipamento e não a assinatura, pode estar relacionado ao IMEI
- SUPI -> quem é o assinante; PEI -> qual é o aparelho
- O PEI pode gerar consulta ao 5G-EIR para verificação do equipamento

| Identificador | O que representa | Quando é usado | Ponto de atenção |
| --- | --- | --- | --- |
| SUPI | identidade permanente da assinatura | autenticação, consulta ao perfil, autorização | não deve ir em claro pelo rádio |
| SUCI | representação protegida do SUPI | registro inicial ou sem identidade temporária válida | deixa a rede de origem recuperar o SUPI sem expor |
| 5G-GUTI | identidade temporária dada pela AMF | sinalizações e acessos posteriores | precisa ser renovado |
| GPSI | identificador público | exposição para aplicações e outros usuários | é a face externa, não serve para autenticar |
| PEI | identidade do equipamento | identificação e verificação do terminal | identifica o aparelho, não o usuário |

## Etapa 1 - acesso inicial à célula
- O UE precisa encontrar uma célula 5G, sincronizar e conseguir acesso ao meio rádio
- Participam UE e gNB (RU, DU e CU), camada física e MAC, e o procedimento de acesso aleatório
- Tudo aqui ainda é RAN, o Core nem sabe que esse UE existe
## Etapa 2 - conexão RRC
- Depois do acesso inicial o UE estabelece conexão RRC com a gNB
- Essa conexão é o caminho de sinalização que permite alcançar o Core
- O RRC gerencia conexão e configuração de rádio, e a mensagem RRC termina na gNB
- Dentro da sinalização RRC pode ir uma mensagem NAS destinada à AMF
- Participam UE e gNB, principalmente a CU-CP
## Etapa 3 - Registration Request
- Com o RRC de pé, o UE manda a solicitação de registro ao Core
- Mensagem principal: Registration Request, do protocolo NAS
- UE cria a mensagem NAS, o gNB apenas transporta, a AMF recebe e coordena o registro
- N1: UE -> AMF
## Etapa 4 - autenticação e segurança
- A AMF recebeu o pedido mas ainda precisa verificar se o assinante é legítimo e se tem autorização
- Participam:
	- AMF, coordenando
	- AUSF, executando a autenticação
	- UDM, fornecendo dados da assinatura
	- UE, respondendo aos desafios
- O que aparece nessa etapa: SUPI e SUCI, 5G-AKA, verificação da assinatura, geração de chaves, ativação da segurança NAS, proteção de integridade e cifragem
### Como a autenticação mútua funciona
- É mútua: verifica a legitimidade do assinante e também da rede
- O USIM (Universal Subscriber Identity Module) e a rede de origem guardam uma credencial secreta associada à assinatura
- USIM é a aplicação que armazena e usa as informações de identidade e autenticação do assinante, em 3G, 4G e 5G
- Participam AMF, AUSF e UDM/ARPF (Authentication Credential Repository and Processing Function)
- A rede manda um desafio, o UE verifica a rede e calcula a resposta
- UE e rede derivam chaves que protegem:
	- a sinalização NAS entre UE e AMF
	- a sinalização e os dados de camada de acesso entre UE e gNB
	- integridade e confidencialidade, conforme a configuração
- Objetivo: impedir acesso indevido e proteger a comunicação
## Etapa 5 - Registration Accept
- Autenticado e com segurança estabelecida, a AMF aceita o registro
- A AMF envia Registration Accept e o UE pode responder com Registration Complete
- Participam principalmente AMF e UDM, mais NSSF quando é preciso avaliar slices, PCF em políticas de acesso e mobilidade, e NRF para descoberta de funções
- No fim disso o UE:
	- é conhecido pelo Core
	- tem contexto na AMF
	- pode receber identidade temporária
	- conhece os slices autorizados
	- pode ser localizado e gerenciado pela rede
## RRC, registro e sessão PDU não são a mesma coisa
- RRC: conexão e configuração de rádio entre UE e gNB. Ter RRC significa só ter caminho de sinalização com a gNB, não significa estar registrado nem ter internet
- Registro: reconhecimento, autenticação e autorização no 5G Core. O Core aceitar o UE ainda não garante que exista sessão para transportar dado de aplicação
- Sessão PDU: conectividade com uma Data Network, é o que de fato carrega os dados
- RRC trata a relação com a RAN, o registro trata a relação com o Core, a sessão PDU trata a conectividade com a DN

| Situação | Registro | RRC | Sessão PDU |
| --- | --- | --- | --- |
| UE recém-ligado | não registrado | sem conexão | não estabelecida |
| UE disponível, sem usar dados | registrado | RRC_IDLE | pode estar estabelecida |
| UE transmitindo dados | registrado | RRC_CONNECTED | estabelecida |
| UE registrado, sem sessão de dados | registrado | RRC_IDLE ou CONNECTED | não estabelecida |

## Sessão PDU
### Solicitação
- Registrado, o UE solicita a sessão PDU para acessar uma Data Network, que pode ser a internet ou uma rede corporativa
- O UE pode informar:
	- DNN, identificando a rede de dados
	- S-NSSAI, identificando o slice
	- tipo de sessão: IPv4, IPv6 ou IPv4v6
- Fluxo: UE -> AMF -> SMF, e a SMF consulta política na PCF, dados de sessão na UDM e seleciona uma UPF
- Também participam NSSF (slice) e NRF (descoberta de uma SMF adequada)
### Configuração do caminho
- Decidido como a sessão será atendida, a rede precisa configurar o caminho efetivo dos pacotes
- A SMF seleciona a UPF, configura regra de encaminhamento, configura QoS e define como os pacotes devem ser tratados
- A UPF instala e executa essas regras e prepara o encaminhamento para a DN
- A gNB prepara os recursos de rádio e associa o tráfego de rádio ao túnel N3 correspondente
- A PCF é a origem das políticas que influenciam essas regras
- Relações principais:
	- SMF -- N4/PFCP -- UPF
	- AMF -- N2/NGAP -- gNB
	- gNB -- N3/GTP-U -- UPF
### Tráfego
- Com o plano de usuário configurado, os pacotes da aplicação finalmente trafegam
- Caminho: UE - Uu - gNB - N3 - UPF - N6 - DN
- Participam do transporte só UE, gNB, UPF e Data Network
- A UPF encaminha os pacotes, aplica filtragem, marcação e QoS, contabiliza tráfego quando configurada e conecta a sessão à DN correta
### O que a sessão carrega
- Pode transportar IPv4, IPv6, IPv4v6, Ethernet ou dados não estruturados
- Nas sessões IP a rede atribui ao UE um endereço ou prefixo
- O DNN identifica a Data Network associada à sessão
- A SMF gerencia a sessão e seleciona/configura a UPF
## Encapsulamento na N3
- A PDU do usuário é encapsulada em GTP-U (GPRS Tunnelling Protocol for the User Plane) para atravessar a rede de transporte
- A N3 normalmente usa GTP-U sobre UDP/IP
- TEID (Tunnel Endpoint Identifier): identifica o contexto do túnel na extremidade que recebe
- QFI (QoS Flow Identifier): identifica o QoS Flow
- gNB e UPF aplicam o tratamento configurado para aquele tráfego
- Falha na N3 impede o tráfego mesmo com o UE registrado, e as causas típicas são:
	- endereço da UPF ou da gNB incorreto
	- porta UDP 2152 bloqueada
	- TEID ou regra de encaminhamento incorreta
	- rota IP inexistente entre gNB e UPF
	- firewall bloqueando GTP-U
## Protocolos e testes

| Protocolo ou teste | Comunicação | Exemplo | O que permite verificar |
| --- | --- | --- | --- |
| NAS | UE - AMF, logicamente pela N1 | Registration Request | registro, autenticação e pedido de sessão PDU |
| NGAP | gNB - AMF pela N2 | Initial UE Message | transporte do NAS e coordenação RAN-Core |
| PFCP | SMF - UPF pela N4 | Session Establishment Request | criação e atualização das regras do plano de usuário |
| GTP-U | gNB - UPF pela N3 | PDU do usuário encapsulada | funcionamento do túnel e transporte dos dados |
| ICMP | UE - destino IP | ping | alcance básico e tempo de resposta |
| iperf3 | cliente - servidor | teste TCP ou UDP | taxa, perda e variação temporal |

## Diagnóstico por etapa
- A lógica é sempre a mesma: identifica a última etapa concluída com sucesso, e a falha está logo depois dela

| Sintoma | Área provável | Primeiras verificações |
| --- | --- | --- |
| não encontra célula | RAN | rádio, frequência, sincronismo, PLMN |
| não registra | controle de acesso | AMF, NAS/NGAP, autenticação, assinatura |
| não cria sessão PDU | gerenciamento da sessão | SMF, DNN, slice, UPF |
| não trafega | plano do usuário | N3, GTP-U, N6, rotas, firewall |
| desempenho ruim | QoS e capacidade | rádio, transporte, UPF e aplicação |

- Detalhando cada caso:
	- não seleciona célula -> cobertura, frequência, sincronismo, PLMN e configuração da RAN
	- encontra a célula mas não registra -> AMF, sinalização NAS/NGAP, autenticação, assinatura e parâmetros de segurança
	- registra mas não cria sessão -> SMF, DNN, slice, políticas, seleção da UPF e dados de assinatura
	- sessão estabelecida mas sem tráfego -> túnel N3, regras da UPF, roteamento, N6, NAT e firewall
	- trafega mal -> condições de rádio, QoS, congestionamento, transporte, capacidade da UPF e aplicação
## Fechando
- SUPI -> identidade permanente; SUCI -> ela protegida; 5G-GUTI -> a temporária que vem depois
- SIDF -> quem desfaz a proteção do SUCI, junto da UDM
- RRC -> relação com a RAN; registro -> relação com o Core; sessão PDU -> relação com a DN
- 5G-AKA -> autenticação mútua, com AMF coordenando, AUSF executando e UDM/ARPF guardando a credencial
- N4/PFCP -> a SMF configura a UPF; N2/NGAP -> AMF e gNB; N3/GTP-U -> dado do usuário com TEID e QFI
- Registrado não é sinônimo de conectado, e é essa distinção que o diagnóstico usa
## Dicionário de siglas

| Sigla   | Significado                                                  | O que é                                                     |
| ------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| 5G-AKA  | 5G Authentication and Key Agreement                          | procedimento de autenticação mútua do 5G                    |
| 5G-EIR  | 5G Equipment Identity Register                               | base para verificação do equipamento pelo PEI               |
| 5G-GUTI | 5G Globally Unique Temporary Identifier                      | identidade temporária atribuída pela AMF                    |
| AMF     | Access and Mobility Management Function                      | registro, NAS, conexão e mobilidade                         |
| ARPF    | Authentication Credential Repository and Processing Function | guarda e processa a credencial de autenticação, junto à UDM |
| AUSF    | Authentication Server Function                               | executa a autenticação do assinante                         |
| CU      | Central Unit                                                 | unidade central do gNB                                      |
| CU-CP   | Central Unit – Control Plane                                 | parte de controle da CU, onde fica o RRC                    |
| DN      | Data Network                                                 | rede acessada pela sessão PDU                               |
| DNN     | Data Network Name                                            | identificador da DN solicitada                              |
| DU      | Distributed Unit                                             | unidade distribuída do gNB                                  |
| gNB     | Next Generation NodeB                                        | estação rádio base do 5G                                    |
| GPSI    | Generic Public Subscription Identifier                       | identidade pública do assinante, tipo o telefone            |
| GTP-U   | GPRS Tunnelling Protocol – User Plane                        | encapsula o dado do usuário na N3                           |
| ICMP    | Internet Control Message Protocol                            | protocolo do ping                                           |
| IMEI    | International Mobile Equipment Identity                      | identidade do aparelho, base do PEI                         |
| MAC     | Medium Access Control                                        | camada de acesso ao meio                                    |
| NAS     | Non-Access Stratum                                           | sinalização lógica entre UE e Core                          |
| NGAP    | NG Application Protocol                                      | protocolo de controle da N2                                 |
| NRF     | Network Repository Function                                  | registro e descoberta de NFs                                |
| NSSF    | Network Slice Selection Function                             | seleção de network slice                                    |
| PCF     | Policy Control Function                                      | políticas de QoS, acesso e cobrança                         |
| PDU     | Protocol Data Unit                                           | unidade de dados, dá nome à sessão PDU                      |
| PEI     | Permanent Equipment Identifier                               | identidade permanente do equipamento                        |
| PFCP    | Packet Forwarding Control Protocol                           | protocolo da N4, entre SMF e UPF                            |
| PLMN    | Public Land Mobile Network                                   | identificação da rede da operadora                          |
| QFI     | QoS Flow Identifier                                          | identifica o QoS Flow dentro do túnel                       |
| QoS     | Quality of Service                                           | qualidade de serviço                                        |
| RAN     | Radio Access Network                                         | rede de acesso rádio                                        |
| RRC     | Radio Resource Control                                       | controla conexão e configuração de rádio, termina na gNB    |
| RU      | Radio Unit                                                   | unidade de rádio do gNB                                     |
| SA      | Standalone                                                   | 5G com núcleo 5G próprio                                    |
| SIDF    | Subscription Identifier De-concealing Function               | recupera o SUPI a partir do SUCI, associada à UDM           |
| SMF     | Session Management Function                                  | gerencia a sessão PDU e controla a UPF                      |
| S-NSSAI | Single Network Slice Selection Assistance Information        | identificador de um network slice                           |
| SUCI    | Subscription Concealed Identifier                            | versão protegida do SUPI                                    |
| SUPI    | Subscription Permanent Identifier                            | identidade permanente da assinatura                         |
| TEID    | Tunnel Endpoint Identifier                                   | identifica o contexto do túnel GTP-U                        |
| UDM     | Unified Data Management                                      | dados de assinatura e identidades                           |
| UE      | User Equipment                                               | equipamento do usuário                                      |
| UPF     | User Plane Function                                          | encaminha os pacotes no plano de usuário                    |
| USIM    | Universal Subscriber Identity Module                         | aplicação no cartão que guarda identidade e credencial      |
| Uu      | interface rádio                                              | enlace entre UE e gNB                                       |
