# Lista PDS - respostas

## Exercício 1
a) Analógico é contínuo no tempo e na amplitude existe em todo instante e pode assumir infinitos valores. Digital é discreto nos dois só existe nos instantes amostrados e só assume um número finito de valores. Minha voz é analógica e o arquivo que o celular grava é digital
b) Amostragem mexe no eixo do tempo, quantização mexe no eixo da amplitude. Na amostragem eu pego o valor do sinal a cada Ts segundos e jogo fora o que está no meio. Na quantização eu pego o valor que sobrou e empurro ele para o nível mais próximo da lista de níveis permitidos
c) A quantização decide qual é o valor, a codificação decide como escrever esse valor em bits

## Exercício 2
a) Ts = 1/Fs = 1/20000 = 50 µs
b) N = Fs · t = 20000 · 2 = 40000 amostras

## Exercício 3
a) Por Nyquist, Fs > 2·Fmax = 8 kHz
b)
5 kHz -> não serve, abaixo de 2·Fmax, dá aliasing (as componentes altas se disfarçam de baixas e o sinal reconstruído sai errado)
8 kHz -> é exatamente o limite. Na teoria funciona, na prática ninguém usa porque qualquer imperfeição do filtro já faz os espectros se sobreporem
12 kHz -> serve, com folga para o filtro anti-aliasing

## Exercício 4
a) 2⁴ = 16 níveis
b) 2⁸ = 256 níveis
c) O de 8 bits, porque mais níveis na mesma faixa deixa cada degrau menor

## Exercício 5
a) É a diferença entre o valor real da amostra e o nível para o qual ela foi arredondada
b) Aumentando o número de bits, já que o passo de quantização é a faixa dividida por 2ⁿ. Dá para ajustar a faixa do conversor ao sinal também, senão fico gastando nível à toa numa região onde o sinal nem chega

## Exercício 6
a) Linearidade: vale a superposição e a homogeneidade. Entrada somada -> saída somada, entrada multiplicada por uma constante -> saída multiplicada pela mesma constante
b) Invariância no tempo: o sistema se comporta igual sempre. Se eu atraso a entrada a saída sai idêntica só que atrasada do mesmo tanto
c) Causalidade: a saída depende só do presente e do passado. Todo sistema em tempo real precisa atender isso ele não tem como saber o que ainda não chegou
d) Estabilidade: satisfaz o critério BIBO, entrada limitada gera saída limitada

## Exercício 7
(V) Um sistema causal depende apenas do presente e do passado
(F) Um sistema instável sempre produz saída limitada
É o contrário, instável é justamente quando existe entrada limitada que gera saída ilimitada
(V) Um sistema linear obedece ao princípio da superposição
(F) Todo sistema discreto é LTI
Discreto só diz que o sinal está amostrado. Para ser LTI precisa seguir linearidade e invariância no tempo ao mesmo tempo

## Exercício 8
Porque qualquer sinal discreto pode ser escrito como uma soma de impulsos deslocados, cada um multiplicado pelo valor da amostra naquele instante. Aí entram as duas propriedades pela invariância no tempo, impulso atrasado gera h[n] atrasada do mesmo tanto e pela linearidade, a resposta à soma é a soma das respostas. Juntando as duas, a saída vira a soma de cópias deslocadas e escaladas de h[n], que é exatamente a convolução y[n] = x[n] * h[n]. Por isso a h[n] é chamada de assinatura do sistema ela sozinha já carrega tudo

## Exercício 9
a) Transformada Discreta de Fourier. Pega N amostras no tempo e devolve N valores dizendo quanto de cada frequência tem ali dentro
b) A FFT não é outra transformada é um algoritmo rápido para calcular a mesma DFT. Ela cai de N² para N·log₂N operações dividindo o cálculo e reaproveitando o que se repete

## Exercício 10
Do domínio do tempo para o domínio da frequência

## Exercício 11
(X) Compressão de imagens
(X) OFDM
(X) Processamento de áudio
(X) Radar
( ) Redes sociais

