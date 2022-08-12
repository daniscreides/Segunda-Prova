"""Escreva um programa para ler uma quantidade de números inteiros desconhecida como entrada e possa calcular a soma destes números. Armazene os números de entrada em uma lista. O programa deve imprimir a lista de entrada e a soma final calculada. Para este algoritmo, a leitura do valor zero (0) indicará o final da leitura de entrada de dados."""

lista = []
entrada = 1
soma = 0
while entrada != 0:
  entrada = int(input("Digite um número: "))
  soma += entrada
  lista.append(entrada)
  if entrada == 0:
    lista.pop()
print(f"\nA lista de entrada é {lista}")
print(f"A soma final calculada é {soma}")