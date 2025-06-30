import os

restaurantes = []

def exibir_nome_programa():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Ativar restaurante')
    print('4 - Sair do app\n')

def finalizar_app():
    os.system('cls')
    print('Saindo do app...\nObrigado por escolhar o Sabor Express!\n')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar:\n")
    restaurantes.append(nome_restaurante)
    print(f'O restaurante cadastrado foi: {nome_restaurante}')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:\n'))
        print(f'Você escolheu a opção: {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            #print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
             print('Ativar restaurante')
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




