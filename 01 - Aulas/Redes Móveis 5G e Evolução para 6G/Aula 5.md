## Lendo o log e a captura
- O log do Core mostra a sequência do registro:
	- o gNB apresentou o UE à AMF por uma InitialUEMessage
	- a AMF criou um contexto NGAP para esse UE
	- a mensagem NAS Registration Request chegou à AMF
	- a AMF reconheceu o UE por uma identidade temporária
	- o registro foi concluído e a rede enviou uma atualização de configuração
	- aparecem o DNN solicitado e o S-NSSAI
- Na captura de pacotes o que se vê é o plano de usuário:
	- o pacote IP do usuário viaja dentro de um túnel GTP-U
	- TEID identifica o túnel, QFI identifica o QoS Flow
	- o endereço 10.45.0.2 tem conectividade IP e o tráfego usa QFI 1
	- pedido ICMP recebendo resposta -> comunicação bidirecional, plano de usuário funcional naquele trecho
- Serve como prova prática do que a aula anterior descreveu: registro é sinalização, tráfego é túnel
## QoS
- Nem todo tráfego deve ser tratado igual. Vídeo, controle industrial, sensor e navegação têm requisitos diferentes de taxa, atraso, jitter, perda e confiabilidade
- A QoS traduz requisito de serviço em regra de prioridade, encaminhamento, agendamento e alocação de recurso
- Sem QoS e gestão de recurso um slice pode existir logicamente e não entregar o desempenho esperado
### QoS Flow, QFI, 5QI e DRB
- QoS Flow: menor granularidade do 5GS para aplicar tratamento diferenciado ao tráfego do usuário
- QFI: identifica um QoS Flow dentro da sessão PDU
- 5QI: referencia um conjunto de características de encaminhamento e desempenho daquele fluxo
- DRB: transporta o tráfego pela interface rádio. Um ou mais QoS Flows podem ser mapeados para um mesmo DRB
- Uma sessão PDU pode conter vários QoS Flows:
```
Sessão PDU
├── QoS Flow 1: controle industrial
├── QoS Flow 2: vídeo
└── QoS Flow 3: dados comuns
```

| Elemento | Função | Exemplo | Cuidado conceitual |
| --- | --- | --- | --- |
| QoS Flow | unidade lógica que recebe tratamento específico | voz, vídeo, controle industrial | é a menor granularidade de QoS do 5GS |
| QFI | identifica o QoS Flow na sessão PDU | QFI 1, QFI 5 | não define sozinho o tratamento |
| 5QI | indica encaminhamento e desempenho | prioridade, atraso, perda | não representa diretamente taxa de dados |
| GBR | requisitos associados a taxa garantida | voz, tempo real | pode exigir reserva e controle de recurso |
| ARP | controla admissão, retenção e preempção | serviço prioritário ou de emergência | não é prioridade de envio de cada pacote |

- Cada QoS Flow pode ter QFI, 5QI, ARP e, nos GBR, GFBR e MFBR
### Da aplicação até o rádio
- A cadeia tem três estágios: a aplicação expressa requisito de serviço, o Core transforma em política e parâmetro de QoS, a RAN converte em decisão dinâmica de rádio
- A aplicação fala em linguagem de serviço: preciso de baixa latência, não posso perder mensagem, preciso de taxa mínima, esse fluxo é mais importante que um download comum
- O Core considera requisito da aplicação, assinatura, política da operadora, slice, disponibilidade de recurso e regra do serviço
	- AF representa as necessidades da aplicação
	- NEF expõe capacidades do Core com segurança, quando necessário
	- PCF decide as políticas
	- SMF aplica as decisões à sessão e configura o plano de usuário
### SDAP e DRB
- A SDAP recebe os pacotes associados aos QoS Flows e faz o mapeamento para os DRBs
- Vários QoS Flows podem compartilhar um DRB, ou fluxos diferentes podem ir para DRBs distintos
- A SDAP não escolhe PRB nem MCS. Ela só organiza por qual bearer de rádio o tráfego vai
- O DRB é o caminho lógico entre UE e gNB, já com o tratamento de rádio adequado
- Cadeia: QoS Flow -> SDAP -> DRB -> RLC/MAC/PHY
### O escalonador
- É onde o tratamento lógico vira decisão concreta de rádio
- Decide qual UE atender, qual fluxo transmitir, em qual slot, quantos PRBs e qual MCS
- Considera prioridade e QoS, quantidade de dados pendentes, qualidade do canal, CQI e MCS possíveis, retransmissão HARQ, carga da célula, PRBs disponíveis, número de UEs concorrentes e restrição de potência e tempo
- Recursos físicos que saem no fim: PRB, símbolo OFDM, slot, MCS, potência, camada MIMO, retransmissão HARQ
- Para entregar a mesma taxa:
	- canal bom -> MCS mais alto -> menos PRBs
	- canal ruim -> MCS mais baixo -> mais PRBs
