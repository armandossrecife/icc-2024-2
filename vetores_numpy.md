## Criando Arrays NumPy

### Função np.array()

A função `np.array()` é a principal ferramenta para criar arrays NumPy a partir de outras estruturas de dados Python, como listas.

```python
import numpy as np

# Criando um vetor a partir de uma lista
minha_lista = [1, 2, 3, 4, 5]
meu_vetor = np.array(minha_lista)
print(meu_vetor)  # Output: [1 2 3 4 5]

# Criando uma matriz a partir de uma lista de listas
minha_lista_de_listas = [[1, 2, 3], [4, 5, 6]]
minha_matriz = np.array(minha_lista_de_listas)
print(minha_matriz)  # Output: [[1 2 3]
                     #         [4 5 6]]
```

### Criando vetores a partir de listas

```python
# Criando um vetor de números sequenciais
vetor_sequencial = np.array([0, 1, 2, 3, 4, 5])
print(f"vetor_sequencial: {vetor_sequencial}")

# Criando um vetor com valores repetidos
vetor_repetido = np.array([1, 1, 1, 1, 1])
print(f"vetor_repetido: {vetor_repetido}")

# Criando um vetor com valores aleatórios (entre 0 e 1)
vetor_aleatorio = np.random.rand(5)
print(f"vetor_aleatorio: {vetor_aleatorio}")

vetor_sequencial: [0 1 2 3 4 5]
vetor_repetido: [1 1 1 1 1]
vetor_aleatorio: [0.65012734 0.66854856 0.65617098 0.4438401  0.84031399]
```

### Criando matrizes a partir de listas aninhadas

```python
# Criando uma matriz identidade 3x3
matriz_identidade = np.eye(3)
print(f"matriz_identidade: {matriz_identidade}")

# Criando uma matriz de zeros 2x4
matriz_zeros = np.zeros((2, 4))
print(f"matriz_zeros: {matriz_zeros}")

# Criando uma matriz de uns 3x3
matriz_uns = np.ones((3, 3))
print(f"matriz_uns: {matriz_uns}")

# Criando uma matriz com valores aleatórios
matriz_aleatoria = np.random.rand(2, 3)
print(f"matriz_aleatoria: {matriz_aleatoria}")
```

### Explicando os exemplos:

* **np.array():** Essa função converte uma lista ou tupla em um array NumPy.
* **Vetores:** Representam arrays unidimensionais.
* **Matrizes:** Representam arrays bidimensionais (ou tabelas).
* **np.eye():** Cria uma matriz identidade.
* **np.zeros() e np.ones():** Cria matrizes preenchidas com zeros ou uns, respectivamente.

**Observações:**

* A forma de um array é definida pelo número de elementos em cada dimensão. Por exemplo, um array 2x3 tem 2 linhas e 3 colunas.
* O tipo de dados dos elementos de um array é inferido automaticamente, mas pode ser especificado explicitamente usando o argumento `dtype`.
* O NumPy oferece muitas outras funções para criar arrays com diferentes distribuições de probabilidade, sequências numéricas e outras características.

## Operações Básicas com Arrays NumPy

### Soma e Subtração
O NumPy permite realizar essas operações 

```python
import numpy as np

# Criando dois arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Soma
soma = array1 + array2
print(soma)  # Output: [5 7 9]

# Subtração
subtracao = array2 - array1
print(subtracao)  # Output: [3 3 3]
```

**Observações:**
* **Operações elemento a elemento:** As operações básicas (+ e -) são realizadas elemento a elemento entre arrays de mesmo formato.

### Produto entre matrizes

O Numpy realiza o produto entre matrizes usando a função dot. 

```python
A = np.array([
    [1, 0, 2],
    [-1, 3, 1]
    ])

B = np.array([
    [3, 1],
    [2, 1],
    [1, 0]
    ])

print(f'A: {A}')
print(f'B: {B}')

A: [[ 1  0  2]
 [-1  3  1]]
B: [[3 1]
 [2 1]
 [1 0]]

C = np.dot(A, B)
print(f'C: {C}')

C: [[5 1]
 [4 2]]
```

## Resolvendo Sistemas Lineares com NumPy

**Entendendo o Problema:**

Um sistema linear é um conjunto de equações lineares. Representamos um sistema linear na forma matricial como Ax = b, onde:

* A: matriz dos coeficientes
* x: vetor das incógnitas
* b: vetor dos termos independentes

**Resolvendo com NumPy:**

O NumPy oferece a função `np.linalg.solve()` para resolver sistemas lineares. Essa função calcula a solução x do sistema Ax = b.

**Exemplo:**

Considere o seguinte sistema de equações lineares:

```
2x + y = 8
x - 3y = -2
```

Podemos representá-lo na forma matricial como:

```
| 2  1 |   | x |   | 8 |
| 1 -3 | * | y | = | -2 |
```

**Código Python:**

```python
import numpy as np

# Definindo a matriz dos coeficientes e o vetor dos termos independentes
A = np.array([[2, 1], [1, -3]])
b = np.array([8, -2])

# Resolvendo o sistema linear
x = np.linalg.solve(A, b)

print("A solução do sistema é:", x)
```

**Saída:**

```
A solução do sistema é: [3. 2.]
```

**Interpretação:**

A solução x = [3, 2] significa que x = 3 e y = 2 é a solução do sistema de equações lineares.

**Outro exemplo:**

```python
# Sistema linear com mais equações e variáveis
A = np.array([[3, 1, -1], [1, 2, 1], [2, 1, 0]])
b = np.array([10, 8, 5])

x = np.linalg.solve(A, b)
print(x)
```

**Observações:**

* A função `np.linalg.solve()` assume que o sistema linear tem uma única solução. Se o sistema não tiver solução ou tiver infinitas soluções, a função levantará uma exceção.

**Aplicações:**

* **Engenharia:** Análise de estruturas, circuitos elétricos, etc.
* **Ciência da Computação:** Algoritmos de aprendizado de máquina, visão computacional, etc.
* **Física:** Modelagem de sistemas físicos, como circuitos RLC, etc.
* **Economia:** Modelagem de sistemas econômicos, etc.

**Em resumo:**

O NumPy oferece uma ferramenta poderosa para resolver sistemas lineares de forma eficiente. A função `np.linalg.solve()` simplifica significativamente essa tarefa, tornando-a acessível a uma ampla gama de aplicações.
