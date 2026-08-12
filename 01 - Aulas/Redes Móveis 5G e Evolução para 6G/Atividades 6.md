## Exercício 1 — Cenário e arquitetura de RAN
| Cenário                          | Arquitetura      |
| -------------------------------- | ---------------- |
| Área rural, transporte limitado  | RAN tradicional  |
| Área urbana densa                | C-RAN            |
| Fábrica com baixa latência       | vRAN             |
| Laboratório de interoperabilidade | Open RAN        |
### Área rural com poucos usuários e transporte limitado
RAN tradicional, com o site inteiro na torre
- Benefícios: não precisa de fronthaul então funciona com backhaul modesto, até rádio-enlace. Site independente se o link cair a célula não some junto
- Riscos: Manutenção presencial e cara, coordenação de interferência limitada e upgrade caixa a caixa
- Pré-requisitos: energia e um backhaul IP qualquer
 O transporte que a C-RAN exige custa mais que o ganho de eficiência num lugar com pouco usuário
### Área urbana densa com muitas células e alta demanda
C-RAN, com pool de BBU centralizado e só o rádio na célula
- Benefícios: coordenação entre células vizinhas, ganho de pooling (a carga não é simultânea em todos os setores), site remoto pequeno e barato
- Riscos: o hub vira ponto único de falha e o fronthaul é caro
- Pré-requisitos: fibra dedicada ou WDM até cada célula, hub com energia e climatização e latência de fronthaul na casa de centenas de microssegundos
O eCPRI alivia a taxa em relação ao CPRI mas não a exigência de latência
### Fábrica com requisitos de baixa latência e controle local
vRAN, com CU e DU em servidor de propósito geral dentro da planta
- Benefícios: DU e UPF no mesmo edge, o pacote não sai do prédio. Escala por software e a fábrica opera a própria rede
- Riscos: desempenho depende de aceleração e de tuning de tempo real no host, e um kernel mal configurado derruba o orçamento de latência inteiro
- Pré-requisitos: sala de servidor no local, sincronismo preciso (PTP ou GNSS), placa aceleradora
### Laboratório voltado à interoperabilidade entre fornecedores
Open RAN
- Benefícios: interface aberta permite O-RU de um fornecedor com O-DU de outro que é justamente o que se quer testar. Acesso ao RIC pra experimentar xApp
- Riscos: integração multi-fornecedor é trabalhosa e quando quebra cada fornecedor aponta pro outro
- Pré-requisitos: fronthaul aberto 7-2x, sincronismo, teste de conformidade e gente pra integrar
## Exercício 2 — Perguntas
- Qual diferença entre vRAN e Open RAN?
	vRAN é sobre implementação: a função da RAN vira software rodando em servidor comum, em vez de hardware dedicado. Open RAN é sobre interface: os pontos entre RU, DU e CU são abertos então dá pra misturar fornecedor. Uma vRAN pode ser toda de um fabricante só e continuar sendo vRAN
- Por que cloud-native não significa apenas "colocar na nuvem"?
	Cloud-native é o jeito de construir: microsserviço em container, stateless, escala horizontal, orquestração, atualização sem derrubar o serviço, estado guardado fora da aplicação. Sem isso não aparece a elasticidade nem a recuperação automática que a nuvem deveria dar
- Qual o papel do Near-RT RIC?
	Controlar a RAN em laço de 10 ms a 1 s, pela interface E2, rodando xApps de mobilidade, escalonamento e controle de interferência
- Que interface conecta O-RU e O-DU?
	Open Fronthaul
- Quais são os principais riscos de uma RAN desagregada?
	- Integração multi-fornecedor e a dificuldade de achar o culpado quando falha
	- Fronthaul: latência, taxa e sincronismo apertados
	- Superfície de ataque maior com mais interface exposta
	- Maturidade desigual das implementações
	- O custo de teste e integração
