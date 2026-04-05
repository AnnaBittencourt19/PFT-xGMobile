### A

- **ACK / NACK:** Sinais de controle do método ARQ. O ACK é a confirmação de que um pacote chegou sem erros, enquanto o NACK informa um erro e exige a retransmissão.
    
- **Antena:** Interface fundamental que converte o sinal elétrico guiado em uma onda eletromagnética no ar (transmissão) e vice-versa (recepção).
    
- **Antena Dipolo:** Estrutura mais simples de antena, formada por dois condutores (geralmente com tamanho de meia onda, $\lambda/2$) alimentados no centro.
    
- **Antena Patch (Microstrip):** Antena plana montada sobre um substrato dielétrico e um plano de terra. Opera em micro-ondas e é a base de celulares e redes 5G por suportar beamforming e MIMO massivo.
    
- **Antena Setorial:** Antena direcional projetada para cobrir apenas um setor específico (ex: 90º), reduzindo interferências e permitindo reuso de frequências em estações base.
    
- **Antena Verde:** Conceito moderno de projeto voltado à sustentabilidade, focado em integração modular, adaptação flexível e uso de materiais menos tóxicos (sem eletrólise nos dipolos).
    
- **Antena Yagi-Uda:** Antena de alto ganho direcional, composta por um elemento ativo (alimentado) acompanhado de elementos passivos (refletor atrás e diretores na frente).
    
- **Área Efetiva ($A_e$):** Parâmetro que mede o "tamanho eletromagnético" da antena, ou seja, o quanto de potência do espaço livre ela consegue capturar.
    
- **ARQ (Automatic Repeat Request):** Estratégia de controle de erro baseada na detecção de falhas e solicitação automática de retransmissão do pacote.
    
- **Atenuação ($\alpha$):** Perda natural e contínua de intensidade da onda ao longo da propagação. Em altas frequências (micro-ondas), ela é agravada severamente por condições climáticas (chuva) e obstáculos físicos.
    

### B - C

- **Banda-base:** Espectro onde o sinal da informação original se encontra natural e localizado em torno da frequência $0\text{ Hz}$.
    
- **Banda-passante:** Ocorre quando o sinal original é modulado e deslocado para operar em torno de uma frequência portadora muito mais alta.
    
- **Beamforming (Formatação de Feixe):** Técnica de processamento que ajusta a amplitude e a fase dos elementos numa matriz de antenas para direcionar o feixe de sinal ativamente para a posição exata do usuário.
    
- **Cabo Coaxial:** Meio guiado físico estruturado em camadas concêntricas: condutor interno de cobre, dielétrico (isolante) e um condutor externo (malha que atua como retorno e blindagem).
    
- **Campo Distante (Fraunhofer):** Região espacial longe da antena ($R > R_2$) onde os campos elétrico e magnético estão estabilizados e as medições de diagrama, ganho e polarização são oficialmente válidas.
    
- **Codificação de Canal:** Etapa de proteção da informação que insere redundância matemática controlada nos bits, garantindo resiliência contra o ruído do canal.
    
- **Codificação de Fonte:** Etapa de compressão focada em remover a redundância e previsibilidade da mensagem original, economizando banda e armazenamento (pode ter perdas, como JPEG, ou não, como Huffman).
    
- **CRC (Cyclic Redundancy Check):** Algoritmo de detecção de erros altamente preciso que realiza uma divisão polinomial em módulo 2 para gerar o bloco verificador FCS.
    

### D - E

- **DAB (Digital Audio Broadcasting):** Sistema europeu terrestre para rádio digital de alta qualidade que utiliza multiplexação para abrigar múltiplas estações no mesmo bloco de espectro.
    
- **Dielétrico:** Material isolante. No cabo coaxial, ele separa os condutores, e seu valor de permissividade ($\epsilon_r$) afeta a atenuação, impedância e velocidade da onda. Num cenário de propagação "sem perdas", é um meio que não dissipa energia da onda eletromagnética.
    
