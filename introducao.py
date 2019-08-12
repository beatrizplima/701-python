import statistics as es

historia_n1 = float(input('Digite sua nota: '))
historia_n2 = float(input('Digite sua nota: '))

# soma = historia_n1 + historia_n2
# media = soma/2
# print('Sua média é: ' + str(media))

lista_notas = [historia_n1, historia_n2]
media =  es.mean(lista_notas)
print(media)

if media >= 7:
    print('O aluno está aprovado')

elif media >= 5 and media < 7:
    print('O aluno está de recuperação')

else:
    print('O aluno está reprovado')