- Resumindo a divisão: o parâmetro de QoS diz o comportamento desejado, o escalonador decide o recurso necessário naquele instante
## Network slicing
- Slice é uma rede lógica configurada para atender requisito específico de serviço e de usuário
- Pode abranger RAN, Core, transporte, edge e sistemas de gerenciamento
- Pode usar recurso compartilhado, reservado ou dedicado
- Está associado a requisito de desempenho, segurança, isolamento e SLA
- Não se resume a VLAN, APN ou DNN
```
Infraestrutura física compartilhada
├── Slice 1: internet móvel
├── Slice 2: automação industrial
└── Slice 3: comunicação de emergência
```

| Conceito | O que representa | Exemplo | Não confundir com |
| --- | --- | --- | --- |
| Network slice | rede lógica com funções, recursos e políticas | slice industrial, slice de banda larga | não é só uma identificação ou segmentação de transporte |
| DNN | identifica a Data Network que o UE quer acessar | internet, empresa.local, mec.fabrica | não define sozinho isolamento, QoS ou slice |
| APN | identifica a rede de dados no EPC/4G | internet.operadora | é análogo ao DNN, mas não equivale a slicing |
| VLAN | segmentação lógica de camada 2 | separar departamentos numa rede Ethernet | não fornece rede lógica fim a fim orientada a serviço |

### S-NSSAI, SST e SD
- S-NSSAI: identifica um slice selecionável na PLMN
- SST: indica o tipo de comportamento e serviço esperado do slice
- SD: opcional, diferencia slices que têm o mesmo SST
- NSSF: auxilia na seleção dos slices permitidos e de uma AMF compatível
### Como o slice é escolhido
1. O UE informa qual slice gostaria de usar, normalmente indicando um S-NSSAI ou um conjunto deles. Ele não cria nem escolhe sozinho o slice final
2. A AMF é o primeiro ponto de decisão. Ela não aceita automaticamente: confere se o assinante tem permissão, se o slice está disponível naquela área, se roaming e política permitem, e se o pedido faz sentido para a sessão
3. A NSSF entra como apoio: quais slices estão disponíveis para esse usuário, qual é permitido naquele contexto, quais AMFs ou conjuntos de funções são compatíveis. Ela não cria o slice nem executa a sessão
4. Definido o slice, a rede escolhe as funções compatíveis: AMF adequada, SMF para a sessão, UPF mais apropriada, políticas da PCF e conexão com o DNN correspondente
5. A sessão PDU passa a funcionar segundo as características do slice: política específica, QoS diferenciada, UPF no edge ou centralizada, roteamento próprio, isolamento lógico e tratamento particular na RAN e no Core
- É aí que o slice deixa de ser uma identificação e passa a influenciar o comportamento real da rede
### Isolamento: dedicar ou compartilhar
- Mais dedicação:
	- função, capacidade ou infraestrutura exclusivas do slice
	- reduz interferência de outros serviços
	- facilita previsibilidade e isolamento operacional
	- aumenta custo e reduz o aproveitamento da infraestrutura
	- se justifica quando segurança, desempenho ou disponibilidade exigem
- Mais compartilhamento:
	- slices diferentes usam funções ou infraestrutura comuns
	- o isolamento vem de política, segurança, quota, QoS e controle de acesso
	- melhora eficiência e utilização
	- exige planejamento de capacidade, monitoramento e controle de congestionamento
	- pode até atender serviço crítico, desde que as garantias sejam implementadas direito
- Ou seja, isolamento forte não é automaticamente a melhor solução, é uma escolha com preço
### Perfis de serviço

