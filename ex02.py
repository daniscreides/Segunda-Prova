"""Reescreva a questão 1 anterior pesquisando na Web ou em livros se, no Python, existe alguma função utilitária já pronta da linguagem capaz de somar os números de uma lista"""

lista = []
entrada = 1
while entrada != 0:
  entrada = int(input("Digite um número: "))
  lista.append(entrada)
  soma = sum(lista)
  if entrada == 0:
    lista.pop()
print(f"\nA lista de entrada é {lista}")
print(f"A soma final calculada é {soma}")