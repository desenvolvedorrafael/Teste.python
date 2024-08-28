def sauda():
    print("bem vindo ao site")
    name = input('qual seu nome?')
    print("bem vindo,", name + "!")


def menu(): 
    print("como posso te ajudar ?")
    print("1-camiseta 3d ?")
    print("2-disgn da camiseta de anime")
    print("3-camiseta de design de filme da marvel")

    opcao = int(input("digite o numero de opcao selecionada:"))

    if opcao == 1:
        print("4-disgn de camiseta serire")

    elif opcao == 2:
        print("1-disgn da camiseta de anime")

    elif opcao == 3:
        print ("1-camisa com design 3d")

    else:
        print("opcao incorreta aperte na opçâo correta ")
        
sauda()
menu()