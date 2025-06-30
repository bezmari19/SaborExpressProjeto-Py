numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Julia', 'Pedro', 'Thiago', 'Agatha']
ano_nascimento = ['1998', '2025']

for i in numeros:
    print(i)
for nome in nomes:
    print(nome)
for ano in ano_nascimento:
    print(ano)

####################################################
impares = 0

for numero in numeros:
    if numero % 2 == 1:
        impares += numero

print(f'A soma dos impares é: {impares}')

###################################################
for numero in range(10, 0, -1):
    print(numero)

##################################################
numero_escolhido = int(input('Digite um número aqui:\n'))

print(f'A tabuada do numero: {numero_escolhido}')
for numero in range(1,11): #para cada numero na lista
    resultado = numero * numero_escolhido #será multiplicado pelo numero escolhido pelo usuário
    print(resultado)

###################################################
numeros_1 = [1,2,3,4,'none',6,7,8,9,10]
soma = 0

try:
    for numero in numeros_1:
        soma += numero
        print(f'A soma dos números é: {soma}')
except TypeError:
    print('Parece que algo está errado em sua lista, não foi possível fazer a soma\n')

###################################################
soma = 0
def media_lista_numeros(numeros):
        for numero in numeros:
            soma += numero
            print(numero)












