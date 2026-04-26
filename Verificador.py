def Senha():
    Pin = []
    while True:
        print("1 - adicionar: ")
        print("2 - Remover: ")
        print("3 - armazenado: ")
        print("4 - ver a lista armazenada")
        print("5 - Sair...")
        print("\n")
        opcao = input("escolha: ")
        
        if opcao == "1":
            senha=input("digite a senha nova: ")
            Pin.append(senha)
            print("senha adicionada!\n")
        
        elif opcao == "2":
            senha=input(" Remover: ")
            if senha in Pin:
                Pin.remove(senha)
                print(f"O Pin {senha} foi removido...\n")
            else:
                 print(f"O Pin {senha} não esta na lista...\n")
                 
        elif opcao == "3":
            senha = input("Digite o Pin: ")
            if senha in Pin:
                print(f"O Pin {senha} está armazenado!\n")
            else:
                print(f"O Pin {senha} não está armazenado!\n")
                
        elif opcao == "4":
            if Pin:
                print("\n a lista armazenada\n")
                for i, senha in enumerate(Pin, start=1):
                    print(f"{senha}")
            else:
                print("A lista está vazia.\n")
                
        elif opcao == "5":
            print("Sainda...")
            break
        else:
            print("Não armazedo...")
            
    return Pin
           
def menu():
    print("1 - Verficador de numero ")
    print("2- alfabeto")
    print("3-alfanumerico")
    print("4- Maioscula e menuscula")
    print("5 - So tem espaço")
    print("6-Saindo.....")
    print("\n")
                
password = Senha()

if not password:
    print("Nenhuma senha cadastrada")
else:
    Inserir = input("\n Digite o Pin: ")
    
    if Inserir in password:
        print("\n acesso liberado...\n")
        while True:
            menu()
            subopcao = input("escolha a: ")
        
            if  subopcao == "1":
                a = input("digite: ")
                print(f"É um numero? {a.isnumeric()}")
                
            elif subopcao == "2":
                b =input("Insira: ")
                print(f"É um alfabeto? {b.isalpha()}")
            
            elif subopcao == "3":
                c =input("Digite: ")
                print(f"É um alfanumerico? {c.isalnum}")
        
            elif subopcao == "4":
                d =input("Insira: ")
                print(f"É maior e menor? {d.istitle()}")
        
            elif subopcao == "5":
                e = input("Digite: ")
                print(f"So tem espaço? {e.isspace()}")
        
            elif subopcao == "6":
                print("Saindo....")
                break
            
            else:
                print("Opção inválida!")
        else:
            print("Pin errado!......")
            
    
    