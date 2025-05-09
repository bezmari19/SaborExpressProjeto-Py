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

#3.1 (SUGESTÃO AVANÇADA) - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

import re

nome = input('Digite o seu nome de usuário:\n')
senha = input('Digite a sua senha:\n')

def verificar_forca_senha(senha):
    tem_numero = bool(re.search(r'\d', senha)) 
    tem_letra = bool(re.search(r'[a-z]', senha)) 
    tem_letra_maiuscula = bool(re.search(r'[A-Z]', senha))  
    tem_caractere_especial = bool(re.search(r'[!@#$%&*()_+\-=\[\]{};:,.?]', senha))

    if len(senha) < 6: 
        return 'fraca'
    elif tem_numero and tem_letra and not tem_letra_maiuscula and not tem_caractere_especial:
        return 'fraca'
    elif tem_numero and tem_letra and tem_letra_maiuscula and not tem_caractere_especial:
        return 'média'
    elif tem_numero and tem_letra and tem_letra_maiuscula and tem_caractere_especial:
        return 'forte'
    else:
        return 'inválida'

forca = verificar_forca_senha(senha)

if forca == 'fraca':
    print('Senha fraca, tente novamente')
elif forca == 'média':
    print('Senha média, tente novamente')
elif forca == 'forte':
    print('Senha forte')
    print(f'Acesso permitido! Seja bem-vindo(a) {nome}')
else:
    print('Senha inválida, tente novamente!')

#3.2 (SIMPLES) - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

nome_usuario = input('Digite aqui o seu nome de usuário:\n')
senha_usuario = input('Digite aqui a senha que você deseja utilizar:\n')

nome_usuario = 'Marina123@'
senha_usuario = 'Marina@123'

if nome_usuario == 'Marina123@' and senha_usuario == 'Marina@123':
    print('Acesso permitido!\nSeja bem-vind(a) Marina!')
else:
    print('Acesso negado!\nNome de usuário ou senha incorretos!')

#4 Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

x = float(input('Digite aqui a coordenada x:\n'))
y = float(input('Digite aqui a coordenada y:\n'))

if x and y > 0:
    print('Esse ponto está no primeiro quadrante')
elif x < 0 and y > 0:
    print('Esse ponto está no segundo quadrante do plano cartesiano')
elif x and y < 0:
    print('Esse ponto está no terceiro quadrante do plano cartesiano')
elif x > 0 and y < 0:
    print('O ponto está no quarto quadrante do plano cartesiano')
else:
    print('Esse ponto deve estar localizado no eixo ou na sua origem')
    