| Perfil | Requisitos predominantes | Exemplos | Observação |
| --- | --- | --- | --- |
| eMBB | capacidade, cobertura e experiência de banda larga | FWA, vídeo, XR, grandes eventos | taxa alta predomina, mas não é o único requisito |
| URLLC | baixo atraso, alta confiabilidade e disponibilidade | automação industrial, controle remoto, proteção de sistemas | edge e reserva ajudam, mas não são obrigatórios sempre |
| mMTC/MIoT | densidade de dispositivos, eficiência energética, pouca sinalização | sensores, medidores, monitoramento ambiental | cada dispositivo gera pouco tráfego |
| Corporativo/campus | segurança, controle, cobertura local e SLA | empresa, hospital, universidade, fábrica | é perfil de negócio, não um SST padronizado isolado |

## Edge e local breakout
- A latência cai quando a UPF e a aplicação ficam mais perto do usuário
- A UPF pode ser implantada num campus, numa empresa ou num data center de edge
- Local breakout: encaminhar o tráfego direto para uma Data Network próxima
- Aplicação sensível a latência pode rodar numa infraestrutura MEC
- O dado pode ser encaminhado localmente enquanto a decisão de controle continua nas funções centrais do Core
- O preço: implantação distribuída exige orquestração, segurança, monitoramento e capacidade computacional em cada ponto
## Redes privativas
- NPN pode operar de forma independente ou apoiada numa rede pública
- SNPN: rede privativa standalone, mais independente
- PNI-NPN: rede não pública integrada à rede pública
- A escolha depende de cobertura, espectro, operação, SLA e integração
- Cenários típicos: indústria, mineração, portos e campi

| Aspecto | PNI-NPN (sobre a rede da operadora) | SNPN (independente) |
| --- | --- | --- |
| Quem fornece | a operadora fornece conectividade para uso restrito | não depende das funções de uma PLMN |
| Recursos | pode usar slice dedicado ao cliente, com RAN, Core e transporte parcialmente compartilhados | pode ter RAN, 5G Core, UPF e aplicações próprias |
| Controle | política, SLA, segurança e acesso definidos para o serviço privado | maior autonomia sobre configuração, dados e operação |
| Quando usar | quando a cobertura e a infraestrutura da operadora atendem o cenário | quando se quer independência, com infra local, nuvem privada ou gerenciada |
| Cuidado | depende do contrato e do que é compartilhado | exige definir claramente responsabilidade de operação, segurança e manutenção |

### Verticais

| Vertical | Requisitos | Casos de uso | Desafios |
| --- | --- | --- | --- |
| Indústria | baixa latência, confiabilidade, disponibilidade, segurança | robôs, PLCs, AGVs, inspeção por vídeo | interferência, mobilidade interna, integração OT/IT, continuidade |
| Agronegócio | cobertura ampla, baixo consumo, área remota | sensores, máquinas agrícolas, monitoramento de animais | distância, energia limitada, transporte |
| Saúde | disponibilidade, privacidade, proteção de dados | monitoramento, telemedicina, ativos hospitalares | dado sensível, integração com sistema clínico, criticidade variável |
| Smart grid | resiliência, segurança, resposta rápida | proteção, automação, medição, manutenção | infraestrutura crítica, cobertura ampla, cibersegurança |
| Cidades inteligentes | escalabilidade, diversidade de dispositivos, integração | câmeras, sensores, iluminação, mobilidade | interoperabilidade, volume de dados, múltiplos responsáveis |

### SLA
- A meta do SLA precisa ser mensurável e sustentada pela arquitetura, pela operação e pelo monitoramento
- Definir meta mensurável de latência, disponibilidade, cobertura, taxa, perda e confiabilidade
- Traduzir essas metas em QoS, slicing, edge, capacidade, segurança e redundância
- Monitorar indicador, detectar violação e executar ação corretiva
- Validar o serviço ponta a ponta: rádio, transporte, Core, edge e aplicação
## Virtualização e cloud-native
- Rede móvel moderna depende de infraestrutura computacional compartilhada: servidor, armazenamento, conectividade e acelerador
- Virtualização e contêiner permitem executar função de rede sobre plataforma compartilhada
- Cloud e automação deixam a implantação e a expansão mais flexíveis
- Só que o requisito de telecom continua o mesmo: desempenho, disponibilidade, baixa latência e sincronismo
- A evolução não é só mudar o lugar onde o software roda. É separar software de hardware, modularizar função e automatizar o ciclo de vida

