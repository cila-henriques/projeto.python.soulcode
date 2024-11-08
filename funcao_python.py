import os

restaurantes = ['Pizza', 'Margareti Compani'],

def opcao_menu():
    try:
        opcao = int(input("Escolha a sua opcao? "))
        if opcao == 1:
            print("1. Cadastrar Restaurante")
        elif opcao == 2:
            print(" 2. Listar Restaurante")
        elif opcao == 3:
            print("3. Ativar Restaurante")
        elif opcao == 4:
            print("4. Sair")
        else:
            opcao_invalidade()     
    except:
        opcao_invalidade()
           
def apresentar_menu():
    print('Tela de Cadastro\n')
    print("1 Cadastrar Restaurante")
    print("2 Listar Restaurante")
    print("3 Ativar Restaurante")
    print("4 Sair")

def opcao_invalidade():
    print("Opção Inválida!")

def finaliza_app(): 
    os.system('cls')
    #os.system('clear')
    print('Finalizando o app')

def cadastrar_restaurante():
    os.system("cls")
    print("Cadastro de Novos Restaurantes")
    no

def main():
    apresentar_menu()
    opcao_menu()
 
if __name__ == '__main__':
    main()
   


