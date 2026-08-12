## Exercício 1 — Projetar um slice
Vertical escolhida: indústria. Chão de fábrica com AGV, braço robótico, sensor e câmera de inspeção
### Requisitos
| Aplicação                | Taxa                    | Latência   | Confiabilidade | Disponibilidade |
| ------------------------ | ----------------------- | ---------- | -------------- | --------------- |
| Controle de AGV e robô   | centenas de kbps por nó | < 10 ms    | 99,999%        | 99,99%          |
| Sensor de vibração e temperatura | poucos kbps     | segundos   | 99,9%          | 99,9%           |
| Câmera de inspeção       | 20 a 50 Mbps de uplink  | < 50 ms    | 99,9%          | 99,9%           |

### UPF local ou Core centralizado
UPF local, dentro da planta. Se o dado de controle tiver que subir até uma UPF na nuvem a latência estoura só no transporte antes mesmo de qualquer processamento. Com breakout local o pacote vai do gNB pra UPF ali do lado e cai direto na rede da fábrica pela N6, e de quebra resolve o requisito de o dado de produção não sair do prédio.
O plano de controle (AMF, SMF, PCF, UDM, NRF) pode ficar centralizado porque ele não está no caminho do pacote,apenas monta o caminho
### Slices e isolamento
- Slice 1 -> SST 2 (URLLC), controle de AGV e robô. Isolamento forte
- Slice 2 -> SST 1 (eMBB), câmera de inspeção e uso geral
- Slice 3 -> SST 3 (MIoT), sensor
- No rádio: PRB reservado pro slice 1, os outros dois dividem o resto
- No core: UPF dedicada pro slice 1, UPF compartilhada pros outros
- O NSSF entrega o S-NSSAI certo no registro e o UE só enxerga o slice que está na assinatura dele
### Riscos e limitações
- Isolamento precisa de capacidade. PRB reservado pro URLLC fica reservado mesmo quando o AGV está parado e é banda que a câmera não vai usar
- Latência de rádio baixa não concerta transporte mal dimensionado. O gargalo costuma estar em switch e fibra da planta e não no 5G
- UPF local vira ponto único de falha se não tiver par redundante
- Handover dentro da planta pode interromper o slice URLLC e AGV em movimento vive fazendo handover
- A RAN suporta um número limitado de slices simultâneos então não dá pra criar slice pra cada aplicação
- Espectro: depende de faixa dedicada pra rede privativa ou de contrato com operadora
## Exercício 2 — Perguntas
- Qual diferença entre QoS Flow e sessão PDU?
	A sessão PDU é o caminho inteiro do UE até a Data Network. O QoS Flow é a granularidade de tratamento dentro dessa sessão, identificado pelo QFI e com um 5QI associado. Uma sessão carrega vários QoS Flows
- Por que slice não é a mesma coisa que DNN?
	DNN é para onde eu vou, a rede de dados de destino. Slice é por onde eu vou, a fatia com NF e recurso próprios. Dá pra ter o mesmo DNN em slices diferentes e um slice para vários DNNs
- Quando faz sentido usar UPF local?
	Quando a latência é apertada ou o dado não pode sair do local
- Isolamento forte sempre é a melhor solução?
	Não. Isolamento forte significa recurso dedicado, e recurso dedicado fica ocioso quando o slice não está usando. Numa fábrica onde o robô é crítico isso se paga mas aplicar o mesmo nível em tudo só encarece a rede e reduz a capacidade total. Isolamento depende da aplicação
- Quais KPIs uma rede privativa industrial deve priorizar?
	- Latência fim a fim e jitter
	- Confiabilidade e taxa de perda de pacote
	- Disponibilidade
	- Tempo de interrupção no handover
	- Taxa de uplink
	- Densidade de dispositivo por célula
