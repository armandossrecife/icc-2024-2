# Introdução às Funções em Python

## Objetivo

Compreender o conceito de funções em Python, sua sintaxe e aplicações, de forma a capacitar os alunos a utilizá-las para resolver problemas computacionais de baixa complexidade.

---

## 1. O que é uma função?

Uma função é um bloco de código que executa uma tarefa específica e pode ser reutilizado em diferentes partes do programa. Em Python, funções permitem:

- Modularizar códigos complexos.
- Reutilizar código, reduzindo repetição.
- Melhorar a clareza e a organização.

### Exemplo do dia a dia:

Uma função pode ser comparada a uma receita. Você fornece os ingredientes (dados de entrada), segue os passos (código), e obtém um resultado (saída).

---

## 2. Sintaxe de uma Função em Python

### Declaração de Função

```python
# Exemplo básico de uma função

def saudacao(nome):
    """
    Função que exibe uma mensagem de saudação.
    Parâmetros:
        nome (str): Nome da pessoa a ser saudada.
    """
    print(f"Olá, {nome}! Bem-vindo!")
```

### Estrutura:

- **`def`**: Palavra-chave para definir uma função.
- **`saudacao`**: Nome da função.
- **`(nome)`**: Parâmetros entre parênteses.
- **`:`**: Indica o início do bloco de código da função.
- **`docstring`**: Descrição da função.

### Chamando a Função

```python
saudacao("João")
# Saída: Olá, João! Bem-vindo!
```

---

## 3. Tipos de Funções

### 3.1 Funções Sem Retorno

Executam uma tarefa, mas não retornam valores.

```python
def exibir_mensagem():
    print("Engenharia de Produção: unindo tecnologia e gestão!")

def main():
    exibir_mensagem()
```

### 3.2 Funções Com Retorno

Devolvem um resultado utilizando a palavra-chave `return`.

```python
def calcular_area_retangulo(base, altura):
    return base * altura

area = calcular_area_retangulo(5, 10)
print(f"Área: {area} m²")
# Saída: Área: 50 m²
```

### 3.3 Funções Com Valores Padrão

Permitem definir valores padrão para os parâmetros.

```python
def calcular_salario(horas_trabalhadas, valor_hora=25):
    return horas_trabalhadas * valor_hora

salario = calcular_salario(40)
print(f"Salário: R${salario}")
# Saída: Salário: R$1000
```

---

## 4. Exemplos

### Exemplo 1: Cálculo simplificado da Eficiência de Produção

```python
def eficiencia(producao_real, producao_teorica):
    """
    Calcula a eficiência de produção em percentual.
    """
    return (producao_real / producao_teorica) * 100

ef = eficiencia(850, 1000)
print(f"Eficiência: {ef:.2f}%")
# Saída: Eficiência: 85.00%
```

### Exemplo 2: Cálculo de Custos Fixos e Variáveis

```python
def custo_total(custos_fixos, custos_variaveis):
    return custos_fixos + sum(custos_variaveis)

custos_fixos = 2000
custos_variaveis = [500, 800, 1200]

custo = custo_total(custos_fixos, custos_variaveis)
print(f"Custo Total: R${custo}")
# Saída: Custo Total: R$4500
```

---

## 5. Boas Práticas

- **Nomes Significativos**: Use nomes que indiquem claramente a função do código.
- **Documentação**: Sempre inclua `docstrings` para explicar o propósito e os parâmetros da função.
- **Modularização**: Divida problemas grandes em múltiplas funções pequenas.
- **Evite Repetições**: Reutilize funções para evitar código duplicado.

---
