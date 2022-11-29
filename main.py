# -*- coding: utf8 -*-

import telebot
import re

import config as conf
from calc import *
import loging as log

bot = telebot.TeleBot(conf.SOME_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome_handler(message):
    text = 'Привет. Для вычислений операций с числами команда /calc'
    bot.reply_to(message, text)


@bot.message_handler(commands=['calc'])
def get_message(message):
    text = 'Введите ваше выражение для вычисления: '
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, make_calc)


def make_calc(msq):
    expression = msq.text
    string = re.match('[-+*/]', expression)
    values = expression.split(string)
    match string:
        case '-':
            res = make_sub(values[0], values[1])
        case '+':
            res = make_sum(values[0], values[1])
        case '*':
            res = make_mult(values[0], values[1])
        case '/':
            res = make_div(values[0], values[1])
        case _:
            res = ''
    log.write_log(f'{expression} = {res}')
    bot.send_message(msq.chat.id, f'{expression} = {res}')

if __name__=='__main__':
    bot.polling(none_stop=True)