| Modelo | Como a função é executada | Exemplo | Consideração |
| --- | --- | --- | --- |
| PNF | software e hardware integrados em equipamento dedicado | gateway ou elemento de Core legado | menor portabilidade, expansão presa ao equipamento |
| VNF | função virtualizada, normalmente em uma ou mais VMs | AMF ou EPC virtualizado | exige hipervisor e gerenciamento da infra virtual |
| CNF | função implementada para rodar em contêiner | AMF ou SMF em Kubernetes | exige orquestração, observabilidade e automação maduras |
| Cloud-native | abordagem de modularidade, automação, resiliência e operação declarativa | microserviços, Kubernetes, CI/CD | não significa apenas hospedar software numa nuvem |

### As camadas, de baixo para cima
- Infraestrutura: a base material. Processamento, aceleração de pacote, armazenamento, comunicação e disponibilidade física. Pode estar em data center central, regional, edge, fábrica/campus ou nuvem privada e pública
- Virtualização: organiza e abstrai o recurso físico. Com VM o hipervisor divide o servidor físico; com contêiner os processos ficam isolados mas compartilham o sistema operacional do host
- Funções de rede: AMF, SMF, UPF, PCF, CU e DU, implementadas como PNF, VNF ou CNF. Ter várias instâncias dá redundância, distribuição geográfica, capacidade e continuidade em caso de falha
- Serviços: o que as funções entregam juntas, e não um novo conjunto de equipamento. Registro, mobilidade, sessão, QoS e encaminhamento
- Aplicações: quem usa a conectividade. Internet, IoT, automação industrial, videoconferência, telemedicina, MEC, sistemas corporativos, veículos conectados
### VM x contêiner
- VM: roda um sistema operacional convidado completo sobre hardware virtualizado, isolamento mais forte, consome mais memória, armazenamento e tempo de inicialização. É o modelo típico de VNF
- Contêiner: isola processos mas compartilha o kernel do host, mais leve, inicia mais rápido, facilita escala horizontal e microserviços. Exige orquestração, observabilidade, controle de rede e segurança adequados
### Kubernetes
- Plataforma de orquestração que distribui Pods entre os nós do cluster e tenta manter o estado desejado da aplicação
- Agenda Pods e workloads nos nós disponíveis
- Recria ou reposiciona Pod quando há falha
- Permite escala, atualização gradual e controle declarativo
- Integra com rede, armazenamento, segurança e observabilidade
- Ressalva importante: ele orquestra contêiner, não resolve sozinho requisito de telecom. Desempenho, latência e sincronismo precisam ser validados
### Observabilidade e automação
- Observabilidade mostra o estado da rede, automação age sobre esse estado
- Logs: registram evento discreto -> inicialização, falha, alteração, mensagem processada, rejeição e erro
- Métricas: valor quantitativo ao longo do tempo -> CPU, memória, tráfego, latência, perda, quantidade de sessões, taxa de falha
- Traces: acompanham uma requisição atravessando vários componentes
- Automação: cria instância, reinicia componente, modifica capacidade, aplica configuração, atualiza software, reage a alarme
- Mudança automatizada exige teste, controle e reversão segura
## Open RAN

| Abordagem | Característica | Exemplo | Ponto de atenção |
| --- | --- | --- | --- |
| RAN tradicional | hardware e software integrados, normalmente de um fornecedor só | banda-base e rádio proprietários | pouca portabilidade, dependência do fornecedor |
| C-RAN | centraliza ou agrupa o processamento de banda-base | pool de BBUs ou DUs atendendo várias RUs | fronthaul exige capacidade, baixa latência e sincronismo |
| vRAN | funções de RAN como software sobre infra computacional | CU e DU virtualizadas em servidores | tempo real e aceleração são desafio |
| Cloud RAN | práticas cloud-native, automação e infra distribuída | CU/DU como VNF ou CNF em edge cloud | não implica automaticamente interface aberta |
| Open RAN | desagregação com interface aberta e interoperabilidade | RU de um fornecedor e DU/CU de outro | integração, teste e responsabilidade multivendor complexos |

- Open RAN é o conceito amplo: desagregar componentes da RAN e usar interface aberta ou padronizada para permitir interoperabilidade, automação e mais diversidade de fornecedor
- O-RAN é a arquitetura e o conjunto de especificações desenvolvidos pela O-RAN Alliance. São coisas diferentes e vale não misturar
### Componentes O-RAN

