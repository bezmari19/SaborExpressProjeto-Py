#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

informacoes = {'nome':'Marina', 'idade':'27', 'cidade':'São Paulo'}


#Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.

def mudar_idade():
    idade = input('Digite a idade atual:\n')
    informacoes['idade'] = idade
    print(f'Sua idade foi atualizada com sucesso.\n')
    print(f'Sua idade no cadastro é: {informacoes.get("idade"), informacoes.get("nome"), informacoes.get("cidade")}')


def adicionar_profissao():
    profissao = input('Digite a profissão:\n')
    informacoes['profissao'] = profissao
    print(f'A profissão foi adicionada com sucesso.\n')
    print(informacoes.get('nome'), informacoes.get('idade'), informacoes.get('cidade'), informacoes.get('profissao'))


def deletar_informacao():
    item_remove = input('Digite o item que deseja remover:\n')
    if item_remove in informacoes:
        del informacoes[item_remove]
        print(f"A informação '{item_remove}' foi removida.")
        print(informacoes)
    else:
        print(f"A informação '{item_remove}' não foi encontrada no dicionário.")


def main():
    mudar_idade()
    adicionar_profissao()
    deletar_informacao()

if __name__ == '__main__':
    # Executa o código principal do aplicativo
    main()

