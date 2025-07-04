#3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
for i in range(1,6):
  numero_quadrados = i**2
  print(numero_quadrados)

#########################################################################################
#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
dados_pessoa = {'nome':'Marina', 'idade':27, 'cidade':'São Paulo', 'profissao':'programadora', 'altura':1.60}
chave = input('informe qual a chave que você deseja verificar:\n')
if chave in dados_pessoa:
    print('voce possui um chave valida!')
else:
    print('Essa chave não existe nas informações.')

##########################################################################################
#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
codigo = 'Estou estudando python a mais de um ano e estou gostando muito e quero me aperfeiçoar muito!'
contagem_codigo = {}
palavras = codigo.split()
for palavra in palavras:
  contagem_codigo[palavra] = contagem_codigo.get(palavra, 0) + 1
print(contagem_codigo)
