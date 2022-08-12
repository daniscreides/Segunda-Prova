"""Reescreva a questão 1 anterior de forma que o programa deve agora ser capaz de informar ao usuário a média dos números da lista e ainda montar e imprimir uma sub-lista contendo apenas os números que estiverem acima da média calculada. Verifique se, no Python, existe alguma função utilitária da linguagem capaz de calcular a média dos números de uma lista"""

import numpy

entrada = 1
lista = []
sub_lista = []

while entrada != 0:
  entrada = int(input("Digite um número: "))
  lista.append(entrada)
  if entrada == 0:
    lista.pop()
  
  media = numpy.mean(lista) 
print(f"\nA média dos números de entrada é {media:.2f}")

for i in lista:
  if i > media:
    sub_lista.append(i)

print(f"A lista dos números de entrada acima da média é {lista}")