| Componente | Papel | Funções típicas | Ponto de atenção |
| --- | --- | --- | --- |
| O-RU | unidade de rádio ligada à antena | RF, conversão e parte da Low-PHY | capacidade, latência e sincronismo no Open Fronthaul |
| O-DU | funções distribuídas e sensíveis ao tempo | High-PHY, MAC, RLC, escalonamento, HARQ | desempenho em tempo real e aceleração |
| O-CU-CP | funções centralizadas de controle | RRC e PDCP de controle | mobilidade, sinalização e disponibilidade |
| O-CU-UP | funções centralizadas de usuário | SDAP e PDCP de usuário | capacidade e encaminhamento |
| Near-RT RIC | otimiza a RAN perto do tempo real | xApps, controle e análise via E2 | conflito entre decisões e desempenho |
| Non-RT RIC | políticas e otimização de horizonte longo | rApps, dado enriquecido, modelo de IA/ML | qualidade do dado e validação das políticas |
| SMO | gerencia e orquestra os elementos O-RAN | configuração, falha, desempenho, ciclo de vida | operação fim a fim em ambiente multivendor |
| O-Cloud | infraestrutura de nuvem que hospeda as funções | computação, rede, armazenamento, aceleradores | latência, sincronismo e desempenho determinístico |

### Interfaces

| Interface | Conecta | Papel | Ponto de atenção |
| --- | --- | --- | --- |
| Open Fronthaul | O-RU - O-DU | controle, usuário, sincronismo e gerenciamento | capacidade, temporização, interoperabilidade |
| E2 | Near-RT RIC - nós da RAN | coleta dado e permite controle por xApps | latência, segurança, conflito de controle |
| A1 | Non-RT RIC - Near-RT RIC | política, informação enriquecida, suporte a IA/ML | coerência das políticas e dos modelos |
| O1 | SMO - elementos gerenciados | configuração, falha, desempenho, inventário | compatibilidade multivendor |
| O2 | SMO - O-Cloud | infraestrutura e ciclo de vida dos workloads | integração entre cloud e funções de RAN |

- Cada interface aberta é também uma fronteira de integração, e é aí que aparece o custo
### RIC, xApps e rApps
- Near-RT RIC executa controle e otimização quase em tempo real, e é onde rodam os xApps
- Non-RT RIC, normalmente dentro do SMO, apoia política, analítica, treinamento e orientação de longo prazo, e é onde rodam os rApps
- Fluxo: dados da RAN -> Non-RT RIC/rApps -> políticas -> Near-RT RIC/xApps -> ações na RAN
- IA na RAN pode apoiar previsão e otimização, mas depende de dado confiável, validação, segurança e supervisão operacional
### Benefícios e desafios
- A favor:
	- interoperabilidade e menos dependência de um fornecedor só
	- evolução e inovação baseadas em software
	- automação e otimização com SMO, RIC, xApps e rApps
	- flexibilidade para distribuir função entre site, edge e data center
	- possibilidade de escolher componente especializado
- Contra:
	- integração e teste multivendor complexos
	- garantir desempenho, latência, jitter e sincronismo
	- superfície de ataque e cadeia de suprimentos maiores
	- responsabilidade dividida entre fornecedores
	- necessidade de observabilidade e diagnóstico fim a fim
