## Ganho e atenuação
- Ganho e atenuação são a mesma conta, o que muda é o sinal do resultado. Comparo a potência em dois pontos do sistema
- $G = \frac{P_2}{P_1} > 1$ -> em dB, $G_{dB} = 10\log_{10}\frac{P_2}{P_1} > 0$
- $A = \frac{P_2}{P_1} < 1$ -> em dB, $A_{dB} = 10\log_{10}\frac{P_2}{P_1} < 0$
- Quando trabalho com tensão em vez de potência o multiplicador vira 20, porque $P = V^2/R$ e o quadrado desce do log:
$$G_{dB} = 10\log_{10}\frac{P_2}{P_1} = 10\log_{10}\frac{V_2^2}{V_1^2} = 20\log_{10}\frac{V_2}{V_1}$$
- 10 log para potência, 20 log para tensão e campo. Trocar um pelo outro é o erro mais fácil de cometer aqui
### Nível de potência
- Potência é a taxa de trabalho por segundo, ou o consumo de energia por segundo: $P[W] = \frac{E[J]}{T[s]}$
- Em escala logarítmica a potência é sempre relativa a uma referência. Muda a referência, muda o nome da unidade
- dBm -> referência 1 mW: $P_{dBm} = 10\log_{10}\frac{P[W]}{1mW}$
- dBW -> referência 1 W: $P_{dBW} = 10\log_{10}\frac{P[W]}{1W}$
- Nos dois casos o número diz quantos dB acima (+) ou abaixo (-) a potência está da referência
- Como 1 W = 1000 mW e $10\log 1000 = 30$, a distância entre as duas escalas é fixa em 30 dB

| Conversão Desejada          | Tipo de Grandeza | Fórmula Matemática                | Regra Prática Rápida                              |
| --------------------------- | ---------------- | --------------------------------- | ------------------------------------------------- |
| **dBW para Watts (W)**      | Potência         | $W = 10^{\frac{dBW}{10}}$         | Divida o dBW por 10 e eleve à base 10.            |
| **dBm para Miliwatts (mW)** | Potência         | $mW = 10^{\frac{dBm}{10}}$        | Divida o dBm por 10 e eleve à base 10.            |
| **Watts (W) para dBW**      | Potência         | $dBW = 10 \cdot \log_{10}(W)$     | Calcule o $\log_{10}$ do valor e multiplique por 10. |
| **Miliwatts (mW) para dBm** | Potência         | $dBm = 10 \cdot \log_{10}(mW)$    | Calcule o $\log_{10}$ do valor e multiplique por 10. |
| **dBm para dBW**            | Unidade          | dBW = dBm - 30                    | Subtraia 30 do valor em dBm.                      |
| **dBW para dBm**            | Unidade          | dBm = dBW + 30                    | Some 30 ao valor em dBW.                          |

- Campo elétrico segue a mesma ideia, com referência de 1 $\mu$V/m -> unidade dB$\mu$. Por ser campo, usa 20 log
### Propagação na atmosfera
- Quase toda comunicação acontece dentro da atmosfera, e a atmosfera não é um meio homogêneo. Temperatura, pressão e altitude variam, o índice de refração varia junto, e é daí que saem os fenômenos de propagação diferentes
- Ondas ionosféricas: a onda sobe, incide na ionosfera (60 km a 1000 km de altitude) e volta para a Terra. Dois mecanismos causam isso:
	- Reflexão: frequência baixa reflete direto ao incidir na camada
	- Refração: em frequência mais alta, mas ainda abaixo de 50 MHz, a onda sofre refrações múltiplas dentro da ionosfera e acaba curvando de volta
	- Faixa em que o fenômeno ocorre: 2 MHz a 50 MHz
	- Enlaces típicos: 4000 km
- Ondas troposféricas: a troposfera (10 km a 12 km) é uma região turbulenta, com variação forte das propriedades do meio. A onda espalha ali e parte da energia volta para o solo
	- Faixa de operação: 1 GHz a 2 GHz
	- Cobra caro por isso: antena especial, amplificador de alta potência e receptor de grande sensibilidade
