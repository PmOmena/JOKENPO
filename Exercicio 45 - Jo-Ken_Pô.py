import random
#Crie um programa que faça o computador jogar Jokenpô com voce.

itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0,2)
jogador = int(input('Qual é a sua jogada? '))
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print('-=' * 11)
print('JO!')
print('KEN!')
print('PÔ!')
print('-=' * 11)
print(f"Jogador jogou {itens[jogador]}")
print(f"O computador jogou {itens[pc]}")
print('-=' * 11)
if jogador == 0 and pc == 0:
    print('Empate!')
elif jogador == 0 and pc == 1:
    print('Vitória do Computador')
elif jogador == 0 and pc == 2:
    print('VITÓRIA DO JOGADOR!')
elif jogador == 1 and pc == 0:
    print('VITÓRIA DO JOGADOR!')
elif jogador == 1 and pc == 1:
    print('Empate!')
elif jogador == 1 and pc == 2:
    print('Vitória do Computador!')
elif jogador == 2 and pc == 0:
    print('Vitória do Computador!')
elif jogador == 2 and pc == 1:
    print('VITÓRIA DO JOGADOR!')
elif jogador == 2 and pc ==2:
    print('EMPATE!')
else:
    print('Resultado Inválido.')

