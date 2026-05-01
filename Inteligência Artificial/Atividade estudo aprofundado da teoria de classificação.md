introducao
## 1. Perceptron
Conceitos básicos e definição: 

  $\quad$O Perceptron é uma das arquiteturas de Rede Neural Artificial (RNA) mais simples já desenvolvidas, ele foi construído sobre um único neurônio artificial chamado Unidade Linear com Threshold (LTU). 
 $\quad$Trata-se de uma rede neural do tipo feedforward o que significa que as entradas (features) fluem em uma única direção (da entrada para a saída) cada entrada é multiplicada por peso seu peso correspondente e passa por uma função de ativação que gera a saída 
![[Pasted image 20260430100346.png]]
 $\quad$ A imagem acima exemplifica essa processo feedforward onde há mais de um input, e que eles passam por camadas (processamentos) até chegar em uma única saída

Matematicamente:
 $\quad$As entradas devem ser combinadas para produzir uma única saída e para isso acontecer tem um processo a LTU executa dois passos fundamentais. 
  $\quad$Sendo o primeiro passo a soma ponderada onde cada entrada é um valor numérico real associada a um peso que indica a relevância daquela entrada para o resultado, pesos maiores tornam certas entradas dominantes sobre a decisão final, a soma de todas as entradas multiplicadas pelo seu peso é dada pela formula:  $$z = w^{T} * x$$ $\quad$Após a soma ponderada os valores passam para a função de ativação onde o valor z passa por uma função degrau (step(z)) que gera uma saída binária de acordo com um limiar de ativação θ, esse limiar de ativação é o threshold, na imagem abaixo é demonstrado como uma saída é ativa (1) ou não, para ela ser ativada sua soma ponderada deve ser maior que a limiar de ativação e para ser desativada (0) sua soma ponderada deve ser menor ou igual ao threshold
![[Pasted image 20260430103245.png]]

Justificativa da fronteira de decisão ser linear: 
 $\quad$O Perceptron é um classificador linear, sua fronteira de divisão é basicamente a divisão do espaço das entradas com uma reta, onde um lado dessa linha é classificado como classe positiva e o outro como classe negativa, a imagem abaixo ilustra essa divisão: ![[Captura de Tela 2026-04-30 às 11.21.35.png]]
  $\quad$A limiar de divisão é linear pois no seu processamento temos apenas uma função linear, não há quadrados ou cubos durante seu processamento, apenas uma função que resulta em uma reta, desse modo não é possível que o gráfico realize curvas ou algo do gênero 

Visão geral sobre o uso do Perceptron 
  $\quad$O perceptron, desenvolvido em 1957 e serviu como fundamento para as redes neurais artificiais. Devido à sua arquitetura simples, ele apresenta a limitação de resolver apenas problemas linearmente separáveis, não sendo recomendado para tarefas complexas que exijam fronteiras de decisão não lineares. Porém, sua facilidade de implementação o torna ideal para mostrar o processo de aprendizado backpropagation e o papel dos pesos aplicados às variáveis de entrada. Sendo assim, seu uso é adequado para cenários lineares básicos e para fins didáticos

backpropagation: 


Fontes: 
[Universidade Federal do Paraná](https://docs.ufpr.br/~centeno/p_iarha/pdf/aula008_perceptron.pdf)
Livro Mãos a obra Aprendizado de máquina
[deeplearningbook](https://www.deeplearningbook.com.br/o-perceptron-parte-1/)
[Asimov Academy](https://hub.asimov.academy/tutorial/o-que-e-o-algoritmo-perceptron/)

