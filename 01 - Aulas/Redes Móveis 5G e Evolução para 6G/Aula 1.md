## Evolução das gerações
### 0G e 1G - voz analógica
- 0G: sistemas móveis pré-celulares, geralmente analógicos
- 1G: primeira geração celular analógica, década de 1980
- Foco em voz, acesso predominantemente por FDMA
- Bandas próximas de 450, 800 e 900 MHz (depende do sistema)
- Baixa capacidade, pouca segurança, pouca eficiência espectral
### 2G - digitalização
- Transição de analógico para digital, voz digital
- Surge o SMS e os primeiros serviços de dados de baixa taxa
	- GSM inicial: ~9,6 kbit/s
	- GPRS: dezenas a pouco mais de 100 kbit/s
	- EDGE: centenas de kbit/s
- Mais segurança e melhor eficiência espectral
### 3G - dados em expansão
- Denominação internacional: IMT-2000
- Tecnologias UMTS/WCDMA e cdma2000
- WCDMA usa portadoras de ~5 MHz
- Acesso inicial à internet móvel, e-mail, navegação e multimídia
- Taxas:
	- 144 kbit/s em alta mobilidade
	- 384 kbit/s em mobilidade reduzida
	- até 2 Mbit/s indoor ou baixa mobilidade
- Consolidação dos smartphones
### 4G - banda larga móvel baseada em IP
- Tecnologia reconhecida: LTE-Advanced
- LTE usa OFDMA no downlink e SC-FDMA no uplink
- Arquitetura orientada a dados, rede toda em IP
- Largura de banda de uma portadora LTE: até 20 MHz
- Taxas:
	- 100 Mbit/s em alta mobilidade
	- 1 Gbit/s em baixa mobilidade ou estacionário
- Melhor suporte a vídeo, redes sociais e streaming, menos latência que o 3G
### 5G - flexibilidade, capacidade e novos serviços
- Suporte a eMBB, URLLC e mMTC
- Maior capacidade e menor latência
- Arquitetura mais flexível, com network slicing
- Aplicações em indústria, cidades inteligentes, agronegócio, saúde e IoT
### Fechando a linha do tempo
- 1G e 2G foram para voz e digitalização básica
- 3G e 4G dados móveis e comunicação IP
- 5G amplia o alvo: pessoas, máquinas, indústrias, sensores, etc (IoT)
	- Evolução: latência, confiabilidade, densidade e automação
## O que impulsionou o 5G
- Capacidade -> crescimento massivo de dispositivos conectados
- Latência -> controle remoto, automação e jogos em nuvem
- Densidade -> tráfego de vídeo e aplicações imersivas
- Flexibilidade -> redes mais programáveis, virtualizadas e orientadas a serviços
- Eficiência -> pressão por eficiência energética e melhor uso do espectro
## As três famílias de serviço
- eMBB: banda larga móvel aprimorada, alta taxa e boa experiência de usuário
- URLLC: comunicação confiável e de baixa latência, para controle crítico
- mMTC: muitos dispositivos, baixo consumo e tráfego esparso
- Na prática um serviço real mistura requisitos das três
## KPIs da rede
- Taxa de dados e capacidade agregada
- Latência fim a fim e latência da interface rádio
- Confiabilidade e disponibilidade
- Densidade de conexões por área
- Mobilidade, cobertura e eficiência energética

| KPI | Exemplo de impacto |
| --- | --- |
| Taxa | Vídeo, XR, upload industrial |
| Latência | Controle remoto e jogos |
| Confiabilidade | Processos críticos |
| Densidade | IoT e cidades inteligentes |
| Energia | Sensores e sustentabilidade |
## NSA x SA
- 5G NSA
	- Usa o Core 4G como âncora
	- Facilita a implantação inicial
	- Entrega ganho de taxa, mas limita os recursos nativos do 5G Core
	- Menos adequado para slicing pleno e serviços SA avançados
- 5G SA
	- Usa 5G Core
	- Arquitetura nativa 5G
	- Base para slicing, QoS avançado, edge e redes privativas
	- É o foco do curso
