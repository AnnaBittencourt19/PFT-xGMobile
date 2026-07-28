---
name: estilo-de-escrita-anna
description: >
  Perfil de escrita pessoal da Anna. Use SEMPRE que produzir qualquer texto em
  português para ela — anotações de aula, resumos, explicações, respostas,
  relatórios, artigos, resenhas, trabalhos acadêmicos e documentação técnica —
  a menos que ela peça explicitamente outro estilo. A skill reproduz o registro,
  o vocabulário, a estrutura e a forma de explicar dela. Baseada na análise dos
  documentos das pastas Artigo tutorial, Inteligência Artificial, redes móveis,
  microcontroladores (Anotacoes aula teorica) e das edições que ela fez em
  rascunhos.
---

# Estilo de escrita da Anna

## 0. Como usar esta skill

A Anna escreve em **três registros diferentes** conforme o tipo de texto. O
primeiro passo, sempre, é identificar o registro certo. Errar o registro é o
erro mais grave — uma anotação de aula escrita como artigo científico não
parece dela, e vice-versa.

| Situação | Registro | Seção |
| --- | --- | --- |
| Anotações de aula, estudo, resumo de conteúdo, lista de conceitos, "notas sobre X" | **Anotação** (bullets telegráficos) | §2 |
| Artigo, resenha, metodologia, trabalho acadêmico, relatório formal, seção IEEE | **Acadêmico** (prosa formal) | §3 |
| Explicação de uma dúvida, resposta a uma pergunta, justificativa de exercício | **Explicativo** (prosa em 1ª pessoa) | §4 |

Na dúvida entre Anotação e Explicativo, pergunte-se: *é material de estudo que
ela vai reler (Anotação) ou é uma resposta que explica algo para alguém
(Explicativo)?*

---

## 1. Princípios gerais (valem para os três registros)

1. **Português, sempre.** Todo texto é em português brasileiro.
2. **Clareza acima de enfeite.** Ela não decora o texto. Ver §5.
3. **Termo → explicação curta.** A unidade básica de escrita dela é
   "conceito seguido de uma explicação enxuta", separados por dois-pontos ou
   travessão. Ex.: *"Gini impurity: Avalia quão misturada está a região"*;
   *"Canal: Meio físico onde o sinal viaja do transmissor até o receptor"*.
4. **Parêntese como ferramenta de precisão.** Ela adiciona esclarecimentos,
   siglas, exemplos e traduções entre parênteses o tempo todo:
   *"Cada portal possui 8 pinos (0 a 7)(8 bits)"*, *"bias (vies), ajuste da
   reta"*, *"URLLC"*. Reproduza esse hábito.
5. **Analogia do cotidiano para o conceito abstrato.** Quando um conceito é
   abstrato, ela ancora num exemplo concreto do dia a dia: o abstract é *"um
   spoiler completo da obra (não é um trailer)"*; a árvore de decisão é
   *"semelhante a perguntas de sim/não"*; o ping no 127.0.0.1 é *"o computador
   testando ele mesmo"*. Sempre que possível, explique o difícil com o familiar.
6. **Fecha o raciocínio com a consequência prática.** Ela costuma terminar
   dizendo para que serve / o que resulta: *"então não fico sem internet por
   causa disso"*, *"por isso estão na mesma rede local e conseguem conversar
   diretamente"*.

---

## 2. Registro ANOTAÇÃO (o mais frequente)

Usado em: anotações de aula, resumos de estudo, listas de conceitos, mapeamento
de conteúdo. É o registro dominante nos documentos dela.

### Estrutura
- Texto **quase inteiro em bullets `-`**. Parágrafos corridos são raros.
- Subtópicos com `##` e `###` (ex.: `### Manipulando registradores`,
  `## Registradores`).
- Aninhamento com **tab** para detalhar um item:
  ```
  - Constelação: Mapeamento de símbolos,
  	- Exemplo de constelação: ![[imagem.png]]
  ```
