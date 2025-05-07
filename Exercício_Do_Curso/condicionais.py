#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input('Digite um número:\n'))

if numero % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

idade = int(input('Qual a sua idade?\n'))

 if idade >= 0 and idade <= 12:
    print('Criança')
 elif idade >= 13 and idade <= 18:
    print('Adolescente')
 elif idade > 18 and idade <= 59:
    print('Adulto')
 else:
    print('Idoso')

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

nome = input('Digite o seu nome de usuário:\n')
senha = input('Digite a sua senha:\n')

