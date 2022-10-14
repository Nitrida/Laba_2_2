import pytest
import re
from datetime import datetime

try:
    import main
except ModuleNotFoundError:
    assert False, 'Нет файла'


class TestRecord:
    init_records = [{'amount': 1000, 'comment': 'Тестовый коммент'},
                    {'amount': 1000, 'comment': 'Тестовый коммент', 'date': '01/09/2019'}]

    @pytest.mark.parametrize("kwargs", init_records)
    def test_init(self, kwargs, msg_err):
        assert hasattr(main, 'Record'), msg_err('add_class', 'Record')
        result = main.Record(**kwargs)
        assert hasattr(result, 'amount'), msg_err('add_attr', 'amount', 'Record')
        assert result.amount == kwargs['amount'],  msg_err('wrong_attr', 'amount', 'Record')
        assert hasattr(result, 'comment'), msg_err('add_attr', 'comment', 'Record')
        assert result.comment == kwargs.get('comment', ''),  msg_err('wrong_attr', 'comment', 'Record')
        assert hasattr(result, 'date'), msg_err('add_attr', 'date', 'Record')
        if 'date' in kwargs:
            assert result.date == datetime.strptime(kwargs['date'], '%d/%m/%Y').date(), \
                msg_err('wrong_attr', 'date', 'Record', ', свойство должно быть датой')
        else:
            assert result.date == datetime.now().date(), \
                msg_err('wrong_attr', 'date', 'Record', ', свойство должно быть датой')

        assert not hasattr(result, 'USD_RATE'), msg_err('dont_create_attr', 'USD_RATE', 'Record')
        assert not hasattr(result, 'EURO_RATE'), msg_err('dont_create_attr', 'EURO_RATE', 'Record')


class TestCaloriesCalculator:

    def test_init(self, init_limit, msg_err):
        assert hasattr(main, 'CaloriesCalculator'), \
            msg_err('add_class', 'CaloriesCalculator', child=True, parent_name='Calculator')
        result = main.CaloriesCalculator(init_limit)
        assert hasattr(result, 'limit'), msg_err('child_method', 'CaloriesCalculator', 'Calculator')
        assert result.limit == init_limit, msg_err('child_method', 'CaloriesCalculator', 'Calculator')

        assert not hasattr(result, 'USD_RATE'), msg_err('dont_create_attr', 'USD_RATE', 'CaloriesCalculator')
        assert not hasattr(result, 'EURO_RATE'), msg_err('dont_create_attr', 'EURO_RATE', 'CaloriesCalculator')


class TestCashCalculator:

    def test_init(self, init_limit, msg_err):
        assert hasattr(main, 'CashCalculator'), \
            msg_err('add_class', 'CashCalculator', child=True, parent_name='Calculator')
        result = main.CashCalculator(init_limit)
        assert hasattr(result, 'limit'), msg_err('child_method', 'CashCalculator', 'Calculator')
        assert result.limit == init_limit, msg_err('child_method', 'CashCalculator', 'Calculator')

        assert hasattr(result, 'EURO_RATE'), msg_err('add_attr', 'EURO_RATE', 'CashCalculator')
        assert type(result.EURO_RATE) == float, msg_err('wrong_attr', 'EURO_RATE', 'CashCalculator')
        assert result.EURO_RATE > 0, msg_err('wrong_attr', 'EURO_RATE', 'CashCalculator',
                                             msg=', курс не может быть равен или меньше 0')

        assert hasattr(result, 'USD_RATE'), msg_err('add_attr', 'USD_RATE', 'CashCalculator')
        assert type(result.USD_RATE) == float, msg_err('wrong_attr', 'USD_RATE', 'CashCalculator')
        assert result.USD_RATE > 0, msg_err('wrong_attr', 'USD_RATE', 'CashCalculator',
                                            msg=', курс не может быть равен или меньше 0')

    @pytest.mark.parametrize("amount,currency", [
        (0, 'usd'), (0, 'eur'), (0, 'rub'),
        (1, 'usd'), (1, 'eur'), (1, 'rub'),
        (-1, 'usd'), (-1, 'eur'), (-1, 'rub')
    ])
    def test_get_today_cash_remained(self, init_limit, data_records, amount, currency, today_cash_remained, msg_err,
                                     monkeypatch):

        result = main.CashCalculator(init_limit)
        assert hasattr(result, 'get_today_cash_remained'), \
            msg_err('add_method', 'get_today_cash_remained', 'CashCalculator')

        records, today, week = data_records
        for record in records:
            result.add_record(record)

        result.EURO_RATE = 70
        monkeypatch.setattr(main.CashCalculator, "EURO_RATE", 70)
        result.USD_RATE = 60
        monkeypatch.setattr(main.CashCalculator, "USD_RATE", 60)
        result.limit = today + (amount * 300)
        assert re.fullmatch(today_cash_remained(amount, currency), result.get_today_cash_remained(currency)), \
            msg_err('wrong_method', 'get_today_cash_remained', 'CashCalculator')