- Propagação próxima ao solo: o sinal chega na antena receptora por visada direta ou por reflexão. A variação de pressão e temperatura ao longo do enlace muda o índice de refração e encurva a onda terrestre
### Propagação no espaço livre
- Espaço livre: região onde o sinal propaga desobstruído, longe do solo, sem a onda interagir com nenhum outro elemento
- Antena isotrópica: elemento irradiante hipotético que emite com a mesma densidade de potência em todas as direções. É a referência de tudo o que vem depois
- A energia se espalha numa casca esférica de área $4\pi r^2$, então a densidade de potência cai com o quadrado da distância:
$$S_o = \frac{P}{4\pi r^2}$$
- Relação da densidade com os campos irradiados:
$$S_o = \frac{1}{2}\frac{E_{máx}^2}{\eta} = \frac{E_{ef}^2}{\eta} = \frac{1}{2}\eta H_{máx}^2 = \eta H_{ef}^2$$
- Campos a uma distância $r$ da antena isotrópica:
$$E_{ef} = \frac{\sqrt{30P}}{r} \qquad H_{ef} = \frac{E_{ef}}{120\pi}$$
- O campo cai com $1/r$ e a densidade de potência com $1/r^2$. Faz sentido, densidade de potência é campo ao quadrado
- A antena de recepção captura só uma parcela pequena dessa frente de onda esférica
### Diretividade, ganho e EIRP
- Antena real não irradia igual para todo lado. Ela concentra energia numa direção (lobo principal) e desperdiça um pouco nos lobos secundários
- Diretividade: quanto a antena concentra em relação à isotrópica
$$D = \frac{S_{máx}}{S_o}$$
- Ganho é a diretividade descontada a eficiência de irradiação $k$: $G_o = k \cdot D$
- Em dB: $G_o(dB) = 10\log_{10}(G_o)$, costuma vir expresso em dBi, o i de isotrópica
- EIRP (potência equivalente de irradiação isotrópica): a potência que uma isotrópica precisaria irradiar para produzir a mesma densidade na direção de apontamento
$$EIRP = G_o P \qquad S'_{máx} = \frac{EIRP}{4\pi r^2}$$
- Ganho de antena não cria energia, só redistribui. Tudo se passa como se fosse uma isotrópica irradiando o EIRP
- O dipolo de meia onda também serve de referência. Ele tem 2,14 dB sobre a isotrópica, então:
$$G_{dBd} = G_{dBi} - 2,14$$
- Área efetiva: razão entre a máxima potência gerada nos terminais da antena e a densidade de potência que incide nela
$$A_e = \frac{P_{r\,máx}}{S} = \frac{\lambda^2 D}{4\pi}$$
- Repara no $\lambda^2$: quanto mais alta a frequência, menor o comprimento de onda e menor a área efetiva. A mesma antena colhe menos potência em frequência alta
### Friis
- O espaço livre não absorve energia do sinal. Mesmo assim existe atenuação, porque a antena receptora só pega um pedaço da frente de onda que foi espalhada pela esfera
- Potência nos terminais da antena receptora:
$$P_R = \frac{G_T P_T}{4\pi r^2}A_{er} = \frac{G_T G_R P_T \lambda^2}{(4\pi r)^2} = G_T G_R P_T\left(\frac{c}{4\pi r f}\right)^2$$
- Atenuação no espaço livre é a razão entre a potência transmitida e a recebida:
$$A = \frac{P_T}{P_R} = \frac{1}{G_T G_R}\left(\frac{4\pi r f}{c}\right)^2$$
- Fórmulas prontas, com $G$ em dBi e distância em km:
$$A(dB) = 32,44 + 20\log f[MHz] + 20\log r[km] - G_T - G_R$$
$$A(dB) = 92,44 + 20\log f[GHz] + 20\log r[km] - G_T - G_R$$
- A constante só muda de 32,44 para 92,44 porque troquei MHz por GHz, fator 1000 -> 60 dB
- Consequência prática que vale guardar: dobrar a distância custa 6 dB, dobrar a frequência custa outros 6 dB
### Alcance máximo
- Se eu fixo a potência mínima que o receptor precisa nos terminais da antena para detectar com qualidade aceitável, consigo estimar até onde o enlace vai considerando só espaço livre:
$$r_{omáx} = \frac{\lambda}{4\pi}\sqrt{\frac{P_T G_T G_R}{P_{R\,mín}}}$$
- Se o meio tem condutividade não nula ele absorve energia, e entra um fator de atenuação exponencial:
$$P_R = \frac{G_T G_R P_T \lambda^2 e^{-2\alpha r}}{(4\pi r)^2}$$
- Aí o alcance máximo vira função transcendental, com solução numérica ou gráfica:
$$r_{máx} = r_{omáx}\exp(-\alpha r_{máx})$$
### Modelagem do canal de rádio
- Canal de rádio é imprevisível se comparado com meio confinado
- O caminho de propagação e os parâmetros dele mudam ao longo do tempo: perfil de percurso, obstáculos, mudanças ambientais
- Por isso o modelo é estatístico e empírico, montado a partir de medição em campo
### Difração
- Difração: fenômeno que permite a onda eletromagnética contornar obstáculo que bloqueia parcialmente o sinal
- Quando a frente de onda incide no obstáculo ela se decompõe em várias frentes com direções distintas, e cada uma propaga segundo um novo vetor de propagação
- É isso que explica receber sinal mesmo sem visada direta
- O percentual do sinal que contorna depende das características eletromagnéticas do obstáculo e do formato dele
- Modelo de Obstáculo Tipo Gume de Faca: simplificação em que o obstáculo
	- tem espessura desprezível
	- tem comprimento infinito
	- é feito de material que absorve completamente a onda incidente
