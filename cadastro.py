from time import sleep

# cria uma lista vazia para armazenar os usuários cadastrados
usuarios = []

#---- função para exibir o menu de opções para o usuário--------------------------
def mostrar_menu():
    sleep(0.7)
    print('=='*22)
    print('----- SISTEMA DE CADASTRO DE USUÁRIOS -----')
    print('1 - Cadastrar usuário')
    print('2 - Mostrar usuários')
    print('3 - Buscar usuário')
    print('4 - Remover usuário')
    print('0 - Sair')
    print('-'*20)

#---- função para cadastrar usuários com nome e idade--------------------------
def cadastrar_usuario():
    nome = input('Digite o nome do usuário: ')
    while True:
        idade = input('Digite a idade do usuário: ')
        try:
            idade = int(idade)
            break
        except ValueError:
                print('Idade inválida! Digite novamente.')
    user = {
        "nome": nome,
        "idade": idade
    }
    # adiciona o usuário à lista de usuários cadastrados
    usuarios.append(user)
    print('-'*20)
    sleep(0.2)
    print('Usuário cadastrado com sucesso!')
    
#---- função para mostrar a lista de usuários cadastrados--------------------------
def mostrar_usuarios():
    if len(usuarios) == 0:
        print('-'*20)
        sleep(0.2)
        print('Não há nenhum usuário cadastrado.')
    else:
        print('-'*20)
        sleep(0.2)
        print('Lista de usuários cadastrados:')
        # percorre a lista de usuários e enumera os usuários, exibindo o nome e a idade de cada um
        for i, user in enumerate(usuarios):
            print(f"{i+1} - Nome: {user['nome']} | Idade: {user['idade']} ")

#---- função para buscar um usuário pelo nome e exibir suas informações--------------------------
def buscar_usuario():
    if len(usuarios) == 0:
        print('-'*20)
        sleep(0.2)
        print('Ainda não foram cadastrados nenhum usuário.')
    else:
        nome_busca = input('Digite o nome do usuário que deseja buscar: ')
        # percorre a lista de usuário em usuário e verfica se a busca contém o nome do usuário
        usuarios_encontrados = [user for user in usuarios if nome_busca.lower() in user['nome'].lower()]
        if len(usuarios_encontrados) > 0:
            print('-'*20)
            sleep(0.2)
            print('Usuário encontrado:')
            for user in usuarios_encontrados:
                print(f"Nome: {user['nome']} | Idade: {user['idade']} ")
        else:
            print('-'*20)
            sleep(0.2)
            print('Usuário não encontrado.')

#---- função para remover um usuário pelo nome--------------------------
def remover_usuario():
    if len(usuarios) == 0:
        print('-'*20)
        sleep(0.2)
        print('Ainda não foram cadastrados nenhum usuário.')
    else:
        nome_remover = input('Digite o nome do usuário que deseja remover: ')
        # percorre a lista de usuário em usuário e verfica se a busca contém o nome do usuário para remover
        usuarios_removidos = [user for user in usuarios if nome_remover.lower() in user['nome'].lower()]
        if len (usuarios_removidos) > 0:
            for user in usuarios_removidos:
                print('-'*20)
                sleep(0.2)
                print(f"O usuário de Nome: {user['nome']} | Idade: {user['idade']} será removido.")
                while True:
                    confirmacao = input('Deseja confirmar a remoção? [S/N]: ').upper()
                    if confirmacao == 'S':
                        usuarios.remove(user)
                        print('Usuário removido com sucesso!')
                        break
                    elif confirmacao == 'N':
                        print('Remoção cancelada.')
                        break
                    else:
                        print('Opção inválida!')
        else:
            print('-'*20)
            sleep(0.2)
            print('Usuário não encontrado.')

# loop principal do programa para exibir o menu e processar as opções escolhidas pelo usuário
while True:
    mostrar_menu()
    sleep(0.5)
    opcao = input('Digite uma opção: ')
    if opcao == '0':
        print('-'*20)
        print('Sistema finalizado.')
        break
    elif opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        mostrar_usuarios()
    elif opcao == '3':
        buscar_usuario()
    elif opcao == '4':
        remover_usuario()
    else:
        print('Opção inválida! Digite uma opção válida.')
sleep(0.5)
print('Agradecemos por utilizar nossos serviços!')



