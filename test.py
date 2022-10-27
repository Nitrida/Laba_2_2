import pytest
from main import CashCalculator, CaloriesCalculator, Record, Calculator

def test_record_creation():

    Record(100, 'comment', '31/03/2021')
    Record(205, 'comment', '21/04/2022')

def cash_calculator():
    cash_calc = CashCalculator(1000)
    cash_calc.add_record(Record(amount=200, comment='На вкусняшки'))
    cash_calc.add_record(Record(amount=350, comment='Ередит на китайский айфон'))
    return cash_calc.get_today_cash_remained()

def cal_calculator():

    calories_calculator = CaloriesCalculator(2000)
    calories_calculator.add_record(Record(amount=1186, comment='Вкусняшка номер раз'))
    calories_calculator.add_record(Record(amount=84, comment='Вкусняшка номер двас', ))
    return calories_calculator.get_calories_remained()

@pytest.mark.parametrize("amount,currency", [
        (0, 'usd'), (0, 'eur'), (0, 'rub'),
        (1, 'usd'), (1, 'eur'), (1, 'rub'),
        (-1, 'usd'), (-1, 'eur'), (-1, 'rub')
])

def test_eval(amount, currency):
    Calculator.limit = Record.today + (amount * 300)