- **Difração:** Fenômeno que ocorre quando a onda atinge os limites de um obstáculo pontiagudo ou fenda, "dobrando-se" e vazando para as áreas de sombra sem linha de visada.
    
- **Diretividade ($D$):** Métrica teórica que compara a concentração de energia de uma antena específica em uma direção com uma antena isotrópica perfeita (que irradiaria igualmente para todos os lados).
    
- **DMR (Digital Mobile Radio):** Sistema digital corporativo de rádio bidirecional. Ele emprega a técnica TDMA para comportar simultaneamente dois slots de voz em um único canal estreito de 12,5 kHz.
    
- **DVB (Digital Video Broadcasting):** Família padrão de TV digital. O DVB-S atende transmissões por satélite, DVB-T para terrestres e DVB-C para cabo.
    
- **Eficiência de Irradiação ($\eta$):** Relação entre a potência de rádio frequência que é efetivamente irradiada pela antena e a potência que é perdida em forma de calor nos materiais.
    
- **Entropia ($H(S)$):** Conceito originado por Shannon, mede a quantidade média de incerteza da fonte e representa o tamanho limite teórico (em bits) alcançável por códigos sem perdas.
    
- **Equações de Maxwell:** Conjunto de quatro equações da física (Leis de Gauss, Faraday e Ampère) que explicam matematicamente o ciclo de indução entre os campos $\vec{E}$ e $\vec{H}$ que permite a propagação no vácuo.
    

### F - M

- **FEC (Forward Error Correction):** Família de códigos robustos (como Reed-Solomon, Turbo, LDPC) que insere alta redundância no transmissor, dando ao receptor a capacidade de corrigir erros diretamente sem solicitar reenvio.
    
- **FNBW e HPBW:** Médias angulares de abertura do feixe principal da antena. O HPBW mede o ângulo até a potência cair à metade (-3 dB), enquanto o FNBW mede a distância angular entre o primeiro nulo de cada lado.
    
- **Frequência de Corte ($f_c$):** O limite mínimo de frequência abaixo do qual um guia de onda passa a atuar como um bloqueio físico, travando completamente o sinal.
    
- **Ganho ($G$):** A medida de diretividade da antena ajustada pela sua eficiência real (descontando o calor). Sua unidade base é o dBi.
    
- **Guia de Onda:** Tubo puramente metálico e oco. Usado em frequências altas, ele direciona as ondas através de sucessivas reflexões nas paredes interiores.
    
- **HDR (HD Radio):** Padrão americano de rádio que transmite sinais híbridos na mesma frequência; a portadora principal transporta áudio FM analógico, e as laterais transportam o digital (IBOC).
    
- **Impedância ($Z$):** Oposição ao fluxo do sinal. É vital "casar" a impedância do cabo com a antena (geralmente fixando ambos em 50 $\Omega$) para que o sinal não seja devolvido pela antena.
    
- **Knife-edge (Modelo Gume de Faca):** Modelo matemático analítico de difração. Calcula os decibéis exatos de perda causados quando a linha de visada do sinal esbarra no cume de uma montanha ou prédio pontiagudo.
    
- **LLR (Log-Likelihood Ratio):** Métrica de software probabilística (usada no 5G) que representa a taxa de confiança na decodificação de um bit; $LLR > 0$ aponta com confiança para "0" e $LLR < 0$ para "1".
    
- **LOS (Linha de Visada):** Condição onde a comunicação ocorre com visibilidade física total e direta entre a antena de transmissão e a de recepção, operando em espaço livre pleno.
    
- **MIMO (Multiple-Input Multiple-Output):** Sistemas com várias antenas emissores e receptoras. As vertentes incluem: _Massive MIMO_ (dezenas/centenas de antenas), _MU-MIMO_ (atendimento a múltiplos usuários na mesma frequência através de feixes) e _XL-MIMO_ (painéis de superfície gigante previstos para o 6G).
    
