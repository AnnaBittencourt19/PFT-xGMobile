## Relacionando aplicações aos serviços 5G

| Aplicação                                                | Categoria | Requisito principal           | Requisito secundário                                          |
| -------------------------------------------------------- | --------- | ----------------------------- | ------------------------------------------------------------- |
| Realidade aumentada para manutenção industrial           | eMBB      | taxa alta no downlink         | latência baixa senão o overlay não acompanha o movimento      |
| Sensores de umidade distribuídos numa lavoura remota     | mMTC      | densidade de conexões         | cobertura ampla e consumo baixo                               |
| Câmera 4K ao vivo em evento esportivo                    | eMBB      | taxa alta no uplink           | capacidade em área densa, tem muita gente disputando a célula |
| Controle remoto em tempo real de robô móvel em fábrica   | URLLC     | latência muito baixa          | confiabilidade e disponibilidade                              |
| Acesso fixo sem fio para residências em comunidade rural | eMBB      | taxa sustentada por domicílio | cobertura e alcance                                           |
| Medição inteligente de energia numa cidade               | mMTC      | densidade de conexões         | eficiência energética do dispositivo                          |

- Realidade aumentada: vídeo e modelo 3D em cima do equipamento, é dado pesado -> eMBB
- Sensores de umidade: cada um manda quase nada(pouco dado), o que pesa é a quantidade de sensores -> mMTC
- Câmera 4K: uplink alto, o fluxo sai do estádio pra rede
- Robô da fábrica: comando pequeno mas não pode atrasar
- Acesso fixo sem fio: substitui a fibra dentro de casa
- Medidor de energia: mesma lógica dos sensores
## Por que o 5G não pode ser resumido a "mais velocidade"?
Porque taxa é só um dos KPIs (indicadores chave de desempenho). Se fosse só velocidade dava pra continuar espremendo o 4G. O que muda é o conjunto, latência fim a fim, confiabilidade, densidade de conexões por área, eficiência energética, e a rede virtualizada e programável, que é o que permite atender diversos perfis na mesma infraestrutura (usando slicing, QoS, edge)
## Qual diferença prática entre NSA e SA?
Onde está o núcleo. No NSA o rádio é 5G mas quem manda ainda é o 4G Core, que fica de âncora, então a operadora implanta rápido e ganha taxa, só que os recursos nativos do 5G ficam de fora. No SA o rádio fala direto com o 5G Core e aí abre slicing pleno, QoS avançado, edge e rede privativa
## Por que espectro baixo e mmWave não resolvem o mesmo problema?
- FR1 (sub-7 GHz) -> propaga bem, atravessa parede, cobre área grande, mas a banda é limitada (5 a 100 MHz)
- FR2 (mmWave, 24,25 a 52,60 GHz) -> 50 a 400 MHz de banda, muita capacidade, só que o alcance é curto e qualquer obstáculo bloqueia
- Eles não resolvem o mesmo problema porque um resolve cobertura e o outro resolve capacidade em ponto específico
- Na prática usam os dois em camada, não é escolher
## Como numerologia e TDD influenciam latência e capacidade?
A numerologia é o espaçamento entre subportadoras (15, 30, 60 kHz...). Espaçamento maior -> símbolo mais curto -> slot mais curto -> latência cai porque o UE não fica esperando tanto pra transmitir. O preço é o prefixo cíclico encurtar junto, aí o sistema aguenta menos atraso de propagação e passa a servir pra célula menor. Com mini-slot nem precisa esperar o slot inteiro, que é o caso do URLLC.
O TDD é outra história. Uplink e downlink dividem a mesma frequência em tempos diferentes, então dá pra ajustar a proporção conforme o tráfego, e como quase todo tráfego é assimétrico (bem mais download que upload) isso rende capacidade. O que eu não tinha pensado antes é que essa configuração DL/UL também entra na conta da latência, se o slot de uplink demora a chegar o pacote fica esperando. E célula vizinha desalinhada atrapalha, por isso sincronismo é crítico em TDD
## O que o UE precisa fazer antes de se registrar no Core?
- Busca de célula -> procura o SSB (PSS, SSS, PBCH, DM-RS) na faixa que ele suporta
- Sincronização -> ajusta tempo e frequência, identifica a célula e lê o MIB (no PBCH) e o SIB1 (no PDSCH)
- Random access -> preâmbulo no PRACH, recebe sincronismo de uplink e uma identificação temporária
- RRC setup -> a gNB configura os recursos de rádio e abre caminho pra sinalização NAS
