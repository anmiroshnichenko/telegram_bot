import telebot
import  random

# bot = telebot.TeleBot("TOKEN", parse_mode=None)
token = ""

bot = telebot.TeleBot(token)

HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show - напечатать все добавленные задачи.
/random - добавлять случайную задачу на дату Сегодня.
/exit - завершить работу."""

RANDOM_TASKS = ["Посмотреть видео по Kubernetes", "Помыть машину", "Выучить английский", "Посмотреть Python", "Купить еду"]

tasks = {}

def add_todo(date, task):
    if date in tasks:
        # Дата   есть в словаре
        tasks[date].append(task)
    else:
        # tasks[date] = [task]
        tasks[date] = []
        tasks[date].append(task)    

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def  random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message): # message.text = /print <date>
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[  ] " + task + "\n"
    else:
        text = "Задач на эту дату нет"    
    bot.send_message(message.chat.id, text)    



# Постоянно  обращаеться к серверам телеграм
bot.polling(none_stop=True)
