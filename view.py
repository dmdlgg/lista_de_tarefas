import flet as ft
from cont import cadastrar 
from cont import mostrar

def main (page: ft.Page):
    page.title = "Lista de Tarefas"

    nome_tarefa = ft.Text('Qual tarefa você deseja adicionar?')
    tarefa = ft.TextField(label="insira a tarefa aqui")
    save_btn = ft.ElevatedButton('Salvar', on_click=cadastrar)
    show_btn = ft.ElevatedButton('Mostrar tarefas', on_click=mostrar)

    page.add(
        nome_tarefa,
        tarefa,
        save_btn,
        show_btn
    )

ft.app(target=main)