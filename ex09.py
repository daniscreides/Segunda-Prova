# Escreva um algoritmo para ler uma quantidade de números inteiros desconhecida como entrada e possa armazená-los em uma lista. O programa deve imprimir a lista de entradas de forma ordenada,  e ainda remover todos os números negativos antes da impressão. Para este algoritmo, a leitura do valor zero (0) indicará o final da entrada de dados.

entrada = 1
lista = []

while entrada != 0:
  entrada = int(input("Digite um número: "))
  lista.append(entrada)

  if entrada == 0 or entrada < 0:
    lista.pop()

lista.sort()

print(f"\nA lista ordenada com os números de entrada positivos é {lista}")