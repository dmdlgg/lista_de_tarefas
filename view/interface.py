import flet as ft


from controller.funcs import cadastrar, mostrar, tarefas

def main (page: ft.Page):
    page.title = "Lista de Tarefas"

    page.clean()
    nome_tarefa = ft.Text('Qual tarefa você deseja adicionar?')
    tarefa = ft.TextField(label="insira a tarefa aqui")
    save_btn = ft.ElevatedButton('Salvar', on_click=lambda e: cadastrar(tarefa.value))
    show_btn = ft.ElevatedButton('Mostrar tarefas', on_click=lambda _: task_page(page))

    layout = ft.Column(
            [
                nome_tarefa,
                tarefa,
                save_btn,
                show_btn
            ],
            alignment="center",
            horizontal_alignment="center",
        )


    page.add(layout)

def task_page(page: ft.Page):
    page.clean()
    page.add(ft.Text('Tarefas Atuais:'))
    back_btn = ft.ElevatedButton('Voltar', on_click=lambda _: main(page))
    mostrar(tarefas, page)
    
    page.add(
        ft.Container(
            back_btn,
            alignment = ft.alignment.center
        )
        )
