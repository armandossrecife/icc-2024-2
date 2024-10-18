## Estruturas de Repetição: Laços de Repetição (para, enquanto)

Estruturas de repetição, também conhecidas como laços, permitem que um bloco de comandos seja executado repetidamente enquanto uma determinada condição for verdadeira. Elas são essenciais para automatizar tarefas repetitivas e processar grandes volumes de dados.

**Laço para:**

* **Sintaxe:**
  ```
  para variavel <- valor_inicial até valor_final passo passo
      comandos
  fimpara
  ```
* **Funcionamento:**
  1. Uma variável é inicializada com um valor inicial.
  2. A condição é verificada: a variável é comparada com o valor final.
  3. Se a condição for verdadeira, os comandos dentro do laço são executados.
  4. A variável é incrementada (ou decrementada) pelo valor do passo.
  5. As etapas 2, 3 e 4 são repetidas até que a condição se torne falsa.

**Exemplo:**
```
para i <- 1 até 10 passo 1
    escreva(i)
fimpara
```
Este código irá imprimir os números de 1 a 10 na tela.

**Laço enquanto:**

* **Sintaxe:**
  ```
  enquanto condicao
      comandos
  fimenquanto
  ```
* **Funcionamento:**
  1. A condição é verificada.
  2. Se a condição for verdadeira, os comandos dentro do laço são executados.
  3. A condição é verificada novamente.
  4. As etapas 2 e 3 são repetidas até que a condição se torne falsa.

**Exemplo:**
```
i <- 1
enquanto i <= 10
    escreva(i)
    i <- i + 1
fimenquanto
```
Este código também irá imprimir os números de 1 a 10 na tela.

**Quando usar cada tipo de laço:**

* **Laço para:** Quando se sabe exatamente quantas vezes o bloco de comandos deve ser executado.
* **Laço enquanto:** Quando a quantidade de repetições depende de uma condição que pode mudar durante a execução do programa.
