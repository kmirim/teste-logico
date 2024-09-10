# Teste lógico

O teste é composto por quatro questões que foram solucionadas em Python. A seguir, farei uma breve descrição da abordagem feita em cada um dos casos. Eu mandei como programa, pois fica mais fácil de verificar se a implementação está correta e realiando as tratativas adequadas. Em todos foram incluidas as tratativas para que fosse recebido um número, caso não fosse, retornar um erro.

1) Programa que irá fatorar um número: 
+ Fiz através de recurssão, é mais próximo do conceito matemático, e por conta disso, mais intuitivo também. 
+ Em relação ao desempenho: pode acabar sendo menos eficiente por ser alocado na stack. 
+ Como a fatoração é sempre o valor que o usuário informará multiplicado por ele, menos um, até chegar em 1 ou 0. Comecei desconsiderando os negativos. Diferente do `while`, a condição de parada será quando entrar na condição do número ser == 1 ou == 0.

2) Programa que retorna se houve aprovação, prova final ou reprovação:
+ Foi feita a tratativa para aceitar notas até 10.
+ Inclui uma função para retornar o valor da média, assim o retorno será utilizado para verificar se a pessoa foi aprovada, reprovada ou está em prova final.

3) Programa para calcular a distância euclidiana entre dois pontos: 
+ Primeiro compreender a lógica matemática por trás do calculo, em resumo é descrita em: distância entre dois pontos que resultará em x, e depois em y. Elevar ao quadrado os valores encontrados, para depois a raiz quadrada para que seja possivel verificar a distancia entre os pontos no plano.
+ Estruturação das tuplas, para que seja incluida as coordenadas de x e y.

4) Programa para retornar a sequência de fibonacci até a posição informada: 
+ Feito através de recurssão, em linguagem python tive dificuldade de implementar através de uma lista, mas posso mandar a lógica e implementação em c. O que acabou pela não inclusão de toda a sequência até o número informado. 
+ A sequência de fibonacci é a soma dos dois anteriores. Sendo assim, fica mais intuitivo fazer sem `while`. 
+ Mais no geral, com a implementação que eu fiz, imagino que daria certo se fosse armazenado o valor em um array, e depois printa-lo. Começando com `0, 1, 1, 2`.
