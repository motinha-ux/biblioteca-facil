def cadastrar_livro():
    print("=====CADASTRAR LIVRO=====\n")

    nome=input("Digite o nome do livro: ")
    autor=input("Digite o nome do autor: ")
    
    if nome=="" or autor=="":
        print("Nome ou autor vazio ao cadastrar livro. Tente novamente!")
    else:
        with open("livros.txt","a") as arquivos:
          arquivos.write(nome+" - "+autor+ "\n")

        print("Livro cadastrado com sucesso!")    

def consultar_livros():
    print("=====LIVROS CADASTRADOS=====\n")

    try:
        with open("livros.txt","r") as arquivos:
            conteudo=arquivos.read()
            livros=conteudo.splitlines()

        if conteudo=="":
            print("Nenhum livro cadastrado!")
        else:
            for i in range(len(livros)):
                print(f"{i+1}. {livros[i]}")

    except FileNotFoundError:
        print("Arquivo não encontrado!")    

def atualizar_livro():
    try:
        with open("livros.txt","r") as arquivos:
            conteudo=arquivos.read()
            livros=conteudo.splitlines()
        
            for i in range(len(livros)):
                print(f"{i+1}. {livros[i]}")
        
        livro_antigo=input("Digite o nome e autor do livro que deseja atualizar: ")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return
    
    encontrado=False
    for i in range(len(livros)):
        if livros[i]==livro_antigo:
            print("Livro encontrado!\n")
            encontrado=True
            print("Podemos atualizar o livro!")

            novo_nome=input("Digite o novo nome do livro: ")
            novo_autor=input("Digite o novo nome do autor do livro: ") 
            livros[i]=novo_nome + " - " + novo_autor
            break
        
    if encontrado:
        if novo_nome=="" or novo_autor=="":
            print("Nome ou autor vazio ao atualizar livro. Tente novamente!")    
        else:
            with open("livros.txt","w") as arquivos:
                for livro in livros:
                    arquivos.write(livro + "\n")
        
            print("Livro atualizado com sucesso!")
        
    else:
        print("Livro não encontrado!")

def excluir_livro():
    try:
        print("=====EXCLUIR LIVRO=====")
        with open("livros.txt","r") as arquivos:
          conteudo=arquivos.read()
          livros=conteudo.splitlines()

        print("=====LIVROS CADASTRADOS=====")
        for i in range(len(livros)):
            print(f"{i+1}. {livros[i]}")
    
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return
    
    livro_excluir=input("Digite o nome e autor do livro que deseja excluir: ")

    encontrado=False
    for i in range(len(livros)):
        if livros[i]==livro_excluir:
            print("Livro encontrado!\n")
            encontrado=True
            del livros[i]
            break

    if encontrado:
        with open("livros.txt","w")as arquivos:
            for livro in livros:
                arquivos.write(livro + "\n")

        print("Livro excluido com sucesso!")
    else: 
        print("Livro não encontrado")

def exibir_menu():

    opcao=0
    while opcao!=5:
        print("=====BIBLIOTECA FACIL=====\n")
        
        print("1 - Cadastrar livro")
        print("2 - Consultar livro")
        print("3 - Atualizar livro")
        print("4 - Excluir livro")
        print("5 - Sair \n")

        try:
            opcao=int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números na opção!!!")
            continue

        if opcao==1:
            cadastrar_livro()
        elif opcao==2:
            consultar_livros()
        elif opcao==3:
            atualizar_livro()
        elif opcao==4:
            excluir_livro()
        elif opcao==5:
            print("Menu encerrado!!!")
        else:
            print("Opção invalida")