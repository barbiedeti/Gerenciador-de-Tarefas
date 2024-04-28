class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Tarefa adicionada com sucesso!")

    def view_tasks(self):
        if self.tasks:
            print("Tarefas:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Não há tarefas para exibir.")

    def mark_task_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] += " (Concluída)"
            print("Tarefa marcada como concluída.")
        else:
            print("Índice de tarefa inválido.")

    def mark_task_incomplete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = self.tasks[task_index - 1].replace(" (Concluída)", "")
            print("Tarefa marcada como incompleta.")
        else:
            print("Índice de tarefa inválido.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Tarefa removida: {removed_task}")
        else:
            print("Índice de tarefa inválido.")
    def show_task_details(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            print(f"Tarefa {task_index}: {self.tasks[task_index - 1]}")
        else:
            print("Índice de tarefa inválido.")



def main():
    task_manager = TaskManager()

    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar uma nova tarefa")
        print("2. Visualizar todas as tarefas")
        print("3. Marcar uma tarefa como concluída")
        print("4. Marcar uma tarefa como incompleta")
        print("5. Remover uma tarefa")
        print("6. Sair do programa")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = input("Digite a nova tarefa: ")
            task_manager.add_task(task)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_index = int(input("Digite o índice da tarefa a ser marcada como concluída: "))
            task_manager.show_task_details(task_index)
            task_manager.mark_task_complete(task_index)
        elif choice == "4":
            task_index = int(input("Digite o índice da tarefa a ser marcada como incompleta: "))
            task_manager.show_task_details(task_index)
            task_manager.mark_task_incomplete(task_index)
        elif choice == "5":
            task_index = int(input("Digite o índice da tarefa a ser removida: "))
            task_manager.show_task_details(task_index)
            task_manager.remove_task(task_index)
        elif choice == "6":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()