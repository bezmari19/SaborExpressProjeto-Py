import os

#restaurantes = ['Pizza','Sushi']
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_programa():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Alternar estado do restaurante')
    print('4 - Sair do app\n')

def finalizar_app():
    exibir_subtitulo('Saindo do app...\nObrigado por escolhar o Sabor Express!\n')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu!')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar:\n")
    categoria = input(f"Digite a categoria do restaurante: {nome_restaurante}\n")
    dados_restaurantes = {'nome': nome_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_restaurantes)
    print(f'O restaurante cadastrado foi: {nome_restaurante}')

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"categoria".ljust(22)} Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(22)} | {categoria.ljust(22)} | {ativo.ljust(22)} \n')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante:\n')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:\n'))
        print(f'Você escolheu a opção: {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            #print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            listar_restaurantes()
            #print('Listar restaurantes')
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
             #print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    # Executa o código principal do aplicativo
    main()




