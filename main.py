from python_aternos import Client
from getpass import getpass
import telebot
from telebot import types
from mcstatus import BedrockServer
import time
import mcpi.minecraft as minecraft

token = "5858885502:AAGVemFEDWVuVatngARlX7AQQIx5jJrTzPs"
id = []
global stoped
stoped = False
ip = "Sanya__Craft.aternos.me"
port = "36747"
version = "1.19.51"
name = "SanyaCraft"

def start_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton("🎮Запустить сервер")
        b2 = types.KeyboardButton("📋Данные сервера")
        b3 = types.KeyboardButton("😏БонУс")
        markup.add(b1, b2, b3)
        bot.send_message(message.chat.id, f"""==========================
СЕРВЕР {name}:
==========================
Сыграни в сервак Дяди Сани, а то нахрен ты здесь тогда?""", reply_markup=markup)

    def serv_checker(message):
        i = False
        while i is False:
            if stoped is True:
                return stoped == False
            else:
                time.sleep(300)
                i = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton("🔁Перезапустить сервер")
        b2 = types.KeyboardButton("⛔Остановить сервер")
        b3 = types.KeyboardButton("📋Данные сервера")
        b4 = types.KeyboardButton("😏БонУс")
        markup.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "\n==========================\n*СЕРВЕР ЗАПУСТИЛСЯ*\n==========================\nТы живой? Поразительно...", parse_mode="Markdown", reply_markup=markup)
        i = False

    @bot.message_handler(content_types=["text"])
    def event(message):
        if message.text == "🎮Запустить сервер":
            try:
                user = "Vovan_Chebupele"
                pswrd = "qwerty228"
                aternos = Client.from_credentials(user, pswrd)
                srvs = aternos.list_servers()

                global s
                s = srvs[0]

                s.start()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                b2 = types.KeyboardButton("⛔Остановить сервер")
                markup.add(b2)
                bot.send_message(message.chat.id, "\n==========================\n*СЕРВЕР ЗАПУСКАЕТСЯ*\n==========================\nподождите некоторое время...\n_т.е. подождите примерно 1000-7 часов 228 jojo времени в -2 степени в геях по цельсии_", parse_mode="Markdown", reply_markup=markup)
                serv_checker(message)
            except Exception:
                server = BedrockServer.lookup(f"{ip}:{port}")
                status = server.status()
                if status.motd != "Offline":
                    bot.send_message(message.chat.id, f"\n==========================\n*СЕРВЕР УЖЕ ЗАПУЩЕН*\n==========================\nНа нем сейчас {status.players_online} играков", parse_mode="Markdown")
                else:
                    bot.send_message(message.chat.id,
                                     f"\n==========================\n*СЕРВЕР УЖЕ КЕМ-ТО ЗАПУСКАЕТЬСЯ*\n==========================\nКакое совпадение! Какой-то пупс хочет поиграться))\n_Чтобы посмотреть состояние сервера нажмите на_ *📋Данные сервера*",
                                     parse_mode="Markdown")

        if message.text == "📋Данные сервера":
            server = BedrockServer.lookup(f"{ip}:{port}")
            status = server.status()
            on_off = "Offline"
            if status.motd == "Offline":
                on_off = "Offline"
            else:
                on_off = "Online"
            bot.send_message(message.chat.id, f"""==========================
ДАННЫЕ СЕРВЕРА:
==========================
IP: {ip}
Порт: {port}
Версия: {version}
Играков: {status.players_online}
Отклик: {status.latency} мс
Состояние: {on_off}""")
        if message.text == "😏БонУс":
            mes = bot.send_message(message.chat.id, """==========================
*ПОЛУЧИ БОНУС:*
==========================
Здесь ты можешь получить бонус, введя СуперМегаГиперХорошЖесткийСектретный код""", parse_mode="Markdown")
            bot.register_next_step_handler(mes, bonus)
        if message.text == "🔁Перезапустить сервер":
            s.restart()
            bot.send_message(message.chat.id,
                             "\n==========================\n*СЕРВЕР ПЕРЕЗАПУСКАЕТСЯ*\n==========================\nподождите некоторое время...\n_т.е. подождите примерно 1000-7 часов 228 jojo времени в -2 степени в геях по цельсии_",
                             parse_mode="Markdown")
        if message.text == "⛔Остановить сервер":
            stoped = True
            s.stop()
            markup_delete = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id,
                                 "\n==========================\n*СЕРВЕР ОСТАНАВЛИВАЕТЬСЯ*\n==========================\nПодождите совсем немного",
                                 parse_mode="Markdown", reply_markup=markup_delete)
            time.sleep(20)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            b1 = types.KeyboardButton("🎮Запустить сервер")
            b2 = types.KeyboardButton("📋Данные сервера")
            b3 = types.KeyboardButton("😏БонУс")
            markup.add(b1, b2, b3)
            bot.send_message(message.chat.id,
                             "\n==========================\n*СЕРВЕР ОСТАНОВИЛСЯ*\n==========================",
                             parse_mode="Markdown", reply_markup=markup)


    def bonus(message):
        if message.text == "я пуська, хочу алмазы и незерит":
            with open("rickroll.png", "rb") as f:
                mes = bot.send_photo(message.chat.id, f)
                bot.register_next_step_handler(mes, bonus)
        elif message.text == "удачной охоты, сталкер!":
            mes = bot.send_message(message.chat.id, "взаимно Сидорович")
            bot.register_next_step_handler(mes, bonus)
        elif "/op" in message.text:
            mes = bot.send_message(message.chat.id, "/get_message @s 'нахрен пошел, а лучше сядь на него'")
            bot.register_next_step_handler(mes, bonus)
        elif message.text == "😏БонУс":
            event(message)
        elif message.text == "📋Данные сервера":
            event(message)
        elif message.text == "🎮Запустить сервер":
            event(message)
        elif message.text == "⛔Остановить сервер":
            event(message)
        elif message.text == "🔁Перезапустить сервер":
            event(message)
        else:
            mes = bot.send_message(message.chat.id, "не нихрена")
            bot.register_next_step_handler(mes, bonus)

    bot.polling()


if __name__ == "__main__":
    start_bot(token)
