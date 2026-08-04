## Exercício 1 — Análise das funções
- AMF
	- Access and Mobility Management Function
	- Registro do UE, gerenciamento da conexão, mobilidade e terminação da sinalização NAS
	- Plano de controle
	- Interage com UE, gNB, AUSF, UDM, SMF, NSSF e NRF
	- N1 (NAS) e N2 (NGAP sobre SCTP)
	- Não encaminha dado de aplicação e não executa a autenticação, só coordena
- SMF
	- Session Management Function
	- Cria, modifica e libera sessão PDU, seleciona a UPF, define regra de encaminhamento e parâmetro de QoS, atribui endereço ao UE
	- Plano de controle
	- Interage com AMF, UPF, PCF, UDM e NRF
	- N4, com PFCP
	- Não encaminha pacote. Ela configura o caminho, quem anda nele é a UPF
- UPF
	- User Plane Function
	- Encaminha o tráfego entre RAN e Data Network, aplica QoS, filtragem e medição de uso, ancora a sessão
	- Plano de usuário
	- Interage com gNB, SMF, DN e outras UPFs
	- N3 e N9 com GTP-U, N6 com IP/Ethernet
	- Não cria sessão nem decide política, só executa a regra que o SMF instalou
- PCF
	- Policy Control Function
	- Transforma assinatura e requisito de serviço em política de QoS, de acesso e de cobrança
	- Plano de controle
	- Interage principalmente com SMF, e com AMF, AF e NEF
	- Serviço Npcf na SBA
	- Não aplica a política no tráfego. Quem aplica é a UPF, com o que o SMF configurou
- UDM
	- Unified Data Management
	- Gerencia dado de assinatura, identidade e serviço permitido, fornece o perfil do assinante
	- Plano de controle
	- Interage com AUSF, AMF e SMF
	- Serviço Nudm
	- Não autentica o UE
- AUSF
	- Authentication Server Function
	- Conduz a autenticação do assinante no procedimento 5G-AKA
	- Plano de controle
	- Interage com AMF e UDM
	- Serviço Nausf
	- Não guarda o perfil do assinante e não faz autorização de serviço
- NRF
	- Network Repository Function
	- Registro e descoberta de NFs, mantém o catálogo do que está disponível na rede
	- Plano de controle
	- Interage com todas as NFs
	- Serviço Nnrf, registro e descoberta
	- Não executa o serviço que foi descoberto, só informa onde ele está
- NSSF
	- Network Slice Selection Function
	- Determina os slices permitidos para o UE e indica as AMFs capazes de atender esses slices
	- Plano de controle
	- Interage com AMF e NRF
	- Serviço Nnssf, usa o S-NSSAI
	- Não cria nem orquestra a infraestrutura do slice, depende de slice já planejado
- NEF
	- Network Exposure Function
	- Expõe capacidade, informação e evento da rede a aplicações externas de forma controlada
	- Plano de controle
	- Interage com AF externa, PCF e demais NFs internas
	- APIs, serviço Nnef
	- Não deixa a aplicação externa falar direto com NF interna
- AF
	- Application Function
	- Informa os requisitos da aplicação e pede influência sobre QoS e roteamento
	- Plano de controle
	- Interage com PCF quando é confiável, e com NEF quando é externa
	- Serviço Naf
	- Não impõe política. Ela solicita, quem decide é a PCF
- NWDAF
	- Network Data Analytics Function
	- Coleta dado das NFs e do gerenciamento e produz estatística, tendência e previsão
	- Plano de controle
	- Interage com praticamente todas as NFs
	- Serviço Nnwdaf
	- Não toma decisão. A decisão é da NF que consome o analytics
## Exercício 2 — Tabela

| Função | Significado                             | Responsabilidade                                              | Plano    | Principal interação | Não faz                             |
| ------ | --------------------------------------- | ------------------------------------------------------------- | -------- | ------------------- | ----------------------------------- |
| AMF    | Access and Mobility Management Function | Registro, conexão, mobilidade e NAS                           | Controle | gNB (N2) e UE (N1)  | Não carrega dado de aplicação       |
| SMF    | Session Management Function             | Ciclo de vida da sessão PDU (Cria, modifica e libera sessões) | Controle | UPF (N4) e PCF      | Não encaminha pacote                |
| UPF    | User Plane Function                     | Encaminhamento e QoS no plano de usuário                      | Usuário  | gNB (N3) e DN (N6)  | Não cria sessão nem define política |
| PCF    | Policy Control Function                 | Política de QoS, acesso e cobrança                            | Controle | SMF                 | Não aplica política no tráfego      |
| UDM    | Unified Data Management                 | Dado de assinatura e identidade (guarda dados)                | Controle | AUSF e AMF          | Não autentica                       |
| AUSF   | Authentication Server Function          | Autenticação do assinante (verificação)                       | Controle | AMF e UDM           | Não guarda o perfil                 |
| NRF    | Network Repository Function             | Registro e descoberta de NFs                                  | Controle | Todas as NFs        | Não executa o serviço descoberto    |
| NSSF   | Network Slice Selection Function        | Seleção de slice e de AMF                                     | Controle | AMF                 | Não cria o slice                    |
| NEF    | Network Exposure Function               | Exposição da rede por API (Porta)                             | Controle | AF e PCF            | Não expõe NF interna diretamente    |
| AF     | Application Function                    | Requisito da aplicação                                        | Controle | PCF ou NEF          | Não impõe política                  |
| NWDAF  | Network Data Analytics Function         | Analytics da rede (Coleta e análise de dados da rede)         | Controle | Todas as NFs        | Não decide                          |

## Exercício 3 — Perguntas
- Qual função gerencia a sessão PDU?
	SMF
- Qual função encaminha os pacotes IP do usuário?
	UPF
- Qual é a diferença entre UDM e AUSF?
	A UDM é onde o dado do assinante mora: perfil, identidade, serviços permitidos. A AUSF é quem usa esse dado pra provar que o UE é mesmo quem diz ser, no 5G-AKA. Uma guarda, a outra verifica
- Por que o NRF é importante na SBA?
	Porque na SBA não existe mais uma topologia fixa de quem fala com quem. Podem existir várias instâncias de AMF, SMF, PCF ao mesmo tempo, subindo e descendo conforme carga, falha ou escalabilidade automática, e nenhuma delas tem endereço fixo pra sempre. Se cada NF precisasse ter a lista das outras configurada na mão, a rede perderia justamente a automação que a SBA prometeu. O NRF resolve isso sendo o catálogo: a NF que sobe registra o perfil dela, e a NF que precisa de um serviço consulta com critério (tipo, slice, região, condição de operação) e recebe as instâncias candidatas. Sem esse ponto de descoberta a arquitetura baseada em serviços não se sustenta
- O que N4 representa entre SMF e UPF?
	É a interface de controle do plano de usuário, com PFCP. Por ela o SMF instala e remove regra na UPF, define encaminhamento, configura tratamento de QoS e pede relatório de uso. É o que materializa a separação dos planos, a decisão fica de um lado e a execução do outro



- Só UPF no plano de usuário 
Extra (Claude que fez as imagens):
  ![[quadrinhos_v2_registro_5gc_seis_quadros.png]]
### Estudos UPF --- DN
![[so_upf_e_dn_cenario_fabrica.png]]
- Partes anteriores: Definem
- UPF: Executa
- Esquecemos de falar N3-GTP-U