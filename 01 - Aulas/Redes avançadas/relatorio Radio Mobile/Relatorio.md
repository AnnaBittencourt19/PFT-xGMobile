# Planejamento de uma Rede TVWS com Radio Mobile
Carmo da Cachoeira - MG
## 1. Identificação do cenário
Rede ponto-multiponto em TVWS, com uma ERB na sede de Carmo da Cachoeira e uma estação remota na zona rural (onde eu moro) e outra dentro da cidade (A ERB fica em um ponto alto que não é dentro da cidade mas é próximo). Foi simulado no site Radio Mobile Online.
Escolhi o município por ser a minha cidade natal. Ele também serve bem ao caso: 11.547 habitantes espalhados em 506 km², relevo de morros e nenhuma emissora de TV atribuída ocupando o espectro local
## 2. Caracterização da região
- Cidade e estado: Carmo da Cachoeira, Minas Gerais
- Coordenadas da região estudada: em torno de −21,46 / −45,22
- População: 11.547 hab, sendo cerca de 9.100 urbanos e 2.650 rurais
- Relevo: colinas e morros, altitudes entre 861 e 1.093m pelo SRTM, desnível de uns 230 m em poucos quilômetros
- Solo: latossolo vermelho argiloso, típico de região cafeeira
- Vegetação: só 6,7% de remanescente de Mata Atlântica, o resto é café, milho e pasto
- Clima: subtropical de altitude, transição entre Cwa(clima temperado com inverno seco e verão quente) e Cwb(clima temperado com inverno seco e verão ameno)
A partir disso seria configurado no simulador: (no Radio Mobile Online não foi necessário inserir essa configuração)

	Clima                       Continental subtropical
	Refratividade da superfície 320 N-units
	Condutividade do solo       0,005 S/m
	Permissividade relativa     15

## 3. Configuração da rede

	Equipamento               transceptor do CRR nas duas pontas
	Potência de transmissão   1 Wp (30 dBm)
	Limiar de recepção        −84,99 dBm (12,6 µV)
	Ganho das antenas         11 dBi nas duas pontas
	Perdas de linha           0 dB
	EIRP                      12,589 W
	Ganho de sistema          136,99 dB
	Confiabilidade requerida  70%
	Frequência simulada       450 MHz

Os 12,6 µV vêm de converter os −85 dBm que a atividade pede, usando $V = \sqrt{PR}$ com 50 Ω.
Duas coisas eu não consegui configurar como o enunciado pede:
- A faixa TVWS no Brasil é 470 a 608 e 614 a 698 MHz mas o campo de frequência do Radio Mobile Online não aceitou valor dentro dela (tem que ter assinatura). Usei 450 MHz 
- A atividade pede antena Corner, mas o programa só oferece Omni, Ellipse, Cardio e Yagi. Usei Yagi que tem largura de feixe parecida (50° a 60° contra 40° a 60° do refletor de canto)
## 4. Localização das estações

![[Captura de Tela 2026-08-20 às 09.16.53.png]]
![[Captura de Tela 2026-08-20 às 09.17.10.png]]
![[Captura de Tela 2026-08-20 às 09.17.27.png]]

| Estação | Latitude | Longitude | Altitude | Antena | Distância à ERB |
| --- | --- | --- | --- | --- | --- |
| ERB | −21,453631 | −45,229287 | 994,7 m | 30 m | — |
| Remota 2 | −21,459914 | −45,221954 | 934,4 m | 10 m | 1,031 km |
| Remota 3 | −21,497254 | −45,203404 | 948,6 m | 10 m | 5,541 km |

Justificativa da ERB: é o local mais alto do conjunto (onde fica uma antena na cidade e é o Cristo da cidade), 60 m acima da Remota 2 e domina a área urbana. Como não existe torre de TV nem de rádio licenciada no município, o critério que usei foi o de ponto elevado (e no Rádio Mobile havia um triângulo invertido no local que indica uma unidade móvel)
Justificativa das remotas: a Remota 3 fica na zona rural a sudeste (onde eu moro e onde minhas galinhas residem), a 5,5 km e representa o caso de comunidade afastada. A Remota 2 está no limite do perímetro urbano ela não atende bem o critério de conectividade limitada mas mantive porque o contraste entre as duas isola o efeito do relevo
## 5. Cobertura de Downlink

