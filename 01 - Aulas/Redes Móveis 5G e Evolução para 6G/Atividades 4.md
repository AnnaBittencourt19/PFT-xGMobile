
Achar a última etapa que deu certo e olho só pra seguinte
## Exercício 1 
1. Não detecta nenhuma célula 5G
	- Última etapa: nenhuma, não há etapa anterior 
	- Área: RAN (Rede de acesso rádio)
	- Causas: gNB não transmitindo na banda/ARFCN que o UE varre, PLMN (identificação da rede da operadora) da gNB diferente do PLMN do SIM
	- Verificar: log do gNB, se a célula subiu e se o NG Setup completou
2. Seleciona a célula mas é rejeitado no registro
	- Última etapa: RRC e Registration Request na AMF
	- Área: controle de acesso
	- Causas: K/OPc diferente do cadastrado no UDM, aí o 5G-AKA falha, SUPI não cadastrado
	- Verificar: a 5GMM cause no Registration Reject. Ela já diz se é autenticação, assinatura ou slice
3. Registra mas não cria sessão PDU
	- Última etapa: registro
	- Área: gerenciamento da sessão
	- Causas: DNN não existe ou não está na assinatura, nenhuma UPF pro par DNN + S-NSSAI, ou PFCP na N4 caiu
	- Verificar: log da SMF e a causa no PDU Session Establishment Reject
4. Sessão criada, tem IP, mas não alcança a DN
	- Última etapa: sessão PDU com IP atribuído
	- Área: plano do usuário
	- Causas: falta NAT ou rota de volta pra sub-rede do UE na N6, TEID ou endereço de túnel errado na N3
	- Verificar: capturar dos dois lados da UPF
		sai request na N6 e não volta reply -> roteamento ou NAT
		não sai nada da UPF -> regra de encaminhamento ou N3
5. Ping funciona mas a aplicação está lenta
	- Última etapa: plano do usuário funcionando fim a fim
	- Área: QoS e capacidade
	- Causas: tudo no QoS Flow default (QFI 1, non-GBR), sem política do PCF, rádio ruim, SINR e MCS baixos, retransmissão HARQ
	- Verificar: iperf3, pra separar throughput de latência
	- Ping atenção. Pacote pequeno passa mesmo com o enlace ruim, o problema só aparece com carga
6. Perde conectividade no handover
	- Última etapa: sessão ativa na célula de origem
	- Área: mobilidade, RAN e AMF
	- Causas: vizinha não configurada na lista de vizinhança ou falta Xn, path switch não completou e a UPF continua mandando pro TEID antigo
	- Verificar: NGAP na hora do handover, se o Path Switch Request teve resposta
## Exercício 2 
- Qual a diferença entre estar registrado e ter uma sessão PDU?
	Registrado é a rede saber quem é o UE e ter autorizado ele, só plano de controle. A sessão PDU é o caminho de dados, com IP, DNN, slice e túnel. Dá pra estar registrado sem nenhuma sessão
- Que funções participam da autenticação?
	AMF( porta de entrada do controle, registro, NAS, mobilidade), AUSF(Executa a autenticação do assinante, UDM comunica com ela) e UDM (Dados de assinatura e identidades)
- Quem seleciona e controla a UPF?
	SMF, pela N4
- Por que o tráfego do usuário não passa pelo AMF?
	Os planos são separados. O AMF cuida de registro, mobilidade e NAS, e esse volume é pequeno perto do dado que a rede move. Se o dado passasse por ele viraria gargalo. Separando, a UPF fica perto do usuário e o AMF centralizado
- O que GTP-U ajuda a transportar?
	O pacote IP do usuário entre gNB e UPF na N3, e entre UPFs na N9. TEID identifica o túnel, QFI identifica o QoS Flow

Imagem ilustrativa feita pelo Claude: (Para entender melhor e exemplificar )
![[diagnostico_conectividade_5g.png]]
- Resumindo:
	não acha célula -> é rádio ver banda, PLMN e se o gNB subiu
	acha mas não registra -> é AMF e credencial. Ver a causa do reject
	registra mas não cria sessão -> é SMF. Ver DNN, slice e se tem UPF
	criou sessão mas não pinga -> é plano do usuário. Ver N3 e N6
	pinga mas está lento -> é QoS e rádio. Rodar iperf
	cai no handover -> é mobilidade. Ver vizinhança e path switch

- SINR: É uma métrica essencial em redes de comunicação sem fio (como 4G, 5G e IoT) que mede a qualidade real do sinal recebido, calculando a proporção entre a potência do sinal útil e a soma de todas as interferências e ruídos do ambiente
	- O que compõe o SINR
		- Sinal (S): A potência do sinal desejado que vem da antena ou torre.
		- Interferência (I): Sinais indesejados vindos de outras torres ou transmissores na mesma frequência.
		- Ruído (N): O ruído térmico natural ou interferência de fundo do sistema eletrônico