- **Multipercurso (Multipath):** Efeito físico nocivo onde reflexões, difrações e refrações criam vários caminhos para o sinal, fazendo cópias chegarem fora de sincronia no receptor e causando variação abrupta no sinal (Fading).
    

### O - P

- **OFDM (Orthogonal Frequency Division Multiplexing):** Modulação de alta eficiência que transmite informações paralelas ao longo de múltiplas subportadoras ortogonais, apresentando forte defesa contra multipercurso.
    
- **Onda Eletromagnética:** Oscilação casada dos vetores elétrico e magnético. Pode viajar sem qualquer meio mecânico e é caracterizada por sua velocidade equivalente à da luz, transportando dados no espaço.
    
- **P25 (Project 25):** Sistema padronizado bidirecional para as forças de emergência. Possui alta interoperabilidade, utiliza arquitetura _trunking_ e possui criptografia padrão robusta.
    
- **PDH / SDH:** Padrões multiplexadores no tempo. O PDH é assíncrono, operando em blocos rígidos, exigindo "desmontar" toda a hierarquia para extrair um único canal; o SDH é a solução moderna que usa relógios em rede e ponteiros dinâmicos (payload).
    
- **Polarização:** Diz respeito ao plano de oscilação do vetor Elétrico. Pode ser linear, circular (muito forte contra chuva e rotação do receptor, usada em satélites) ou elíptica.
    

### R - Z

- **Rayleigh e Rice (Modelos):** Ferramentas de engenharia para lidar com multipercurso. Rayleigh cobre cenários puramente ocultos e caóticos da cidade grande (NLOS), e Rice aborda as rurais ou abertas onde uma LOS existe como componente dominante.
    
- **Reflexão e Refração:** Comportamentos em interfaces de materiais. A primeira força o raio a rebater sob ângulos idênticos e no mesmo plano, enquanto a segunda (Lei de Snell) permite que atravesse e distorça seu ângulo conforme a densidade dielétrica muda.
    
- **S11 (Coeficiente de Reflexão):** Parâmetro crítico do equipamento real de antena. Exibido linear ou em dB, dita quanto do sinal não "sai" para o ar e é refletido para os circuitos por falha de impedância (ideal é $\le -10\text{ dB}$).
    
- **SDR (Software Defined Radio):** Rádios revolucionários onde processos rígidos em peças (filtros, criptografia, modulação) ocorrem via CPU e algoritmos, permitindo que a mesma placa atue como rádio FM hoje e 5G amanhã com apenas um upload de software.
    
- **TEM / TE / TM:** Dinâmicas modais eletromagnéticas. Em TEM, ambos os campos ($\vec{E}$ e $\vec{H}$) estão no plano perpendicular em relação ao túnel do cabo coaxial. Guias de onda operam usando restrições geométricas onde ou o Elétrico (TE) ou o Magnético (TM) são mantidos estritamente perpendiculares à casca de propagação.
    
- **Vetor de Poynting ($\vec{S}$):** Mede e orienta geometricamente para onde a energia flui através de uma combinação (produto vetorial) das forças elétrica e magnética em um certo tempo.
    
- **VSAT (Very Small Aperture Terminal):** Uma rede completa de satélite remota e portátil em formato de "mini hub" para comunicação militar ou platafórmica em alto mar (Bandas Ku e C).
    
- **VSWR (Voltage Standing Wave Ratio):** Outra forma de reportar a saúde do casamento de rádio. VSWR no valor 1 indica perfeição; toda onda enviada foi lançada com sucesso no espaço livre.
    
- **Zona de Fresnel:** Uma geometria virtual que os sistemas rádio traçam ao redor da linha reta de comunicação (LOS). Obstáculos que violem os primeiros 60% dessa zona interna causam perturbações graves na fase da onda receptora e cancelamentos letais.