import pytest
import main
from main import CashCalculator, CaloriesCalculator, Record

def test_record_creation():
    # test_record = Record(100, 'comment', '31/03/2021')
    # test_record = Record(205, 'comment', '21/04/2022')
    if len(main.com) == 0:
        print('[Нехватает коментариев]')


def test_cash_calculator():
    cash_calc = CashCalculator(1000)
    cash_calc.add_record(Record(amount=200, comment='На вкусняшки'))
    cash_calc.add_record(Record(amount=350, comment='Ередит на китайский айфон'))
    cash_calc.add_record(Record(amount=450, comment='Ередит на китайский айфон'))
    # return cash_calc.get_today_cash_remained()
    assert cash_calc == 'Денег нет, держись'


def test_cal_calculator():
    calories_cal = CaloriesCalculator(1000)
    calories_cal.add_record(Record(amount=450, comment='Вкусняшка номер раз'))
    calories_cal.add_record(Record(amount=250, comment='Вкусняшка номер двас' ))
    calories_cal.add_record(Record(amount=250, comment='Вкусняшка номер трис'))
    assert calories_cal == 'Хватит есть'