## Espectro: FR1 e FR2

| | FR1 | FR2 |
| --- | --- | --- |
| Faixa | 450 MHz a 7,125 GHz | 24,25 GHz a 52,60 GHz |
| Largura de banda | 5 a 100 MHz | 50 a 400 MHz |
| Ponto forte | Cobertura | Largura de banda |
| Desafio | Capacidade limitada | Alcance e bloqueios |

- FR1 é sub-7 GHz, melhor cobertura e penetração
- FR2 é onda milimétrica, mais banda disponível e propagação bem mais difícil
- Frequência baixa favorece cobertura, frequência alta favorece capacidade localizada
- DSS/refarming -> uso gradual do espectro, com custo de complexidade operacional
- O projeto da rede é sempre um equilíbrio entre cobertura, capacidade e custo
## New Radio (NR)
- Interface aérea do 5G, projetada para ser flexível
- Suporta diferentes larguras de banda e faixas de frequência
- Permite numerologias diferentes para ajustar tempo e frequência
- Usa evoluções do OFDM no downlink e no uplink na maioria dos cenários
- Integra beamforming, massive MIMO e agendamento avançado
### MIMO e beamforming
- MIMO usa múltiplas antenas para melhorar capacidade, cobertura e robustez
- Beamforming direciona a energia para regiões ou usuários específicos
- Em frequência alta o beamforming compensa as perdas de propagação
- Aumentam o desempenho, mas complicam planejamento e operação
### Estrutura de tempo e frequência

| Tema | Ideia central | Exemplo | Atenção |
| --- | --- | --- | --- |
| Numerologia | Espaçamento entre subportadoras | 15, 30, 60 kHz... | Afeta duração dos símbolos e latência |
| Slot | Unidade de agendamento temporal | Símbolos OFDM | Não confundir com "canal" |
| BWP | Parte ativa da largura de banda | UE usa uma fração da portadora | Ajuda na eficiência energética |
| PRB | Bloco físico de recursos | Tempo + frequência | Base do agendamento |

- Numerologia flexível -> espaçamentos diferentes entre subportadoras ( numero 0 = 15 kHz, 1 = 30kHz ...)
- Slots e mini-slots adaptam a transmissão a serviços diferentes
- TDD dinâmico ajusta uplink e downlink conforme a demanda
- A camada física foi desenhada pra atender cenários diferentes com a mesma família tecnológica
- PRB = 12 subportadoras
$$BWprb = 12 * ∆ƒ $$
$$Nprb = \frac{BWP}{12∆ƒ}$$
### FDD x TDD
- A forma de separar uplink e downlink impacta planejamento e interferência
- FDD usa frequências separadas para uplink e downlink
- TDD usa a mesma frequência em tempos diferentes
- TDD permite ajustar a proporção DL/UL, útil pra tráfego assimétrico
- Sincronização entre células é crítica em rede TDD
## Canais físicos
- Existem pra transportar dados, controle, sincronismo e medições
- SSB -> ajuda o UE a encontrar e sincronizar com a célula
- PDCCH -> controle
- PDSCH e PUSCH -> dados de downlink e uplink
- PUCCH -> controle no uplink
- PRACH -> acesso inicial à rede
### SSB
- Não é só um canal físico, é um bloco que contém:
	- PSS - Sinal Primário de Sincronização
	- SSS - Sinal Secundário de Sincronização
	- PBCH - Canal Físico de Broadcast
	- DM-RS do PBCH - Sinal de Referência para Demodulação
- Serve pra detectar a célula, sincronizar tempo e frequência, identificar a célula e obter as informações iniciais da rede
### PDCCH
- Ocupa determinados REs dentro de uma região chamada CORESET
- Informa ao UE:
	- onde está o PDSCH
	- quantos PRBs foram alocados
	- qual modulação e codificação usar
	- se ele deve transmitir no uplink
	- onde está o PUSCH
