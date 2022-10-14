import datetime as dt
from decimal import Decimal


date_format ='%d/%m/%Y'


class Calculator:
    def __init__(self, limit: Decimal):
        self.limit = limit
        self.records = []

    def add_record(self, next_record: 'Record '):
        self.records.append(next_record)

    def get_today_stats(self):
        d_today = dt.date.today()
        return sum([record.amount
                    for record in self.records
                    if record.date == d_today])

    def get_week_stats(self):
        d_today = dt.date.today()
        date_week_ago=d_today - dt.timedelta(days=7)
        return float(sum([record.amount
                          for record in self.records
                          if date_week_ago < record.date <= d_today]))

    def get_today_remained(self):
        spent_today = self.get_today_stats()
        return self.limit - spent_today


class CashCalculator(Calculator):
    USD_RATE = 61
    EURO_RATE = 58
    RUB_RATE = 1.0

    class CaloriesCalculator(Calculator):
        def get_calories_remained(self):
            spent_today = round(self.get_today_remained())
            if spent_today > 0:
                return (f'Сегодня можно съесть что-нибудь ещё, '
                        f'но с общей калорийностью не более {spent_today} кКал')
            else:
                return 'Хватит есть'

    def get_today_cash_remained(self, currency: str):
        all_currency ={
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE),
            'rub': ('руб', self.RUB_RATE),
        }

        if currency not in all_currency:
            raise ValueError('Валюта введена некорректно')
        currency_name, currency_course = all_currency[currency]
        spent_today = self.get_today_remained()
        if spent_today ==0:
            return 'Денег нет, держись'

        today_spent_currency = round(abs(spent_today / currency_course), 2)
        if spent_today > 0:
            return (f'На сегодня осталось{today_spent_currency} '
                    f'{currency_name}')
        else:
            return (f'Денег нет, держись: твой долг - '
                    f'{today_spent_currency} {currency_name}')


class Record:
    def __init__(self, amount: Decimal, comment: str, date: str = None):
        self.amount = float(amount)
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, date_format).date()
        else:
            self.date = dt.date.today()

class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        # Сколько можно еще съесть
        spent_today = round(self.get_today_remained())
        if spent_today > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {spent_today} кКал')
        else:
            return 'Хватит есть!'
#проверка результатов

cal = input('Введите сумму: ')
cal = float(cal)
am = input('Введите денежную сумму/количество калорий')
am = float(am)
com = input('Введите коментарий к записи: ')

calories_calculator = CaloriesCalculator(cal)
calories_calculator.add_record(Record(amount=am, comment=com))
am = input('Введите денежную сумму/количество калорий')
am = float(am)
com = input("Введите коментарий к записи: ")

calories_calculator.add_record(Record(amount=am, comment=com))
am = input('Введите денежную сумму/количество калорий')
am = float(am)
com = input('Введите коментарий к записи: ')

date_str = input('Введите дату выпуска (dd/mm/yyyy)')

#dat = dt.datetime.strptime(date_str, '%d/%m/%Y').date()

calories_calculator.add_record(Record(amount=am,
                                      comment=com,
                                      date=date_str))
print(calories_calculator.get_calories_remained())

money = input('Введите сумму: ')
money = float(money)
am = input('Введите денежную сумму/количество калорий')
am = float(am)
com = input('Введите коментарий к записи: ')

cash_calculator = CashCalculator(money)
cash_calculator.add_record(Record (amount = am, comment = com))
am = input('Введите денежную сумму/количество калорий')
am = float(am)
com = input("Введите коментарий к записи: ")

cash_calculator.add_record(Record(amount=am, comment=com))
am = input('Введите денежную сумму/количество калорий')
am = float(am)
com = input('Введите коментарий к записи: ')

date_str = input('Введите дату выпуска (dd/mm/yyyy)')

#dat = dt.datetime.strptime(date_str, '%d/%m/%Y').date()

cash_calculator.add_record(Record(amount=am,
                                  comment=com,
                                  date=date_str))
print(cash_calculator.get_today_cash_remained('rub'))
