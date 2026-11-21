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

def atualizar_livro():
    with open("livros.txt","r") as arquivos:
        conteudo=arquivos.read()
        livros=conteudo.splitlines()
        
    print(livros)
    livro_antigo=input("Digite o nome e autor do livro que deseja atualizar: ")

    encontrado=False
    for i in range(len(livros)):
        if livros[i]==livro_antigo:
            print("Livro encontrado!\n")
            encontrado=True
            print("Podemos atualizar o livro!")

            novo_nome=input("Digite o novo nome do livro: ")
            novo_autor=input("Digite o novo nome do autor do livro: ") 
            livros[i]=novo_nome + " - " + novo_autor
        
    if encontrado:
        with open("livros.txt","w") as arquivos:
            for livro in livros:
                arquivos.write(livro + "\n")
        
        print("Livro atualizado com sucesso!")
        
    else:
        print("Livro não encontrado!")

def excluir_livro():
    pass

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
            atualizar_livro()
        elif opcao==4:
            print("Excluir livro selecionado!")
        elif opcao==5:
            print("Menu encerrado!!!")
        else:
            print("Opção invalida")