import pytest
from main import CashCalculator, CaloriesCalculator, Record, Calculator

def test_record_creation():
    com="sdfds"
    Record(100, 'comment', '31/03/2021')
    Record(205, 'comment', '21/04/2022')
    if len(Record.comment)==0:
        assert com == '[Нехватает коментариев]'


def test_cash_calculator():
    cash_calc = CashCalculator(1000)
    # cash_calc.add_record(Record(amount=200, comment='На вкусняшки'))
    # cash_calc.add_record(Record(amount=350, comment='Ередит на китайский айфон'))
    # return cash_calc.get_today_cash_remained()
    if Record.amount>0 and len(Record.comment)>0 :
        assert cash_calc == '[Еще осталось на покушать]'
    if len(Record.comment)==0:
        assert cash_calc == '[Забыли коментарий]'
    if CashCalculator.spent_today <= 0:
        assert cash_calc == '[Денег нет]'


def test_cal_calculator():
    calories_cal = CaloriesCalculator(2000)
    # calories_cal.add_record(Record(amount=1186, comment='Вкусняшка номер раз'))
    # calories_cal.add_record(Record(amount=84, comment='Вкусняшка номер двас', ))
    if Record.amount>0 and len(Record.comment)>0 :
        assert calories_cal == '[Можно сьесть еще чуть чуть]'
    if len(Record.comment)==0:
        assert calories_cal == '[Забыли коментарий]'
    if CaloriesCalculator.spent_today <= 0:
        assert calories_cal == '[Хватит есть]'

# def test_cashCalc(cash_calc):
#     assert cash_calculator == 'Ваш остаток 730.0 Rub'

# def test_CalCalc(calories_cal):
#     assert calories_cal == '[Хватит есть]'






