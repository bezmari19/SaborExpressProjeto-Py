import os

def exibir_nomePrograma():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Ativar restaurante')
    print('4 - Sair do app\n')

def finalizar_app():
    os.system('cls')
    print('Saindo do app...\nObrigado por escolhar o Sabor Express!\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção:'))
    print(f'Você escolheu a opção: {opcao_escolhida}\n')

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nomePrograma()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    # Executa o código principal do aplicativo
    main()




