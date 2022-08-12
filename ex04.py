"""Assuma que seu programa possui a seguinte lista de nomes de clientes da empresa:
clientes = ['caio', 'wellington', 'pedro', 'bruno', 'ana', 'caio', 'bruno', 'david', 'pedro']
Escreva um algoritmo que seja capaz de verificar se um dado nome passado como entrada se encontra na lista e, se existir, informar o número de ocorrências.
Escreva um algoritmo que seja capaz de receber um nome passado como entrada e remover todas as ocorrências deste nome na lista
Escreva um algoritmo capaz de receber um nome passado como entrada e possa retornar a posição da primeira ocorrência de um dado nome na lista. Se o nome não existir, deve-se retornar o valor -1 sinalizando posição inválida não encontrada
Escreva um algoritmo capaz de receber um nome passado como entrada e possa retornar a posição da última ocorrência de um dado nome na lista. Se o nome não existir, deve-se retornar o valor -1 sinalizando posição inválida não encontrada"""

clientes = ['caio', 'wellington', 'pedro', 'bruno', 'ana', 'caio', 'bruno', 'david', 'pedro']

nome = input("Digite um nome: ")
print(f"\nO nome {nome} aparece na lista {clientes.count(nome)} vez")

if nome in clientes:
  print(f"O índice que o nome {nome} aparece na primeira ocorrência é o {clientes.index(nome)}")
else:
  print("-1")

contador = 0
for k in clientes:
  if k == nome:
    clientes.pop(contador)
  contador += 1
  
print(f"\nLista sem a ocorrência de nomes: \n{clientes}")