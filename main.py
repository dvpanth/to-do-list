''' TO DO LIST '''
import time
import os

todo = {}
STDSTATE = False
OPTIONS = "\n1. add\n2. view\n3. complete \n4. delete\n5. exit\n"

def clear_screen():
    os.system('cls' if os.name =='nt' else 'clear')

def prompt_add():
    name = input('Name your task: ')
    return name

def add_task(name):
    todo[name] = STDSTATE

def view_task(name):
    state = todo.get(name)
    if state is not None:
        if state:
            print('\nCompleted')
        else:
            print('\nNot Complete')
        time.sleep(2)

def complete_task(name):
    if name is not None:
        todo[name] = True

def prompt_selection(todo):
    names = [element for element in todo.keys()]
    if len(names) < 1: 
        print('\nNothing to select!')
        time.sleep(1)
    else:
        valid = False
        while not valid:
            try:
                selection = input(f'\nWhich task do you want to select? (1-{len(names)})')
                name = names[int(selection) - 1]
                valid = True
                return name
            except Exception as e:
                print(f"ERR: You only have {len(names)} tasks!")

def delete_task(name):
    if name is not None:
        del todo[name]

def print_todo():
    print('\n=== TO DO LIST ===\n')
    for key in todo.keys():
        print(f'- {key}')

run = True

while run:

    clear_screen()

    print_todo()

    print(OPTIONS)
    selection = input('==> ')

    if selection == '1':
        name = prompt_add()
        add_task(name)
    elif selection == '2':
        name = prompt_selection(todo)
        view_task(name)
    elif selection == '3':
        name = prompt_selection(todo)
        complete_task(name)
    elif selection == '4':
        name = prompt_selection(todo)
        delete_task(name)
    elif selection == '5':
        run = False