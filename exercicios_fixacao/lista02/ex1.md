### Algoritmo da soma de dois números
<br/>
a) Para esse problema, o conjunto de entradas será um conjunto composto por dois números inteiros, por exmeplo (10,5). Já o conjunto de saídas válidas serão somente um número inteiro. Para o exemplo citado, por exemplo, a saída seria 15

b) Para resolver esse problema, as instruções elementares são:
- Ler os números da entrada;
- Mostrar um valor na tela;
- Escrever um número em uma folha;
- Identificar unidade, dezena, centena, milhar, etc..., de cada número;
- Comparar entre dois números e ver qual é o maior ou menor, ou se eles são iguais;
- Identificar qual número está abaixou ou acima de outro número;
- Contar a quantidade de algarismos de um número;
  
c) Segue o algoritmo para a resolução do problema:

- Guarde 0 na variável "cont"
- Leia o primeiro número e guarde na variável "n1"; 
- Leia o segundo número e guarde na variável "n2"; 
- Compare "n1" com "n2", guarde o número maior na variável "maior" e o outro número na "menor";
- Guarde na variável "tamanho" a quantidade de algarismos de "maior";
- Escreva "maior" em uma folha;
- Escreva, abaixo de "maior" alinhando as unidades de ambos os números, a variável "menor";
- Enquanto "cont" for menor que "tamanho":
    - Some o termo de "maior" com o termo abaixo de "menor" e guarde na variável "t_soma";
    - Se houver um termo acima do termo do termo de "maior":
        - Some esse número com "t_soma" e guarde em "t_soma";
    - Se "t_soma" for maior ou igual a 10:
        - Coloque embaixo dos termos somados somente a unidade de "t_soma" e coloque a dezena em cima do próximo termo de "maior";
    - Some 1 em "cont";  
- Mostre o número obtido abaixo de "menor";
<br/><br/>
- Nesse caso, eu utilizei o "enquanto" que é uma iteração condicional e o "se" que é uma execução condicional.