- Geometria: o obstáculo está a $d_1$ da fonte e $d_2$ do destino, e $H$ é a distância entre a linha de visada e o topo do obstáculo. A parcela da frente de onda a partir de $S_o$ é a que atinge o destino
### Elipsoide de Fresnel
- Elipsoide de Fresnel: região do espaço, em função da distância $r$ da fonte, que delimita uma variação máxima de fase de $\pi$ radianos
- Os pontos de foco dos elipsoides são as antenas de transmissão e recepção
- Primeira zona: calota esférica, é a mais importante, contém a parte mais significativa da energia que vai da fonte para o destino
- Zonas II, III e seguintes: anéis esféricos, contribuem bem menos
- Raio do elipsoide da zona $n$, num ponto a $d_1$ do transmissor e $d_2$ do receptor:
$$\rho_n = \sqrt{\frac{n\lambda d_1 d_2}{d_1 + d_2}}$$
- O enlace só é considerado desobstruído quando nenhum obstáculo interfere no primeiro elipsoide. Linha de visada livre não basta
### Atenuação por obstáculo
- O modelo Gume de Faca considera Terra plana, ou seja, enlace curto o bastante para o raio da Terra ser desprezível
- O que importa é a altura do obstáculo em relação à linha de visada naquele ponto:
$$H = h_o - h_v$$
	- $H > 0$ -> o obstáculo ultrapassa a linha de visada
	- $H < 0$ -> o obstáculo fica abaixo dela
- O campo difratado sai de integrar a contribuição da parte desobstruída da frente de onda. Como a superfície está longe da fonte, dá para tratar como onda plana, e a diferença de percurso vira quadrática. É esse termo quadrático no expoente que faz aparecer as integrais de Fresnel
- Parâmetro de difração de Fresnel-Kirchhoff:
$$V_o = H\sqrt{\frac{2(d_1+d_2)}{\lambda d_1 d_2}} = \frac{H\sqrt{2}}{\rho_1}$$
	- positivo se o obstáculo passar a linha de visada, negativo se não passar
- Integrais de Fresnel (no Matlab, `fresnelc(x)` e `fresnels(x)`):
$$C(x) = \int_0^x \cos\left(\frac{\pi u^2}{2}\right)du \qquad S(x) = \int_0^x \sin\left(\frac{\pi u^2}{2}\right)du$$
- Fator de atenuação de campo do modelo Gume de Faca:
$$A_o = \left|\frac{E}{E_o}\right| = \frac{1}{\sqrt{2}}\sqrt{\left[\frac{1}{2}-C(V_o)\right]^2 + \left[\frac{1}{2}-S(V_o)\right]^2}$$
- Perda de potência em dB causada pelo obstáculo:
$$L = -20\log\left|\frac{E}{E_o}\right| = -20\log\left(\frac{1}{\sqrt{2}}\sqrt{\left[\frac{1}{2}-C(V_o)\right]^2 + \left[\frac{1}{2}-S(V_o)\right]^2}\right)$$
- Três casos que resumem o comportamento:
	- obstáculo tangenciando a linha de visada, $V_o = 0$ -> 6 dB de perda. Mesmo com a visada aparentemente livre já perco metade do campo
	- topo do obstáculo uma vez $\rho_1$ acima da visada -> 16,32 dB
	- topo do obstáculo 60% de $\rho_1$ abaixo da visada -> perda praticamente nula. É a regra dos 60%: liberando 60% do primeiro elipsoide o enlace já se comporta como espaço livre
### Aproximações numéricas
- Servem para não precisar calcular as integrais de Fresnel na mão
$$A_{obs}(dB) = -20\log(0,5 - 0,62V_o), \qquad -0,80 < V_o < 0$$
$$A_{obs}(dB) = -20\log\left(0,5\,e^{-0,95V_o}\right), \qquad 0 < V_o < 1$$
$$A_{obs}(dB) = -20\log\left(0,4 - \sqrt{0,1184 - (0,38 - 0,1V_o)^2}\right), \qquad 1 < V_o < 2,4$$
$$A_{obs}(dB) = -20\log\left(\frac{0,225}{V_o}\right), \qquad V_o > 2,4$$
$$A_{obs}(dB) = 20\log\left|\frac{E_o}{E}\right| \cong 16 + 20\log\left(\frac{H}{\rho_1}\right), \qquad V_o > 2,2$$