- Não carrega dado de usuário, carrega instrução de escalonamento
### PDSCH
- Ocupa PRBs e símbolos definidos pelo escalonador
- Transporta dados de aplicação, mensagens de sinalização e algumas informações de sistema
### PUSCH
- Funciona parecido com o PDSCH, mas no uplink
- O UE transmite usando determinados PRBs, determinados símbolos OFDM e determinada modulação/codificação
### PUCCH
- Ocupa recursos específicos no uplink pra transportar controle:
	- ACK/NACK
	- Channel State Information (CSI) (como tá o canal)
	- Scheduling Request (agendamento)
- Pode usar poucos PRBs e poucos símbolos, depende do formato
### PRACH
- Caso um pouco diferente dos outros
- Transporta os preâmbulos de acesso aleatório, usados quando o UE quer iniciar o acesso à rede
- Ocupa uma oportunidade específica no tempo, uma região específica na frequência e tem forma de onda e estrutura próprias
- Usa recurso de tempo e frequência, mas não é "dado colocado em símbolo OFDM comum" como no PDSCH ou PUSCH
## Procedimento de acesso ponta a ponta
- Busca de célula -> Sincronização -> Random access -> RRC setup -> Registro no Core -> Sessão PDU
### 1. Busca de célula
- O UE procura uma célula 5G disponível na faixa de frequência que ele suporta
- Busca principalmente o SSB (PSS, SSS, PBCH, DM-RS do PBCH)
- Com isso ele detecta que existe uma célula, identifica ela, localiza a transmissão no tempo e pega as informações básicas da rede
### 2. Sincronização
- O UE ajusta a referência de tempo, frequência, início dos símbolos e quadros, e a identificação física da célula
- Depois lê as informações iniciais:
	- MIB (Bloco Mestre de Informação) -> transmitido pelo PBCH
	- SIB1 (Bloco de Informação de Sistema Tipo 1) -> transmitido pelo PDSCH
- Essas informações dizem ao UE como acessar aquela célula
### 3. Random access
- O UE usa o PRACH pra transmitir um preâmbulo
- Objetivo:
	- informar que quer acessar a rede
	- obter sincronização no uplink
	- receber recursos pra transmitir
	- obter uma identificação temporária na célula
- Ainda não registra o usuário no Core, só cria as condições iniciais pro UE trocar sinalização com a gNB
### 4. RRC setup
- RRC = Radio Resource Control
- Permite que a gNB configure os recursos de rádio, que UE e gNB troquem sinalização e que as mensagens destinadas ao Core sejam transportadas pela RAN
### 5. Registro no Core
- A gNB só encaminha a sinalização NAS (Estrato de Não Acesso) entre o UE e o AMF (Função de Gerenciamento de Acesso e Mobilidade)
- Durante o registro podem acontecer:
	- identificação do assinante
	- envio de SUPI (Identificador Permanente da Assinatura) ou SUCI (Identificador Ocultado da Assinatura)
	- autenticação
	- verificação da assinatura no UDM (Gerenciamento Unificado de Dados)
	- estabelecimento da segurança NAS
	- seleção de slice
	- criação do contexto do UE no AMF
	- Registration Accept
- No fim o UE está reconhecido e autorizado pela rede
### 6. Sessão PDU
- Conexão lógica entre o UE e uma rede de dados, é ela que permite enviar e receber tráfego
- Nessa etapa são definidos:
	- endereço IP do UE
	- DNN (Nome da Rede de Dados)
	- slice utilizado
	- regras de QoS
	- UPF (Função do Plano de Usuário) responsável
	- túneis de dados entre gNB e UPF
