#1 - Imprima a frase: Python na Escola de Programação da Alura
print('Python na Escola de Programação da Alura.\n')

#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = input('Escreva seu nome aqui:')
idade = input('Coloque sua idade aqui:')
print(f'Olá meu nome é {nome} e tenho {idade} anos!')

#3 - Imprima a frase: Estudo Python na Alura! (adicional que coloquei ao exercício) em que cada letra da palavra Alura deve ser impressa em uma linha diferente.
print('Estudo Python na Alura!')
print('\n','A\n', 'L\n', 'U\n', 'R\n', 'A\n')

#4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
valor_pi = 3.14159
print(f'O valor arredondado de pi é: {valor_pi:.2f}')