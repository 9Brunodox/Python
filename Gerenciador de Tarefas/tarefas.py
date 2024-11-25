def adicionar_tarefa(tarefas, nome_tarefa):
    
    tarefa = {"Tarefa": nome_tarefa, "Completa": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada.")

def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["Completa"] else "x"
        nome_tarefa = tarefa["Tarefa"]
        indice_ajustado = indice + 1
        print(f"{indice_ajustado}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefas(tarefas, indice, novo_nome):
    tarefas[indice] = {"Tarefa": novo_nome, "Completa": False}
    print("Novo da tarefa atualizado!")
    
def completar_tarefas(tarefas, indice):
    indice_ajustado = int(indice) - 1
    tarefas[indice_ajustado]["Completa"] = True
    print(f"Tarefa {indice} marcada como completa!")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["Completa"]:
            tarefas.remove(tarefa)
        print("As tarefas que foram completadas foram excluídas com sucesso!")
    return
        
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
    elif escolha == 4:
        ver_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa que deseja marcar como completa: "))
        completar_tarefas(tarefas, indice)
    elif escolha == 5:
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == 6:
        break

print("Saindo do programa...")
        