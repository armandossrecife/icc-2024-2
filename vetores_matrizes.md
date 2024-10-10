## Vetores e Matrizes: Estruturas de Dados Fundamentais

**Vetores**

Um vetor é como uma lista ordenada de elementos do mesmo tipo. Imagine uma fila de pessoas, cada uma com um número. Essa fila seria um vetor, e cada pessoa seria um elemento.

* **Declaração:**
  ```portugol
  var
      notas: vetor[1..10] de real
  ```
  Esse código declara um vetor chamado `notas` que pode armazenar até 10 números reais.
* **Acesso:**
  Para acessar um elemento específico, usamos o índice. O primeiro elemento tem índice 1.
  ```portugol
  escreva(notas[3])  // Imprime o terceiro elemento do vetor
  ```
* **Operações:**
  * Atribuição: `notas[5] := 9.5`
  * Leitura: `leia(notas[1])`
  * Percorrendo todos os elementos:
    ```portugol
    para i <- 1 até 10
        escreva(notas[i])
    fimpara
    ```

**Matrizes**

Uma matriz é como uma tabela, com linhas e colunas. Cada elemento é identificado por dois índices: linha e coluna.

* **Declaração:**
  ```portugol
  var
      matriz: matriz[1..3, 1..4] de inteiro
  ```
  Essa matriz tem 3 linhas e 4 colunas, e armazena números inteiros.
* **Acesso:**
  ```portugol
  escreva(matriz[2, 3])  // Imprime o elemento na segunda linha e terceira coluna
  ```
* **Operações:**
  * **Atribuição:** `matriz[1, 2] := 15`
  * **Percorrendo todos os elementos:**
    ```portugol
    para i <- 1 até 3
        para j <- 1 até 4
            escreva(matriz[i, j])
        fimpara
    fimpara
    ```

**Exemplos de Aplicação em Engenharia Mecânica**

* **Armazenar coordenadas:** Um vetor pode armazenar as coordenadas (x, y, z) de um ponto no espaço. Uma matriz pode armazenar as coordenadas de vários pontos.
* **Representar matrizes de rigidez:** Em análise estrutural, as matrizes de rigidez são usadas para descrever o comportamento de elementos estruturais.
* **Armazenar dados de sensores:** Os dados de vários sensores podem ser armazenados em uma matriz, onde cada linha representa um sensor e cada coluna representa um ponto no tempo.
* **Resolver sistemas de equações lineares:** Matrizes são fundamentais para resolver sistemas de equações lineares, que surgem em diversos problemas de engenharia.

**Exemplo: Cálculo da média de notas**

```portugol
var
    notas: vetor[1..5] de real
    i: inteiro
    soma, media: real

inicio
    para i <- 1 até 5
        escreva("Digite a nota ", i, ": ")
        leia(notas[i])
        soma := soma + notas[i]
    fimpara

    media := soma / 5
    escreva("A média das notas é: ", media)
fim
```

**Exemplo: Multiplicação de matrizes**

```portugol
// ... (declaração das matrizes A e B)

var
    C: matriz[1..linhaA, 1..colunaB] de real
    i, j, k: inteiro

// ... (cálculo da multiplicação, utilizando os índices i, j e k)
```

**Considerações Adicionais**

* **Linguagens de Programação:** A sintaxe e as funcionalidades podem variar entre as linguagens.
* **Vetores Dinâmicos:** Algumas linguagens permitem que o tamanho do vetor seja ajustado durante a execução do programa.
* **Matrizes Multidimensionais:** É possível criar matrizes com mais de duas dimensões.
* **Bibliotecas Numéricas:** Bibliotecas como NumPy (Python) e MATLAB oferecem funções especializadas para trabalhar com vetores e matrizes.
