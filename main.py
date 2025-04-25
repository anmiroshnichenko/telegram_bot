import random

HELP = """
help - напечатать справку по  программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
random - добавлять случайную задачу на дату Сегодня.
exit - завершить работу."""

# RANDOM_TASK = "Посмотреть видео по Kubernetes"
RANDOM_TASKS = ["Посмотреть видео по Kubernetes", "Помыть машину", "ВЫучить английский", "Посмотреть Python", "Купить еду"]
tasks = {}
# today = list() # today = [] # список можно создать двумя способами: today = list() или today = []
# tomorrow = list() # tomorrow = []
# other = list() # other = []
run = True
# while run == True:
def add_todo(date, task):
    if date in tasks:
        # Дата   есть в словаре
        tasks[date].append(task)
    else:
        # tasks[date] = [task]
        tasks[date] = []
        tasks[date].append(task)
    print(f'Задача {task} добавлена на дату {date}')  
    # print("Задача", task, "добавлена на дату", date)

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Задач на такую дату нет")         
    elif command == "add":
        date = input("Введите дату добавления задачи: ")
        task = input("Введите название задачи: ")                
        add_todo(date, task)
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        run = False
    else:
        print("Неизвестная команда") 
        break
        # run = False
print("До свидания!")