## Exercício 12
Que o sinal é uma mistura de coisas que variam devagar com coisas que variam rápido. As baixas são o contorno geral (graves no áudio, áreas de cor uniforme na imagem), as altas são o que muda bruscamente de uma amostra para outra (chiado no áudio, borda na imagem)

## Exercício 13
Porque a FFT radix-2 divide o bloco pela metade até sobrar um par e isso só fecha certinho se N for potência de 2

## Exercício 14
(4) Elimina apenas uma faixa de frequências
(3) Preserva apenas uma faixa de frequências
(1) Preserva frequências baixas
(2) Preserva frequências altas

## Exercício 15
a) Passa-baixas
b) Passa-altas
c) Passa-faixa
d) Rejeita-faixa estreito (notch) em 60 Hz

## Exercício 16

| Característica | FIR | IIR |
| --- | --- | --- |
| Resposta ao impulso finita | Sim | Não |
| Sempre estável | Sim | Não |
| Menor custo computacional | Não | Sim |
| Pode ter fase linear | Sim | Não |

O que explica a tabela inteira é a realimentação. O FIR não tem, a saída depende só das entradas então a resposta ao impulso acaba e não tem como entrar em loop instável. O IIR realimenta a saída, aí a resposta nunca termina e a estabilidade passa a depender de onde ficam os polos. Em troca disso ele consegue a mesma seletividade com uma ordem bem menor

## Exercício 17
a) Faixa de passagem: as frequências que o filtro deixa passar praticamente sem mexer, ganho perto de 1
b) Faixa de rejeição: as que ele atenua, ganho perto de 0
c) Frequência de corte: a fronteira entre as duas, marcada onde a amplitude cai para 1/√2, que é -3 dB

## Exercício 18
Porque processador só lida com número finito e discreto e o sinal do mundo real é contínuo. Amostrar é o que transforma a curva numa sequência de valores que dá para somar, multiplicar e filtrar

## Exercício 19
Nyquist é o que define quantas amostras por segundo o sistema precisa transmitir para o outro lado conseguir reconstruir o sinal. Isso amarra direto a taxa de bits: taxa = Fs · bits por amostra. Amostrando abaixo de 2·Fmax dá aliasing e a informação perdida não volta mais, não tem processamento depois que conserte. Amostrando muito acima eu gasto banda à toa. É de onde saem os 8 kHz da telefonia (voz até 4 kHz) e os 44,1 kHz do CD (audição até 20 kHz), os dois com uma folga para o filtro anti-aliasing

## Exercício 20
No tempo eu vejo a amplitude variando instante a instante, o que responde quando as coisas acontecem: onde tem pico, quanto dura, qual o formato da onda. Na frequência eu vejo de quais senoides o sinal é feito e com que intensidade cada uma aparece, o que responde do que o sinal é composto
É a mesma informação vista de dois ângulos, e a DFT é a ponte entre eles. A escolha depende da pergunta: para saber em que momento houve uma batida cardíaca eu olho no tempo, para saber se tem interferência de 60 Hz no ECG eu olho na frequência

## Desafio
O microfone capta a voz analógica aí passa pelo filtro anti-aliasing e é amostrada. Como a voz inteligível vai até uns 8 kHz, 16 kHz já resolve. Depois vem a quantização em 16 bits, que deixa o ruído de quantização bem abaixo do nível da voz
Com o sinal digital, quebro ele em blocos de uns 20 ms e passo cada bloco pela FFT. Depois vejo o espectro daquele pedaço e consigo separar o que é voz do que é ruído porque eles ficam em regiões diferentes. Sabendo onde está cada coisa, aplico a filtragem passa-faixa na banda de voz e notch em 60 Hz se aparecer zumbido da rede elétrica
Todo esse encadeamento é modelado como sistema discreto, e as propriedades importam aqui. Causalidade porque numa chamada ao vivo eu só tenho o que já chegou, e estabilidade para o filtro não oscilar e estourar o áudio. No fim o sinal volta para o tempo pela FFT inversa e é transmitido
