def adicionar_tarefa(tarefas, nome_tarefa):
    
    tarefa = {"Tarefa": nome_tarefa, "Completa": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada.")

def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["Completa"] else "x"
        nome_tarefa = tarefa["Tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefas(tarefas, indice, novo_nome):
    tarefas[indice] = {"Tarefa": novo_nome, "Completa": False}
    print("Novo da tarefa atualizado!")
        
tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas: ")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Remover terafeas completadas")
    print("6. Sair")
    
    escolha = int(input("Digite sua escolha: "))
    
    if escolha == 1:
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == 2:
        ver_tarefas(tarefas)
    elif escolha == 3:
        numero_tarefa = int(input("Escolha a tarefa: "))
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefas(tarefas, numero_tarefa, novo_nome)
    elif escolha == 6:
        break

print("Saindo do programa...")
        