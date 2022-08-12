""" Faça um programa para uma escola que, dadas três notas obrigatórias de um aluno e seu nome completo, exiba, no final, o nome do estudante, notas, a média final e o seu conceito.""" 

aluno = input("Digite seu nome do aluno completo: ")
n1 = float(input("Digite sua 1ª nota: "))
n2 = float(input("Digite sua 2ª nota: "))
n3 = float(input("Digite sua 3ª nota: "))

lista_notas = [n1, n2, n3]
media = sum(lista_notas)/len(lista_notas)

if media >= 80:
  conceito = 'A'
elif media >= 50 and media < 80:
  conceito = 'B'
else:
  conceito = 'C'

lista_final = [aluno, n1, n2, n3]

print(f"\n{lista_final}")
print(f"{aluno} obteve conceito {conceito} em suas nota. \nAs 3 notas fornecidas como entrada foram: {lista_notas} com Média final: {media:.2f}")