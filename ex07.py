# Escreva um algoritmo que, mediante uma lista de números inteiros não ordenada, possa informar a posição (o index) do maior elemento dentro da lista

lista = []
maior = 0

while True:
  entrada = int(input("Digite um número: "))
  if entrada == 0:
    break
  lista.append(entrada)
  
  if entrada > maior:
    maior = entrada

print(f"\nLista dos números de entrada: {lista}")
print(f"O maior número da lista é {maior} e ele ocupa o índice {lista.index(maior)}")