![[Captura de Tela 2026-08-20 às 10.14.32.png]]
![[Captura de Tela 2026-08-20 às 10.11.43.png]]
![[Captura de Tela 2026-08-20 às 10.12.57.png]]

Verde é sinal acima de −75 dBm e o amarelo entre −85 e −75 dBm
O mapa não saiu redondo nem contínuo, ele saiu picotado. As manchas verdes seguem as vertentes viradas para a ERB, e os vazios ficam nos fundos de vale e atrás das cristas. Era de esperar em UHF (Frequência Ultra-Alta) com relevo desse tipo:

	tem visada          -> o sinal chega sobrando
	tem crista no meio  -> some em poucas centenas de metros

O alcance útil fica num raio de uns 10 a 15 km em volta da sede. As manchas isoladas mais longe são topo de morro que ainda enxerga a ERB. A cobertura pega a area urbana inteira. Configurei 50 km de raio máximo e não aparece nada nem perto disso, o que bate com o horizonte de rádio da geometria: $(d\approx 4,12\times (\sqrt{h_{t}}+\sqrt{h_{r}})$

$$d \approx 4{,}12(\sqrt{30}+\sqrt{10}) \approx 35{,}6\ \text{km}$$

A Remota 2 cai no meio do verde. A Remota 3 cai na borda, numa parte já entrecortada de vazios
## 6. Análise dos enlaces
### Downlink

![[Captura de Tela 2026-08-20 às 09.24.16.png]]
![[Captura de Tela 2026-08-20 às 09.27.17.png]]

Onde está vermelho está bloqueado pelo "pico" e o sinal acaba chegando mais fraco. −81,86 dBm é muito baixo para 5,5 km. Achei que uma antena de 50 m mudaria isso, mas caiu só para −79,65 dBm (continua ruim)

![[Captura de Tela 2026-08-20 às 12.40.50.png]]

### Uplink

![[Captura de Tela 2026-08-20 às 10.04.27.png]]
![[Captura de Tela 2026-08-20 às 10.05.33.png]]

### Resultados

|                       | ERB ↔ Remota 2 | ERB ↔ Remota 3        |
| --------------------- | -------------- | --------------------- |
| Distância             | 1,031 km       | 5,541 km              |
| Perda no espaço livre | 85,76 dB       | 100,34 dB             |
| Perda por obstrução   | 0,87 dB        | 26,95 dB              |
| Perda por vegetação   | 0 dB           | 0 dB                  |
| Perda estatística     | 6,63 dB        | 6,58 dB               |
| Perda total           | 93,25 dB       | 133,86 dB             |
| Sinal recebido        | −41,25 dBm     | −81,86 dBm            |
| Margem sobre −85 dBm  | 43,74 dB       | 3,13 dB               |
| Condição              | viável         | limítrofe (no limite) |

A última linha é a margem simulada menos os 1,85 dB da seção 3. Ela corrige só o espaço livre, e a difração também cresce com a frequência então na prática a Remota 3 fica pior que 1,28 dB.
O enlace da Remota 2 desce a encosta sem nada no caminho. Os 0,87 dB de obstrução mostram que a primeira zona de Fresnel está quase toda livre.
Já na Remota 3, o perfil passa por duas elevações e ainda sobe forte logo antes da remota, trecho que o simulador pinta de vermelho. Aí o raio de Fresnel no meio sobe para 30,4 m
Ao observar o tamanho da obstrução(o "pico"): 26,95 dB. A distância maior acrescentou 14,58 dB de espaço livre, quase a metade disso. Ou seja, o que atrapalha esse enlace é o morro, não a distância
### Downlink comparado com Uplink
Os quatro relatórios deram valores iguais dois a dois: 43,74 dB nos dois sentidos da Remota 2 e 3,13 dB nos dois sentidos da Remota 3.
- Os resultados foram iguais? Sim
- Que parâmetros provocaram diferença? Nenhum. O perfil e a difração não dependem de quem transmite e o sistema é simétrico porque o transceptor é o mesmo nas duas pontas com a mesma potência, o mesmo ganho e o mesmo limiar
- O enlace é bidirecionalmente viável? Sim os dois
- A cobertura de downlink garante o uplink? Aqui sim, por causa dessa simetria. Numa rede celular normal não garantiria porque a ERB transmite com mais potência que o terminal e o uplink limita a célula antes do downlink

## 7. Discussão dos resultados
A localização da ERB funcionou para o que eu queria atender. Os 994,7 m de cota mais os 30 m de torre deram visada limpa sobre a cidade, e o enlace curto fechou com mais de 40 dB. Adequada em parte, porque com a antena diretiva apontada em 142° o norte e o oeste do município ficam fora do lóbulo. Para cobrir o município inteiro desse mesmo ponto eu teria que setorizar ou trocar por omni e perder ganho.
As duas remotas estabeleceram enlace, mas a Remota 3 foi mais difícil com 3,13 dB contra 43,74 dB da outra. O pico teve influência a obstrução vai de 0,87 para 26,95 dB entre um enlace e outro.
Um ponto que me chamou atenção é a confiabilidade de 70%, que veio da configuração da aula. Nesse valor a perda estatística fica em 6,6 dB. Se eu subir para 95%, que é o usual em projeto, ela vai para uns 20 dB (escalando o termo de variabilidade pelo quantil da normal) e a Remota 3 passa a ter margem negativa. A Remota 2 continuaria confortável, com uns 30 dB. Então sob critério de projeto só um dos dois enlaces é viável de verdade.
O teste dos 50 m já responde parte da pergunta de como melhorar a Remota 3: altura sozinha não resolve. Subi a antena e ganhei 2,21 dB e a margem foi de 3,13 para 5,35 dB. Faz sentido, o obstáculo é alto e está perto da remota, então subir antena não tira o percurso de dentro da sombra
Aumentar a potência não dá, 1 Wp já é o teto da [Resolução 747](https://informacoes.anatel.gov.br/legislacao/resolucoes/2021/1593-resolucao-747). 
Sobre o TVWS ser adequado: acho que sim. O relatório da fase IV do projeto TVWS do NIC.br com o Inatel registrou cobertura de uns 14 km com 1 W de pico em campo, bem mais que os 5,5 km do meu enlace mais difícil. Então a tecnologia dá conta da distância, quem limita aqui é a topografia. O projeto de cada ponto remoto é que tem que tratar desobstrução como requisito
## 8. Conclusão
A rede funciona na configuração simulada, os quatro enlaces fecharam acima de −85 dBm. Com diferenças: 43,74 dB de margem na Remota 2 a 1 km e 3,13 dB na Remota 3 a 5,5 km.
E a causa não é a distância e sim a perda no espaço livre cresce 14,58 dB entre os dois enlaces enquanto a obstrução salta de 0,87 para 26,95 (devido ao relevo).
Downlink e uplink deram idênticos, por causa da reciprocidade do canal e de eu usar o mesmo transceptor nas duas pontas. A Remota 3 não se resolve subindo antena, ela precisa de reposicionamento encosta acima ou de uma repetidora no meio do caminho para ser considerada operacional.

## Referências
- Resolução Anatel nº 747/2021: https://informacoes.anatel.gov.br/legislacao/resolucoes/2021/1593-resolucao-747
- IBGE Cidades, Carmo da Cachoeira: https://www.ibge.gov.br/cidades-e-estados/mg/carmo-da-cachoeira.html
- Testes de campo TVWS em Quixadá: https://inatel.br/noticias/xgmobile-valida-tecnologia-tv-white-spaces-em-testes-de-campo-no-ceara