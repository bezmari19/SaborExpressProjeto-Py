numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Julia', 'Pedro', 'Thiago', 'Agatha']
ano_nascimento = ['1998', '2025']

#para cada item da lista
#imprime cada componente da lista
for i in numeros:
    print(i)
for nome in nomes:
    print(nome)
for ano in ano_nascimento:
    print(ano)

####################################################
#para cada numero impar da lista, faz a soma
#imprime a soma de todos os números impares
impares = 0

for numero in numeros:
    if numero % 2 == 1:
        impares += numero

print(f'A soma dos impares é: {impares}')

###################################################
#faz a contagem descrente dos números da lista
for numero in range(10, 0, -1):
    print(numero)

##################################################
#para o número que o usuário quer escolher terá a tabuada
#para cada numero da lista, faz a multplicação com o numero escolhido
#imprime o resultado da conta em ordem crescente
numero_escolhido = int(input('Digite um número aqui:\n'))

print(f'A tabuada do numero: {numero_escolhido}')
for numero in range(1,11): #para cada numero na lista
    resultado = numero * numero_escolhido #será multiplicado pelo numero escolhido pelo usuário
    print(resultado)

###################################################
#para cada item da lista, tenta rodar e exibe uma mensagem caso não seja possivel ou não tenha um elemento
#TENTATIVA 1:
numeros_1 = [1,2,3,4,'none',6,7,8,9,10]
soma = 0

try:
    for numero in numeros_1:
        soma += numero
        print(f'A soma dos números é: {soma}')
except TypeError:
    print('Parece que algo está errado em sua lista, não foi possível fazer a soma\n')

#TENTATIVA 2:
lista_numerica = [10,15,20,25,5,]
soma_numerica= 0

try:
    for numero in lista_numerica:
        soma_numerica += numero
        print(f'A soma dos número da lista são: {soma_numerica}')
except Exception as i:
    print(f' Ocorreu um erro: {i}')

##################################################
#para cada item da lista faz a contagem da média
#imprime o resultado
#coloca as exceções caso haja uma divisão por 0 ou houver um erro na lista
lista_de_numeros = [10,9,7,2,3,4,8]
soma_numeros = 0

try:
    for i in lista_de_numeros:
        soma_numeros += i
        media = soma_numeros/len(lista_de_numeros)
        print(f'A média dos valores listados é: {media}')
except ZeroDivisionError:
    print('A lista está fazia, não é possível seguir com o cálculo da média')
except Exception as e:
    print(f' Ocorreu um erro: {e}')













