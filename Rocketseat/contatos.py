contatos = [
    {'nome': 'Maria', 'telefone': '21987654321', 'email': 'maria@email.com', 'favorito': False},
    {'nome': 'Bruno', 'telefone': '11940028922', 'email': 'bruno@email.com', 'favorito': True},
    {'nome': 'Ana', 'telefone': '41955554444', 'email': 'ana@email.com', 'favorito': True},
    {'nome': 'João', 'telefone': '31912345678', 'email': 'joao@email.com', 'favorito': False}
]

def listar_contatos():
    if not contatos:
        print("Não há contatos registrados!")
        return
    contatos_ordenados = sorted(contatos, key=lambda contato: contato['favorito'], reverse=True)


    for index, contato in enumerate(contatos_ordenados, start=1):
        marcador = "★" if contato['favorito'] == True else "✆"

        telefone_formatado = formatar_telefone(contato['telefone'])
        print(f"{index}. {marcador} {contato['nome']} - {telefone_formatado}")
    return contatos_ordenados

def adicionar_contato(nome, email, telefone, favorito=False):
    novo_contato = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'favorito': favorito
    }

    contatos.append(novo_contato)
    print(f"Novo contato adicionado!")

def editar_contato():
    try:
        numero = int(input("\nDigite o número do contato que deseja editar: "))
        indice = numero - 1

        if 0 <= indice <= len(contatos):
            contato_selecionado = contatos[indice]

            while True:
                print("Informações do contato: ")
                print(f"Nome: {contato_selecionado['nome']}")
                print(f"Nome: {contato_selecionado['telefone']}")
                print(f"Nome: {contato_selecionado['email']}")
                print()
                print("O que deseja editar?")
                escolha = input("Nome / Telefone / Email / Digite 0 para sair\n R:")
                if escolha.lower() == "nome":
                    novo_nome = input("Digite o novo nome: ")
                    contatos[indice]['nome'] = novo_nome
                elif escolha.lower() == "telefone":
                    novo_telefone = int(input("Digite o novo número de telefone (Somente números): "))
                    contatos[indice]['telefone'] = novo_telefone
                elif escolha.lower() == "email":
                    novo_email = input("Digite o novo email: ")
                    contatos[indice]['email'] = novo_email
                elif escolha == "0":
                    break
         
    except ValueError as e:
        print(f"Erro: {e}")

def remover_contato():
    todos_contatos = sorted(contatos, key=lambda contato: contato['favorito'], reverse=True)

    try:
        numero = int(input("\nDigite o número do contato para favoritar: "))
        indice = numero - 1

        if 0 <= indice < len(contatos):
            contato_selecionado = todos_contatos[indice]

            nome_contato_selecionado = todos_contatos[indice]['nome']

            for contato_original in contatos:
                if contato_original['nome'] == nome_contato_selecionado:
                    contatos.remove(contato_selecionado)
                    print(f"\nO contato '{contato_selecionado['nome']}' foi removido!.")
        else:
            print("\nErro: Número do contato inválido.")
    except ValueError:
        print("\nErro: Por favor, digite um número.")

def marcar_como_favorito():
    todos_contatos = sorted(contatos, key=lambda contato: contato['favorito'], reverse=True)

    try:
        numero = int(input("\nDigite o número do contato para favoritar: "))
        indice = numero - 1

        if 0 <= indice < len(contatos):
            contato_selecionado = todos_contatos[indice]

            nome_contato_selecionado = todos_contatos[indice]['nome']

            for contato_original in contatos:
                if contato_original['nome'] == nome_contato_selecionado:
                    if not contato_selecionado['favorito']:
                        contato_original['favorito'] = True
                        print(f"\n★ Contato '{contato_selecionado['nome']}' favoritado com sucesso!")
                    else:
                        print(f"\nO contato '{contato_selecionado['nome']}' já é um favorito.")
        else:
            print("\nErro: Número do contato inválido.")
    except ValueError:
        print("\nErro: Por favor, digite um número.")

def formatar_telefone(numero):
    # Primeiro, removemos qualquer caractere que não seja um dígito
    # Isso torna a função robusta, mesmo que o número já esteja meio formatado
    numero_limpo = "".join(filter(str.isdigit, numero))
    
    tam = len(numero_limpo)

    # Celular com DDD (11 dígitos, ex: 11940028922)
    if tam == 11:
        ddd = numero_limpo[:2]
        parte1 = numero_limpo[2:7]
        parte2 = numero_limpo[7:]
        return f"({ddd}) {parte1}-{parte2}"
        # Se não se encaixar em nenhum formato, retorna o número como está
    else:
        return numero
