### TCP
- Processo receptor: 
	- Um endereço hospedeiro (IP)
	- Um identificador de porta (número de porta)(porta 8080 por exemplo (HTTP))
- TCP usa ACK(controle de erro) ,controle de fluxo)
- Stop-and-wait:
![[Captura de Tela 2026-07-22 às 10.32.51.png]]
- Go-back-N:
![[Captura de Tela 2026-07-22 às 10.33.20.png]]
- Selective-repeat:
![[Captura de Tela 2026-07-22 às 10.33.38.png]]
### UDP
- Cabeçalho mais simples
- Não orientado a conexão
- Não confiavel
- Checksum
- Chamadas
### TCP vs. UDP ![[Captura de Tela 2026-07-22 às 10.34.21.png]]
### Métricas
- Latência, Throughput, jitter, perda, goodput e confiabilidade 
- Latência: Tempo de ida ou volta, é a soma do tempo de processamento, de fila, de transmissão e de propagação
- Throughput: Quantidade total de dados transmitidos com sucesso por unidade de tempo 
- Goodput: Taxa de dados úteis entregues à aplicação
- Jitter: É a variação da latência entre pacotes consecutivos. Um jitter elevado prejudica aplicações em tempo real.
![[Captura de Tela 2026-07-22 às 10.47.13.png]]
