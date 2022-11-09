import pytest
from cl import CashCalculator, CaloriesCalculator, Record


@pytest.fixture()
def cash_calculator():
    cash_calc = CashCalculator(1000)
    cash_calc.add_record(Record(amount=200, comment='На вкусняшки'))
    cash_calc.add_record(Record(amount=350, comment='Ередит на китайский айфон'))
    cash_calc.add_record(Record(amount=450, comment='Ередит на китайский айфон'))
    return cash_calc.get_today_cash_remained


@pytest.fixture()
def cal_calculator():
    calories_cal = CaloriesCalculator(1000)
    calories_cal.add_record(Record(amount=450, comment='Вкусняшка номер раз'))
    calories_cal.add_record(Record(amount=250, comment='Вкусняшка номер двас' ))
    calories_cal.add_record(Record(amount=250, comment='Вкусняшка номер трис'))
    return calories_cal


def test_cashCalc(cash_calculator):
    assert cash_calculator('usd') == 'Денег нет, держись'

def test_cashCalc2(cash_calculator):
    assert cash_calculator('rub') == 'Денег нет, держись'

def test_CalCalc(cal_calculator):
    assert cal_calculator.get_calories_remained() == 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 50 кКал'

def test_calCalc2(cal_calculator):
    cal_calculator.add_record(Record(amount=1450, comment='Торт'))
    assert cal_calculator.get_calories_remained() == 'Хватит есть!'
