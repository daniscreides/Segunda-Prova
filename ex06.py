# Escreva um programa que leia um conjunto de números inteiros de tamanho desconhecido e os armazene em uma lista. O programa deve ser capaz de informar ao usuário quantos números pares existem na lista. Um número é considerado par quando o resto da divisão inteira por 2 (dois)  é igual a 0 (zero), ou seja: (num % 2) == 0. Para este algoritmo, a leitura do valor zero (0) indicará o final da leitura de entrada de dados

entrada = 1
lista = []
pares = 0

while entrada != 0:
  entrada = int(input("Digite um número: "))
  lista.append(entrada)

  if entrada == 0:
    lista.pop()

  if entrada % 2 == 0:
    pares += 1

print(f"\nQuantidade de números de entrada: {lista}")
print(f"A quantidade de números pares é {pares-1}")