- A economia depende de escala, integração, automação, contrato, maturidade dos produtos e custo operacional. Não é ganho automático
### Segurança
- Mais interface, API e componente distribuído amplia a superfície de ataque
- API e interface aberta exigem autenticação, autorização, criptografia e controle de acesso
- Função, contêiner e planos de rede precisam continuar isolados
- Software, imagem de contêiner e componente de terceiro precisam ser verificados
- Credencial, certificado, chave e segredo precisam de ciclo de vida controlado
- Vulnerabilidade precisa ser identificada, corrigida e monitorada continuamente
- Log e evento de segurança devem ser correlacionados entre RAN, cloud e sistemas de gerenciamento
### Por que virtualizar RAN é difícil
- Parte do processamento tem prazo rígido e precisa de comportamento temporal previsível
- Tempo, jitter e sincronismo: não basta média de processamento baixa, a variação também precisa ser controlada
- Camada física: codificação, decodificação, FFT, beamforming e MIMO exigem muita capacidade e resultado previsível
- Aceleradores: FPGA, GPU, SmartNIC, DPDK. Virtualizar não significa eliminar hardware especializado
- Validação: benchmark isolado não basta. Testar carga máxima, latência, jitter, sincronismo, falha, interoperabilidade e desempenho no ambiente real
## Fechando
- QoS Flow -> menor unidade de tratamento; QFI identifica, 5QI caracteriza, DRB transporta no rádio
- SDAP -> mapeia QoS Flow em DRB; escalonador -> transforma QoS em PRB, MCS e slot
- Slice -> rede lógica fim a fim, não é DNN, não é APN, não é VLAN
- S-NSSAI = SST (+ SD); UE pede, AMF autoriza, NSSF apoia, e o slice passa a moldar a sessão
- Isolamento é escolha com preço, não é sempre melhor dedicar
- Edge -> UPF perto do usuário e local breakout, controle continua central
- SNPN -> privativa independente; PNI-NPN -> privativa apoiada na rede pública
- PNF -> VNF -> CNF -> cloud-native é a linha da desagregação de software
- Open RAN -> conceito de desagregação; O-RAN -> as especificações da O-RAN Alliance
- RIC -> onde a otimização programável mora: xApps no Near-RT, rApps no Non-RT
## Dicionário de siglas