## Recapitulação
- eMBB -> taxa alta, banda larga móvel
- URLLC -> latência baixa e confiabilidade, controle crítico
- mMTC -> muitos dispositivos, baixo consumo, tráfego esparso
- NSA -> rádio 5G com Core 4G de âncora
- SA -> rádio 5G com 5G Core, base pra slicing e edge
- FR1 -> sub-7 GHz, cobertura
- FR2 -> mmWave, capacidade
- Numerologia -> espaçamento de subportadora, mexe na duração do símbolo e na latência
- PRB -> unidade de recurso em tempo + frequência, base do agendamento
- BWP -> fração da portadora que o UE usa de fato
- SSB -> PSS + SSS + PBCH + DM-RS, é por onde o UE acha e sincroniza com a célula
- PDCCH -> controle, diz onde estão PDSCH e PUSCH
- PDSCH / PUSCH -> dados de DL e UL
- PUCCH -> controle de UL (ACK/NACK, CSI, SR)
- PRACH -> preâmbulo de acesso aleatório
- MIB vem no PBCH, SIB1 vem no PDSCH
- AMF -> acesso e mobilidade; UDM -> dados do assinante; UPF -> plano de usuário
- SUPI -> identificador permanente; SUCI -> o mesmo, só que ocultado
## Dicionário de siglas
### Gerações e tecnologias de acesso
- FDMA (Frequency Division Multiple Access): divide o acesso por faixa de frequência, cada usuário na sua
- TDMA (Time Division Multiple Access): divide o acesso por tempo, cada usuário no seu slot
- GSM (Global System for Mobile Communications): padrão de 2G digital
- SMS (Short Message Service): mensagem de texto curta
- GPRS (General Packet Radio Service): dados por pacote no 2G
- EDGE (Enhanced Data rates for GSM Evolution): evolução do GPRS, modulação melhor e mais taxa
- IMT-2000 (International Mobile Telecommunications-2000): nome oficial do 3G na UIT
- UMTS (Universal Mobile Telecommunications System): sistema 3G europeu
- WCDMA (Wideband Code Division Multiple Access): acesso do UMTS, separa usuários por código, portadora de ~5 MHz
- LTE (Long Term Evolution): rádio do 4G
- LTE-A (LTE-Advanced): versão do LTE que atende os requisitos de 4G da UIT
- NR (New Radio): interface aérea do 5G
### Formas de onda e antenas
- OFDM (Orthogonal Frequency Division Multiplexing): divide a banda em várias subportadoras ortogonais
- OFDMA (Orthogonal FDM Access): OFDM usado como acesso múltiplo, cada usuário recebe um conjunto de subportadoras
- SC-FDMA (Single Carrier FDMA): variação usada no uplink do LTE, gasta menos bateria do celular
- MIMO (Multiple Input Multiple Output): várias antenas no transmissor e no receptor
- mmWave (millimeter wave): onda milimétrica, faixa do FR2
- DSS (Dynamic Spectrum Sharing): 4G e 5G dividindo a mesma faixa dinamicamente
- FDD (Frequency Division Duplex): UL e DL em frequências separadas
- TDD (Time Division Duplex): UL e DL na mesma frequência, em tempos d
- iferentes
### Serviços e requisitos
- eMBB (Enhanced Mobile Broadband): banda larga móvel aprimorada, foco em taxa
- URLLC (Ultra-Reliable Low Latency Communications): comunicação ultraconfiável e de baixa latência
- mMTC (massive Machine Type Communications): comunicação massiva entre máquinas
- KPI (Key Performance Indicator): indicador usado pra medir o desempenho da rede
- QoS (Quality of Service): regras que definem tratamento diferente pra cada tipo de tráfego
- XR (Extended Reality): guarda-chuva de realidade virtual, aumentada e mista
- IoT (Internet of Things): internet das coisas, dispositivos conectados
### Arquitetura
- UE (User Equipment): o dispositivo do usuário, celular, módulo IoT, etc
- gNB (next generation NodeB): a estação rádio base do 5G
- RAN (Radio Access Network): a parte de rádio da rede
- NG-RAN (Next Generation RAN): a RAN do 5G
- NSA (Non-Standalone): rádio 5G ancorado no Core 4G
- SA (Standalone): 5G completo, rádio 5G com 5G Core
- 5GC (5G Core): núcleo nativo do 5G
- AMF (Access and Mobility Management Function): cuida de registro, acesso e mobilidade
- UDM (Unified Data Management): guarda os dados do assinante
- UPF (User Plane Function): encaminha o tráfego de dados do usuário
- NAS (Non-Access Stratum): sinalização entre UE e Core, a gNB só repassa
- RRC (Radio Resource Control): protocolo que configura os recursos de rádio entre UE e gNB
- PDU (Protocol Data Unit): unidade de dados; a Sessão PDU é a conexão lógica do UE com a rede de dados
- DNN (Data Network Name): nome da rede de dados de destino
- SUPI (Subscription Permanent Identifier): identificador permanente do assinante
- SUCI (Subscription Concealed Identifier): o SUPI cifrado, pra não trafegar aberto no ar
### Estrutura de recursos
- PRB (Physical Resource Block): bloco de recursos em tempo + frequência
- RE (Resource Element): a menor unidade, uma subportadora em um símbolo OFDM
- BWP (Bandwidth Part): parte da portadora que o UE usa de fato
- CORESET (Control Resource Set): região de tempo/frequência onde o PDCCH pode aparecer
### Canais e sinais
- SSB (Synchronization Signal Block): bloco de sincronização, PSS + SSS + PBCH + DM-RS
- PSS (Primary Synchronization Signal): sinal primário de sincronização
- SSS (Secondary Synchronization Signal): sinal secundário de sincronização
- PBCH (Physical Broadcast Channel): canal de broadcast, leva o MIB
- DM-RS (Demodulation Reference Signal): sinal de referência que permite demodular o canal
- PDCCH (Physical Downlink Control Channel): controle de downlink, leva o escalonamento
- PDSCH (Physical Downlink Shared Channel): dados de downlink
- PUSCH (Physical Uplink Shared Channel): dados de uplink
- PUCCH (Physical Uplink Control Channel): controle de uplink
- PRACH (Physical Random Access Channel): canal de acesso aleatório, leva o preâmbulo
- CSI (Channel State Information): informação de como está o canal, o UE reporta pro escalonador
- SR (Scheduling Request): pedido de recurso pra transmitir
- ACK/NACK: confirmação de que o bloco chegou certo ou errado
- MIB (Master Information Block): informação mínima pra acessar a célula, vem no PBCH
- SIB1 (System Information Block 1): informação de sistema mais completa, vem no PDSCH
- Em telecomunicações via satélite , um downlink é a ligação entre um satélite e uma ou mais estações terrestres ou receptores, e um uplink é a ligação entre uma estação terrestre e um satélite.
- U = Uplink
- D = Downlink
- ![[Captura de Tela 2026-07-28 às 10.24.21.png]]
### Atividade 01
• Por que o 5G não pode ser resumido a “mais velocidade”?
	O 5G não pode ser resumido a "mais velocidade". Diferente do 3G e do 4G, pensados em torno da conexão de pessoas, o 5G foi projetado com três casos de uso de primeira classe: eMBB, para banda larga móvel; mMTC, para conectar máquinas em alta densidade e URLLC para aplicações críticas com latência de ~1 ms. Esses perfis são conflitantes entre si e coexistem na mesma infraestrutura por meio do network slicing. Portanto, o 5G não só conecta pessoas com mais eficiência, como incorpora a comunicação entre máquinas como objetivo de projeto.
• Qual diferença prática entre NSA e SA?
- O 5G NSA usa o Core 4G como âncora, entrega ganho de taxa mas limita os recursos nativos do 5G Core e é menos adequado para slicing pleno e serviços SA avançados. Já, o 5G SA usa o 5G Core, tem a arquitetura nativa 5G e é a base para slicing, QoS avançado, edge computing e redes privativas.
• Por que espectro baixo e mmWave não resolvem o mesmo problema?
- Espectro baixo e mmWave não resolvem o mesmo problema. Existe uma oposição: ou eu tenho alcance, ou tenho velocidade. A faixa baixa atravessa parede e cobre bastante área, mas ali sobra pouco espectro livre, então a taxa é limitada. O mmWave é o contrário: para na primeira parede, mas tem centenas de MHz disponíveis, e é daí que vem a velocidade alta. Por isso o mmWave só serve em célula pequena, e a maioria das redes 5G roda mesmo na faixa média, em 3,5 GHz.
problema de cobertura de longo alcance e a dificuldade de penetração do sinal
