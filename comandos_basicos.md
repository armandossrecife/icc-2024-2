## Variáveis, Constantes, Operadores e Mais: Fundamentos da Programação

**Variáveis**

Imagine uma caixa com um rótulo. Essa caixa pode armazenar diferentes tipos de objetos, como números, palavras ou até mesmo outras caixas. Em programação, essa caixa é chamada de variável. Ela é utilizada para guardar dados que podem mudar durante a execução de um programa.

* **Declaração:** Antes de usar uma variável, você precisa declará-la, ou seja, informar ao computador o nome e o tipo de dado que ela irá armazenar. 
  * **Exemplo em Portugol:** `var numero: inteiro`
* **Atribuição:** Para colocar um valor dentro de uma variável, usamos o operador de atribuição `:=`. 
  * **Exemplo:** `numero := 10`

**Constantes**

Uma constante é como uma caixa com um cadeado. Uma vez que você coloca algo dentro, não pode mais mudar. Elas são utilizadas para valores que não se alteram durante a execução do programa.

* **Declaração:** 
  * **Exemplo em Portugol:** `const PI: real := 3.14159`

**Operadores**

Operadores são símbolos que realizam operações em valores.

* **Operadores Aritméticos:**
  * `+` (adição), `-` (subtração), `*` (multiplicação), `/` (divisão), `^` (potenciação)
  * **Exemplo:** `resultado := 5 + 3`
* **Operadores Relacionais:**
  * `=` (igual a), `<>` (diferente de), `<` (menor que), `>` (maior que), `<=` (menor ou igual a), `>=` (maior ou igual a)
  * **Exemplo:** `se idade >= 18 então`
* **Operadores Lógicos:**
  * `e` (AND), `ou` (OR), `não` (NOT)
  * **Exemplo:** `se (idade >= 18) e (altura >= 1.60) então`

**Entrada e Saída de Dados**

* **Entrada:** Permite que o usuário digite informações que serão armazenadas em variáveis.
  * **Exemplo em Portugol:** `leia(nome)`
* **Saída:** Exibe informações na tela.
  * **Exemplo:** `escreva("Olá, ", nome)`

**Comando if**

O comando `if` permite que o programa tome decisões com base em uma condição. Se a condição for verdadeira, um bloco de comandos é executado.

* **Sintaxe:**
  ```
  se condicao então
      comandos
  fimse
  ```
  * **Exemplo:**
  ```
  se idade >= 18 então
      escreva("Você é maior de idade.")
  fimse
  ```

**Comando if else**

O comando `if else` permite que o programa execute um bloco de comandos se a condição for verdadeira e outro bloco caso contrário.

* **Sintaxe:**
  ```
  se condicao então
      comandos1
  senão
      comandos2
  fimse
  ```
  * **Exemplo:**
  ```
  se aprovado então
      escreva("Parabéns, você foi aprovado!")
  senão
      escreva("Estude mais para a próxima.")
  fimse
  ```

**Exemplo Completo:**

```portugol
var
    nome: caractere
    idade: inteiro

inicio
    escreva("Digite seu nome: ")
    leia(nome)
    escreva("Digite sua idade: ")
    leia(idade)

    se idade >= 18 então
        escreva(nome, ", você é maior de idade.")
    senão
        escreva(nome, ", você é menor de idade.")
    fimse
fim
```

**Aplicações na Engenharia Mecânica:**

* **Cálculos:** Realizar cálculos complexos, como o cálculo de tensões em uma viga.
* **Simulações:** Simular o comportamento de sistemas mecânicos, como o movimento de um pêndulo.
* **Controle:** Controlar processos industriais, como a temperatura de um forno.
* **Análise de dados:** Analisar dados de sensores para monitorar o desempenho de equipamentos.