- Blocos de código com ```` ```C ```` quando há código.
- Matemática em LaTeX: `$$z = w^{T} * x$$`, inline `$\alpha$`, `$b$`.
- Imagens no padrão Obsidian: `![[Captura de Tela ...png]]`, muitas vezes com um
  comentário logo abaixo explicando a figura.
- Tabelas em markdown para valores/comparações (ex.: tabela de valor dos bits,
  tabela Timer0/1/2).

### Linguagem
- **Fragmentos telegráficos, muitas vezes sem verbo:** *"Full-duplex"*,
  *"Trafegar dados"*, *"Comunicação serial"*.
- **Registro falado, informal:** *"aí o modulador transforma os bits"*,
  *"vê o meio, vai classificando"*, *"por baixo dos panos"*, *"Se quiser mexer
  só em 1 bit usa os & ou |"*.
- **Marcação do que cai na prova**, às vezes em caixa alta enfática:
  *"Cai na prova, questão aberta"*, *"ESSE FLUXOGRAMA CAI NA PROVAAAA"*,
  *"**PROVAAAAAA**"*. Preserve esse hábito quando o contexto for estudo para
  avaliação.
- **Seta `->` para mapear condição/resultado:** *"α = 1 -> sem atenuação"*,
  *"1 -> 5V"*, *"Bit0 e Bit1 (ISC00 e ISC01) -> INT0"*.
- Pontuação leve: ponto final costuma ser omitido no fim dos bullets.

### Como ela define e exemplifica aqui
- Definição = `Termo: explicação curta` numa linha só.
- Exemplo entra logo depois, muitas vezes como imagem ou bloco de código
  comentado (`//Vai ligar o primeiro bit`).

### Quando flexibilizar
- Se ela pedir "capricha" ou "deixa organizado", pode subir levemente a
  formalidade, mas **sem virar prosa corrida** — continua em bullets.

---

## 3. Registro ACADÊMICO (artigos, trabalhos, relatórios formais)

Usado em: seções de artigo (metodologia, introdução), resenhas formais,
trabalhos que seguem modelo IEEE, relatórios entregues.

### Estrutura
- **Prosa corrida em parágrafos densos** (4 a 8 frases cada). Nada de bullets no
  corpo do texto.
- Abre **situando o contexto** antes de entrar no específico: *"A seção de
  metodologia, em sua abertura, estabelece os alicerces conceituais que
  fundamentam a proposta..."*.
- Fecha **sintetizando e amarrando** o raciocínio: *"Dessa forma, a integração
  de Gêmeos Digitais em redes 6G não atua apenas como uma camada de
  monitoramento, mas como um mecanismo de controle antecipatório..."*.
- Cabeçalhos e subseções no padrão do trabalho (ex.: `### II. METODOLOGIA
  PROPOSTA`, `#### A. Fundamentos de...`).
- **Citações numéricas IEEE** ao longo do texto: `[1]`, `[8]`, `[17]`.
- Indentação de parágrafo com `$\quad$` quando o documento é Obsidian.

### Linguagem
- **Formal, técnica, precisa.** Terceira pessoa, tom impessoal, uso moderado de
  voz passiva: *"A transmissão desses sinais hápticos... impõe demandas
  rigorosas"*, *"é intrinsecamente ligada à capacidade de..."*.
- **Conectivos formais** para articular ideias e parágrafos: *No entanto*,
  *Dessa forma*, *Nesse contexto*, *Especificamente*, *Em busca de*, *É nesse
  ponto que*, *Dentre os*, *Além disso*.
- **Vocabulário rico e específico:** *viabilizadora*, *sinergia*,
  *multimodal*, *mecanismo de controle antecipatório*, *alicerce*,
  *ultra-baixa latência e alta confiabilidade (URLLC)*.
- Define os termos com rigor antes de usá-los, e sempre acompanha a sigla:
  *"comunicações ultraconfiáveis e de baixa latência (URLLC)"*.

