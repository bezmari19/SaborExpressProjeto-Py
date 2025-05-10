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


#3.1 (Avançado) - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e#3.1 (SUGESTÃO AVANÇADA) - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
#Atualizando o código para verificação
import re #importando a biblioteca que permite verificar se a senha contém números, letra e caracteres especiais (o padrão para a força da senha)

nome = input('Digite o seu nome de usuário:\n')
senha = input('Digite a sua senha:\n')

def verificar_forca_senha(senha): #Essa Função verifica a força da senha a partir de alguns critérios (import re) 
    #verifica se a senha contém números
    tem_numero = bool(re.search(r'\d', senha))
    #verifica se a senha contém letras minusculas
    tem_letra = bool(re.search(r'[a-z]', senha)) 
    #verifica se a senha contém letras maiusculas
    tem_letra_maiuscula = bool(re.search(r'[A-Z]', senha))
    #verifica se a senha contém caracteres especiais
    tem_caractere_especial = bool(re.search(r'[!@#$%&*()_+\-=\[\]{};:,.?]', senha))

#Abaixo, são criados critérios para verificar a força da senha com base nos padrões definidos acima
    #Senha fraca: menos de 6 caracteres ou apenas números ou apenas letras
    if len(senha) < 6: 
        return 'fraca'
    #Senha fraca: contém letras e números, mas não contém letras maiusculas ou caracteres especiais
    elif len(senha) >= 6 and not tem_numero and not tem_letra:
        return 'fraca'
    #Senha média: contém letras e números, mas não contém letras maiusculas ou caracteres especiais e não é menor que 6
    elif len(senha) >= 6 and not tem_numero and tem_letra and not tem_letra_maiuscula and not tem_caractere_especial:
        return 'média'
    #Senha forte: contém letras, números, letras maiuculas e caracteres especiais
    elif len(senha) >= 6 and tem_numero and tem_letra and tem_letra_maiuscula and not tem_caractere_especial:
        return 'forte'
    else:
        return 'inválida'

forca = verificar_forca_senha(senha) #A váriavel criada armazena a força da senha a partir da função e os critérios criados acima 

#Aqui, se aplica a estrtura da função para verificar e imprimir ao usuário a força da senha e se é permitido a entrada ou não
#A força da senha é verificada e, com base nos critérios definidos é impresso ao usuários se a senha foi aceita ou não para login
if forca == 'fraca': #Se a senha for fraca, o usuários deve tentar uma nova senha
    print('Senha fraca, tente novamente')
elif forca == 'média': #Se a senha for média, o usário deverá tentar uma nova senha, mas mais encrenmentada
    print('Senha média, tente novamente ainda não é segura')
elif forca == 'forte': #Se a senha for forte, o usuário pode acessar o sistema
    print('Senha forte')
    print(f'Acesso permitido! Seja bem-vindo(a) {nome}')
#Se a senha atender a nenhum critério, o usuário deve tentar mais uma vez ou sair do sistema
else:
    print('Senha inválida! Não atende a nenhum dos requisitos, tente novamente ou clique em sair') 

#3.2 (SIMPLES)
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

if x > 0 and y > 0: #atualizado (x and y > 0) para (x > 0 and y > 0)
    print('Esse ponto está no primeiro quadrante')
elif x < 0 and y > 0:
    print('Esse ponto está no segundo quadrante do plano cartesiano')
elif x and y < 0:
    print('Esse ponto está no terceiro quadrante do plano cartesiano')
elif x > 0 and y < 0:
    print('O ponto está no quarto quadrante do plano cartesiano')
else:
    print('Esse ponto deve estar localizado no eixo ou na sua origem')