| Sigla | Significado | O que é |
| --- | --- | --- |
| 5QI | 5G QoS Identifier | referencia as características de desempenho de um QoS Flow |
| A1 | interface A1 | liga Non-RT RIC ao Near-RT RIC, leva políticas |
| AF | Application Function | representa as necessidades da aplicação |
| AGV | Automated Guided Vehicle | veículo autônomo de chão de fábrica |
| AMF | Access and Mobility Management Function | registro, acesso e mobilidade |
| APN | Access Point Name | identifica a rede de dados no 4G, análogo ao DNN |
| ARP | Allocation and Retention Priority | controla admissão, retenção e preempção |
| BBU | Baseband Unit | unidade de banda-base da RAN tradicional |
| CI/CD | Continuous Integration / Continuous Delivery | prática de integração e entrega contínuas |
| CNF | Cloud-native Network Function | função de rede feita para rodar em contêiner |
| CQI | Channel Quality Indicator | indicador de qualidade do canal reportado pelo UE |
| C-RAN | Centralized/Cloud RAN | centralização do processamento de banda-base |
| CU | Central Unit | camadas superiores do gNB |
| DN | Data Network | rede acessada pela sessão PDU |
| DNN | Data Network Name | identifica a DN solicitada |
| DPDK | Data Plane Development Kit | biblioteca de aceleração de pacotes |
| DRB | Data Radio Bearer | caminho lógico dos dados entre UE e gNB |
| DU | Distributed Unit | funções da RAN sensíveis a tempo |
| E2 | interface E2 | liga o Near-RT RIC aos nós da RAN |
| eMBB | enhanced Mobile Broadband | perfil de banda larga móvel |
| EPC | Evolved Packet Core | núcleo do 4G |
| FFT | Fast Fourier Transform | transformada usada no processamento OFDM |
| FPGA | Field Programmable Gate Array | hardware reconfigurável usado como acelerador |
| FWA | Fixed Wireless Access | acesso fixo sem fio |
| GBR | Guaranteed Bit Rate | fluxo com taxa garantida |
| GFBR | Guaranteed Flow Bit Rate | taxa garantida do fluxo GBR |
| GPU | Graphics Processing Unit | acelerador usado em processamento paralelo |
| GTP-U | GPRS Tunnelling Protocol – User Plane | encapsula o dado do usuário na N3 |
| HARQ | Hybrid Automatic Repeat Request | retransmissão rápida na camada MAC |
| IA/ML | Inteligência Artificial / Machine Learning | modelos usados em otimização de rede |
| ICMP | Internet Control Message Protocol | protocolo do ping |
| MAC | Medium Access Control | camada de acesso ao meio, faz escalonamento |
| MCS | Modulation and Coding Scheme | esquema de modulação e codificação |
| MEC | Multi-access Edge Computing | computação na borda |
| MFBR | Maximum Flow Bit Rate | taxa máxima do fluxo GBR |
| MIMO | Multiple Input Multiple Output | múltiplas antenas e camadas espaciais |
| MIoT | Massive IoT | IoT massiva, mesmo perfil do mMTC |
| mMTC | massive Machine Type Communications | muitos dispositivos, pouco tráfego cada |
| NAS | Non-Access Stratum | sinalização entre UE e Core |
| Near-RT RIC | Near Real-Time RIC | controle e otimização quase em tempo real, hospeda xApps |
| NEF | Network Exposure Function | expõe capacidades do Core por API |
| NGAP | NG Application Protocol | protocolo de controle da N2 |
| Non-RT RIC | Non Real-Time RIC | políticas e otimização de horizonte longo, hospeda rApps |
| NPN | Non-Public Network | rede não pública, privativa |
| NSSF | Network Slice Selection Function | apoia a seleção de slice e de AMF |
| O1 | interface O1 | gerenciamento entre SMO e elementos O-RAN |
| O2 | interface O2 | gerenciamento entre SMO e O-Cloud |
| O-Cloud | O-RAN Cloud | infraestrutura de nuvem que hospeda as funções O-RAN |
| O-CU-CP | O-RAN Central Unit – Control Plane | RRC e PDCP de controle |
| O-CU-UP | O-RAN Central Unit – User Plane | SDAP e PDCP de usuário |
| O-DU | O-RAN Distributed Unit | High-PHY, MAC, RLC e escalonamento |
| OFDM | Orthogonal Frequency Division Multiplexing | modulação multiportadora do 5G |
| O-RU | O-RAN Radio Unit | rádio ligado à antena, RF e Low-PHY |
| OT/IT | Operational Technology / Information Technology | mundo do chão de fábrica e mundo de TI |
| PCF | Policy Control Function | decide as políticas |
| PDCP | Packet Data Convergence Protocol | cifragem, compressão de cabeçalho e ordenação |
| PDU | Protocol Data Unit | unidade de dados, dá nome à sessão PDU |
| PHY | Physical Layer | camada física |
| PLC | Programmable Logic Controller | controlador industrial |
| PLMN | Public Land Mobile Network | rede móvel pública, a rede da operadora |
| PNF | Physical Network Function | função em hardware dedicado |
| PNI-NPN | Public Network Integrated NPN | rede privativa apoiada na rede pública |
| PRB | Physical Resource Block | bloco de recurso físico, unidade de alocação no rádio |
| QFI | QoS Flow Identifier | identifica o QoS Flow dentro da sessão PDU |
| QoS | Quality of Service | qualidade de serviço |
| rApp | rApp | aplicação que roda no Non-RT RIC/SMO |
| RAN | Radio Access Network | rede de acesso rádio |
| RF | Radio Frequency | parte de radiofrequência |
| RIC | RAN Intelligent Controller | controlador programável da RAN |
| RLC | Radio Link Control | segmentação e retransmissão no rádio |
| RRC | Radio Resource Control | controla conexão e configuração de rádio |
| RU | Radio Unit | unidade de rádio |
| SD | Slice Differentiator | diferencia slices com o mesmo SST |
| SDAP | Service Data Adaptation Protocol | mapeia QoS Flow em DRB |
| SLA | Service Level Agreement | acordo de nível de serviço |
| SmartNIC | Smart Network Interface Card | placa de rede com processamento próprio |
| SMF | Session Management Function | gerencia a sessão PDU |
| SMO | Service Management and Orchestration | gerencia e orquestra os elementos O-RAN |
| SNPN | Standalone Non-Public Network | rede privativa independente |
| S-NSSAI | Single Network Slice Selection Assistance Information | identifica um slice selecionável na PLMN |
| SST | Slice/Service Type | tipo de comportamento esperado do slice |
| TEID | Tunnel Endpoint Identifier | identifica o contexto do túnel GTP-U |
| UE | User Equipment | equipamento do usuário |
| UPF | User Plane Function | encaminha o tráfego do usuário |
| URLLC | Ultra-Reliable Low-Latency Communications | perfil de baixa latência e alta confiabilidade |
| VLAN | Virtual LAN | segmentação lógica de camada 2 |
| VM | Virtual Machine | máquina virtual com SO convidado completo |
| VNF | Virtual Network Function | função de rede executada em VM |
| vRAN | virtualized RAN | funções de RAN como software sobre infra comum |
| xApp | xApp | aplicação que roda no Near-RT RIC |
| XR | Extended Reality | realidade estendida |
