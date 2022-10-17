from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '5663125010:AAEj514xqnGYJTxkcLShRCaORSBHe-kxy_4'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


class Solver8:
    def dvoichnay_to_decyat(self, data):
        number = 0
        len_dat = len(data)
        for i in range(0, len_dat):
            number += int(data[i]) * (2**(len_dat - i -1))
        return number

    def decyat_to_dvoichnay(self, n):
        b = ''
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        return b

    def vyrashenie(self, s):
        if '+' in s:
            s = s.replace(' ', '').split('+')
            sp = [self.dvoichnay_to_decyat(str(s[0])), self.dvoichnay_to_decyat(str(s[1]))]
            return self.decyat_to_dvoichnay(sum(sp))
        elif '-' in s:
            s = s.replace(' ', '').split('-')
            sp = [self.dvoichnay_to_decyat(str(s[0])), self.dvoichnay_to_decyat(str(s[1]))]
            return self.decyat_to_dvoichnay(sp[0] - sp[1])
        elif '*' in s:
            s = s.replace(' ', '').split('*')
            sp = [self.dvoichnay_to_decyat(str(s[0])), self.dvoichnay_to_decyat(str(s[1]))]
            return self.decyat_to_dvoichnay(sp[0] * sp[1])
        elif '/' in s:
            s = s.replace(' ', '').split('/')
            sp = [self.dvoichnay_to_decyat(str(s[0])), self.dvoichnay_to_decyat(str(s[1]))]
            return self.decyat_to_dvoichnay(sp[0] / sp[1])


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


def get_answer(n, m):
    formula = fac(m) / (fac(m - n) * fac(n))
    return formula


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Приветик 👋\nДанный бот поможет тебе с ср по информатике, нажмми на команду и узнаешь как ей пользоваться\n/infa_ege_8\n/math_help_sochetanya')


@dp.message_handler(commands=['infa_ege_8'])
async def process_start_command(message: types.Message):
    print(message.text)
    try:
        s = message.text.replace('/infa_ege_8 ', '')
        await message.reply(Solver8().vyrashenie(s))
    except:
        await message.reply('😡 Ты либо неправильно написал, либо не знаешь че эта функция делает.Она решает примеры вида:\n\n/infa_ege_8 101111*1111\n/infa_ege_8 1110101111 - 10000010\n/infa_ege_8 101111 + 11101')


@dp.message_handler(commands=['math_help_sochetanya'])
async def process_start_command(message: types.Message):
    try:
        s = message.text.replace('/math_help_sochetanya ', '').split()
        list_answers = {}
        for el in s:
            el1, el2 = map(int, el.split(','))
            try:
                list_answers[f'{el1}, {el2}'] = get_answer(el1, el2)
            except RecursionError:
                await message.reply(f'Sorry! Review your numbers - {el1, el2}')

        for el in list_answers:
            await message.reply(f'{el}  =  {list_answers[el]}')
    except:
        await message.reply('😡 Ты либо неправильно написал, либо не знаешь че эта функция делает.Она решает сочетания, типа:\n\n/math_help_sochetanya 2,7 1,5 4,9\n/math_help_sochetanya 1,5')


if __name__ == '__main__':
    executor.start_polling(dp)
