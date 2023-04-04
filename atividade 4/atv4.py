lista_de_compras = []

while True:
    print("O que você deseja fazer?")
    print("1 - Inserir item na lista")
    print("2 - Apagar item da lista")
    print("3 - Listar itens da lista")
    print("4 - Sair do programa")

    opcao = input("> ")

    if opcao == "1":
        item = input("Digite o item a ser adicionado: ")

        lista_de_compras.append(item)

        print(f"O item '{item}' foi adicionado à lista de compras.")

    elif opcao == "2":
        print("Qual item você deseja apagar?")
        for i, item in enumerate(lista_de_compras):
            print(f"{i+1} - {item}")


        num_item = int(input("> "))


        item_removido = lista_de_compras.pop(num_item-1)


        print(f"O item '{item_removido}' foi removido da lista de compras.")

    elif opcao == "3":
        print("Itens da lista de compras:")
        for item in lista_de_compras:
            print(item)

    elif opcao == "4":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma das opções disponíveis.")