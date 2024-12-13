# Programa da Calculadora modularizado em funcoes

# Area de declaracao das funcoes do programa
def informacoes():
  print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
  print("Bem vindo ao programa mini-calculadora")
  print("Este programa faz a soma, multiplicação, subtração e divisão")
  print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

def entrada_dados():
  n1 = float(input("Informe o primeiro número:"))
  n2 = float(input("Informe o seguendo número:"))
  return n1, n2

def soma(n1, n2):
  # processamento das entradas de dados
  adicao = n1 + n2
  # devolve o resultado da adicao
  return adicao

def subtracao(n1, n2):
  sub = n1 - n2
  return sub

def multiplicacao(n1, n2):
  m = n1 * n2
  return m

def divisao(n1, n2):
  d = n1/n2
  return d

# Area de execucao do programa chamando as funcoes e demais instrucoes
informacoes()
print("Soma dois numeros")
n1, n2 = entrada_dados()
s = soma(n1, n2)
print("A soma dos números é:",s)
print("-------------------------------")

print("Multiplica dois numeros")
n1, n2 = entrada_dados()
m = multiplicacao(n1, n2)
print("O produto dos números é:",m)
print("-------------------------------")

print("Subtrai dois numeros")
n1, n2 = entrada_dados()
sub = subtracao(n1, n2)
print("A subtração dos números é:",sub)
print("-------------------------------")

print("Divisão de dois numeros")
n1, n2 = entrada_dados()
d = divisao(n1, n2)
print("A divisão dos números é:",d)
print("-------------------------------")
