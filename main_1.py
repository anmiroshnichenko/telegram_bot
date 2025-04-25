# # Создаем пустой словарь, в который затем будем добавлять записи
# task_dict = {}

# date = input ("Введите дату: ")
# task = input ("Введите задачу: ")
# task_dict[date] = task 


# date = input ("Введите дату: ")
# task = input ("Введите задачу: ")
# task_dict[date] = task  


# date = input ("Введите дату: ")
# task = input ("Введите задачу: ")
# task_dict[date] = task  

# name = input("Введите имя: ")
# login = "Alex"

# if name == login:
#     print("Hello,", name)
# elif len(name) < 3:
#     print("Такое имя недопустимо")
# elif name == "Al":
#     print("Al, bro")
# else:
#     print("Hello, user!")    

# print("The end")

# x = 1
# while x <= 10:
#     print(x)
#     x+=1

def multiply(a, b):
    print('a =', a)
    print('b =', b)
    result = a * b
    return result

# c = multiply(3, 3)
# c = multiply(3, 525)
# print(c)

def print_helloo():
    print('Hello')
    print('World')


def count_letter(list_worlds, letter):
    """Считает косличество слов с списке по заданному символу"""
    count = 0 # созаём счётчик
    for word in list_worlds:
        if letter.lower() in word.lower():  # приводим к нижнему регистру
            count += 1  # это тоже самое что и count = count + 1
    return count # возвращаем результат

list_worlds = ['python', 'c++', 'c', 'scala', 'java', 'C']
letter = 'c'

# result  = count_letter(list_worlds, letter)
# print(result)
    
# pip3 install --user PyTelegramBotApi


import telebot
# bot = telebot.TeleBot("TOKEN", parse_mode=None)
token = ""

bot = telebot.TeleBot(token)
my_name = 'Александр'
@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        text = 'Ба! Знакомые все лица!'
        # bot.send_message(message.chat.id, message.text)       
    else:
        text = message.text
    bot.send_message(message.chat.id, text)

# Постоянно  обращаеться к серверам телеграм
bot.polling(none_stop=True)



