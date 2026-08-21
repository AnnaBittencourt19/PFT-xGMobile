Exercício 18: Considere que uma antena transmissora localizada a 450 metros de altitude está distante 85 quilômetros de uma antena receptora com 625 metros de altitude. A 56 quilômetros da antena transmissora tem-se  um obstáculo gume de faca com 543 metros de altura. Determinar:
$\lambda = 3\times10^8/3,6\times10^9 = 0,0833$ m
$d_1 = 56$ km, $d_2 = 29$ km
$$h_v = 450 + (625-450)\cdot\frac{56}{85} = 565,29\ m$$
$$H = 543 - 565,29 = -22,29\ m$$
$$\rho_1 = \sqrt{\frac{0,0833\cdot 56000\cdot 29000}{85000}} = 39,90\ m$$
$H/\rho_1 = -0,559$ -> o obstáculo libera 55,9% do primeiro elipsoide
a) O acréscimo na atenuação devido a esse obstáculo, para a frequência de 3,6 GHz.
$$V_o = \frac{-22,29\sqrt2}{39,90} = -0,790$$
$$A_{obs} = -20\log(0,5 - 0,62\cdot(-0,790)) = -20\log(0,9899) = 0,09\ dB$$

b) A potência na recebida considerando um transmissor de 80 watts e ganhos das antenas de transmissão e recepção de 30 e 35 dBi, respectivamente. Considere as perdas de cabos e conectores iguais a 10 dB no enlace como um todo.
$$A = 92,44 + 20\log(3,6) + 20\log(85) - 30 - 35 = 77,15\ dB$$
$P_T = 10\log(80000) = 49,03$ dBm
$$P_R = 49,03 - 77,15 - 10 - 0,09 = -38,21\ dBm$$

c) Qual a perda total do enlace
$$L = 77,15 + 10 + 0,09 = 87,24\ dB$$
