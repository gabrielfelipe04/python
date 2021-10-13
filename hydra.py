def barra():
    print('-' * 30)


def clear():
    print('\n' * 10)

users = ['']
senhas = ['']


def cadastrar():
    print('Novo usuário: ')
    new_user = input()
    clear()
    print('A senha deve conter:\n- No máximo 6 digitos\n- Apenas números\nSenha:  ')
    new_pass = int(input())
    repeat_pass = int(input('Digite novamente: '))
    if new_pass == repeat_pass:
        users.append(new_user)
        senhas.append(repeat_pass)
        menu()
    else:
        print('-' * 30)
        print('Senhas diferentes')  # 1ª Verificação
        print('-' * 30)
        cadastrar()


def login():
    user = input('Login: ')
    if user in users:
        senha = int(input('Senha: '))
        if senha == senhas[users.index(user)]:
            print(f'Bem-vindo(a), {user}')  # 3ª Verificação
        else:
            print('Senha inválida')  # 4ª Verificação
            login()
    else:
        print('Usuário inválido!')  # 2ª Verificação
        login()


def comando():
    c = int(input('c://hydra > '))
    if c == 1:
        cadastrar()
    elif c == 2:
        login()
    elif c == 3:
        # Terminal
        print('Terminal')
        pass
    else:
        print('Digite um comando válido')
        comando()


def menu():
    print('-' * 30)
    print('DIGITE UM COMANDO:')
    print('1 - Cadastrar')
    print('2 - Login')
    print('3 - Terminal')
    print('-' * 30)
    comando()


menu() 

def menu():
    barra()
    print('ESCOLHA UMA OPÇÃO ABAIXO: ')
    print('1 - Cadastrar\n2 - Entrar\n3 - Hackear')
    barra()
    escolha()


menu()
