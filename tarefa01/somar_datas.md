### Somar Datas
A) A entrada desse problema é uma data e um número que pertence ao conjunto dos números inteiros. Já a saída é uma única data. Para cada conjunto de uma data e um número na entrada só temos uma saída possível.

B) Segue o algoritmo:
1.  Analise o mês da data recebida, se for mês 02, guarde o valor 29, se for o mês for 01, 03, 05, 07, 08, 10 ou 12, guarde o valor 31 e se for qualquer outro, guarde o valor 30;
2.  Faça a soma do numero recebido com o dia da data recebia;
3.  Caso o valor da soma do passo anterior seja menor ou igual ao valor guardado no passo nº 1, substitua o dia da data recebida pelo valor da soma;
4.  Mostre essa data e finalize o algoritmo;
5.  Caso o valor da soma seja maior que o valor guardado no passo nº2, siga os próximos passos;
6.  Faça a divisão da soma obtida no passo nº2 pelo valor guardado no 1º passo, guarde tanto o resultado da divisão como o seu resto;
7.  Substitua o dia da data recebida pelo valor do resto da divisão do passo anterior;
8.  Faça a soma do valor da divisão do passo nº6 com o mês da data recebida;
9.  Caso o valor da soma do passo anterior seja menor ou igual a 12, substitua o mês da data recebida por esse valor;
10. Mostre essa data e finalize o algoritmo;
11. Caso o valor da soma do passo nº8 seja maior que 12, siga os próximos passos;
12. Faça a divisão da soma obtida no passo nº8 por 12, guarde tanto o resultado da divisão como o seu resto;
13. Substitua o mês da data recebida pelo valor do resto da divisão do passo anterior;
14. Adicione no ano da data recebida, o valor da divisão do passo nº12;
15. Mostre essa data;
