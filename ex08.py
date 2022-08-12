# Reescreva a questão 7 anterior pesquisando na Web ou em livros se, no Python, existe alguma função utilitária já pronta da linguagem capaz de encontrar o maior número dentro de uma lista.

lista = []

while True:
  entrada = int(input("Digite um número: "))
  if entrada == 0:
    break
  lista.append(entrada)
  maior = max(lista)

print(f"\nLista dos números de entrada: {lista}")
print(f"O maior número da lista é {maior} e ele ocupa o índice {lista.index(maior)}")