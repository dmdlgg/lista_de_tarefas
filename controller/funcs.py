import flet as ft

tarefas = []

def cadastrar(t):
    tarefas.append(t)
    print(f'tarefa cadastrada: {t}')


def mostrar(ts, page):
    for tarefa in ts:
        page.add(ft.Text(tarefa))
    page.update()

 