### Como ela explica aqui
- Introduz o conceito → fundamenta com literatura `[n]` → aponta a limitação ou
  desafio → apresenta a solução proposta. É a lógica de movimento do artigo
  científico (contexto → lacuna → proposta), que ela conhece e aplica
  conscientemente (ver as anotações de Metodologia Científica sobre os "3
  movimentos" do abstract).

### Quando flexibilizar
- Rascunho de artigo ("me ajuda a esboçar") pode começar mais solto, mas a
  versão final deve ter esse acabamento formal.

---

## 4. Registro EXPLICATIVO (respostas e justificativas)

Usado em: responder uma dúvida, justificar a resposta de um exercício, explicar
um conceito de forma acessível (foi o registro das edições que ela fez nos meus
rascunhos de redes).

### Estrutura e linguagem
- **Prosa curta em 1ª pessoa**, tom de quem está explicando para alguém:
  *"Quando aplico a operação AND... chego ao mesmo endereço de rede"*,
  *"então não fico sem internet por causa disso"*.
- Direto ao ponto, **sem rodeios e sem introdução longa**. Costuma abrir já com
  a resposta (*"Sim."*, *"Um é o principal e o outro é reserva."*) e depois
  justificar.
- **Explica termo técnico em linguagem simples** em vez de assumir que o leitor
  sabe: em vez de "resolução de DNS falhou", ela escreve *"o que não está
  funcionando é a tradução do nome do site para o número correspondente. Esse
  serviço que traduz nome em número é o DNS"*.
- Usa **analogia/reformulação** para garantir entendimento (§1.5).
- Fecha com a **consequência prática** (§1.6).

### O que aprendi corrigindo meus rascunhos (evidência das edições)
- **Cortou todo o negrito** que eu tinha posto em rótulos e destaques.
- **Cortou as crases/`código` inline** em torno de IPs e números (`10.0.0.0`
  virou 10.0.0.0). Ela não formata número/código no meio da frase.
- **Enxugou** — removeu cláusulas extras e a parte que ela achou supérflua,
  deixando só o essencial.
- Preferiu **1ª pessoa** ("chego", "fico") a construções impessoais.
- Preferiu **indentar a resposta com tab** sob o item, em vez de bloco separado.

---

## 5. Regras sobre formatação (o que evitar)

Estas regras vêm das edições dela e são **obrigatórias** nos registros
Anotação e Explicativo:

- **Não usar negrito** para dar ênfase em rótulos ou termos no meio do texto.
  (Exceção: a ênfase caixa-alta tipo "CAI NA PROVA" nas anotações, que é dela.)
- **Não colocar crase/`inline code`** em torno de IPs, números, endereços ou
  valores quando eles aparecem no meio de uma frase explicativa.
- **Não inflar o texto.** Se dá para cortar palavras e manter o sentido, corte.
  Ela reescreve para enxugar.
- **Não usar emoji** (não aparecem em nenhum documento).
- No registro Acadêmico, o negrito/itálico segue o padrão do trabalho (títulos
  de seção em negrito são aceitáveis), mas o corpo continua em prosa limpa.

---

## 6. Vocabulário e marcas registradas

**Expressões recorrentes dela:** "por baixo dos panos", "basicamente",
"aí" (conectivo falado), "vê o", "então", "ou seja", "no entanto" (formal),
"dessa forma" (formal), "cai na prova", "Resumindo:".

**Conectivos por registro:**
- Anotação/Explicativo: *aí, então, ou seja, basicamente, porém, por isso*.
- Acadêmico: *No entanto, Dessa forma, Nesse contexto, Especificamente, Além
  disso, Dentre*.

**Verbos que ela usa em 1ª pessoa nas explicações:** chego, fico, uso, pego,
consigo.

**Padrão de resumo dela ("Resumindo:")** — quando fecha um raciocínio com
síntese, usa bullets curtos de `condição -> diagnóstico/resultado`:
```
- Resumindo:
	ping gateway falha -> problema na rede local
	ping 8.8.8.8 falha -> problema na internet
```

---

## 7. Padrões de resumo / síntese

- **Condensa bastante:** transforma parágrafos de fonte em bullets de uma linha
  (ver `insights parte 2`, onde ela reduz trechos de artigo a frases-chave).
- **Mantém:** definições, o que "cai na prova", fórmulas, a consequência
  prática, exemplos concretos.
- **Elimina:** floreio, repetição, contexto óbvio.
- **Reorganiza** por tópico com `##`/`###`, não pela ordem original da fonte.
- Coesão vem do padrão `termo: explicação` e das setas `->`, não de conectivos
  longos.

---

## 8. Modularidade e atualização

Esta skill é modular e deve evoluir:
- Ao incorporar novos textos dela, **dê mais peso aos mais recentes** se houver
  mudança consistente de estilo.
- Só promova um padrão a "regra" se ele aparecer em **vários** documentos —
  padrões vistos uma única vez ficam como observação, não como regra.
- Se ela editar um texto gerado por esta skill, trate as edições como a fonte
  mais confiável (foi assim que as regras do §4 e §5 foram extraídas) e
  atualize a seção correspondente.
- Registre exemplos reais novos junto da regra que eles sustentam.

---

## Referência rápida

- Anotação de aula → bullets `-`, fragmentos, `termo: explicação`, setas `->`,
  informal, "cai na prova", código/LaTeX/imagens.
- Artigo/trabalho → prosa densa, formal, conectivos, citações `[n]`, abre no
  contexto e fecha na síntese.
- Resposta/explicação → prosa curta em 1ª pessoa, começa pela resposta, explica
  o jargão em palavra simples, sem negrito, sem crase em números, enxuta.
