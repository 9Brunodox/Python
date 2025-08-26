import contatos

opcoes = [1, 2, 3, 4, 5, 6]

def main():
    while True:
        print()
        print("1- Ver agenda de contatos")
        print("2- Adicionar um contato")
        print("3- Editar um contato")
        print("4- Excluir um contato")
        print("5- Tornar um contato favorito")
        print("6- Sair")
        print()
        try:
            escolha = int(input("Digite uma opção: "))
            if escolha not in opcoes:
                print("Escolha inválida")
            match escolha:
                case 1:
                    print("======== AGENDA =======")
                    contatos.listar_contatos()
                    print("=======================")
                case 2:
                    nome = input("Digite o nome do contato: ")
                    telefone = int(input("Digite o telefone do contato (Somente números): "))
                    email = input("Digite o email do contato: ")
                    favoritar = input("Contato é favorito? Sim / Não\n R:")
                    favorito = True if favoritar.lower() == "sim" else False
                    contatos.adicionar_contato(nome, email, telefone, favorito)
                case 3:
                    contatos.editar_contato()
                case 4:
                    contatos.remover_contato()
                case 5:
                    contatos.marcar_como_favorito() 
                case 6:
                    break     
        except TypeError as e:
            print(f"Erro: {e}")

main()