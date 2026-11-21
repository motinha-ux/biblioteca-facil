def cadastrar_livro():
    print("=====CADASTRAR LIVRO=====\n")

    nome=input("Digite o nome do livro: ")
    autor=input("Digite o nome do autor: ")

    with open("livros.txt","a") as arquivos:
        arquivos.write(nome+" - "+autor+ "\n")

    print("Livro cadastrado com sucesso!")    

def consultar_livros():
    print("=====LIVROS CADASTRADOS=====\n")

    with open("livros.txt","r") as arquivos:
        conteudo=arquivos.read()

    print(conteudo)

def exibir_menu():

    opcao=0
    while opcao!=5:
        print("=====BIBLIOTECA FACIL=====\n")
        
        print("1 - Cadastrar livro")
        print("2 - Consultar livro")
        print("3 - Atualizar livro")
        print("4 - Excluir livro")
        print("5 - Sair \n")

        opcao=int(input("Escolha uma opção: "))

        if opcao==1:
            cadastrar_livro()
        elif opcao==2:
            consultar_livros()
        elif opcao==3:
            print("Atualizar livro selecionado!")
        elif opcao==4:
            print("Excluir livro selecionado!")
        elif opcao==5:
            print("Menu encerrado!!!")
        else:
            print("Opção invalida")