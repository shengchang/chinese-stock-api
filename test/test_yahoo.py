# coding=utf-8
# system library
import unittest
import datetime

# project library
from cstock.yahoo_engine import YahooEngine


class TestEngine(unittest.TestCase):

    def setUp(self):
        self.engine = YahooEngine()

    def test_get_url(self):
        url = self.engine.get_url('600010', ('2014-03-04', '2014-03-05')) 
        self.assertEqual(url, "http://ichart.yahoo.com/table.csv?s=600010.ss&a=3&b=4&c=2014&d=3&e=5&f=2014")

    def test_parser(self):
        data = ("Date,Open,High,Low,Close,Volume,Adj Close\n" 
                "2014-08-22,34.20,34.22,33.49,33.70,2222200,33.70\n"
                "2014-08-21,33.81,34.29,33.15,34.21,3544800,34.21")

        stocks = self.engine.parse(data, 'foo_id')
        self.assertEqual(len(stocks), 2)
        self.assertEqual(
            stocks[0].as_dict(),
            {'close': '33.70',
             'code': 'foo_id',
             'date': '2014-08-22',
             'high': '34.22',
             'low': '33.49',
             'name': None,
             'open': '34.20',
             'price': None,
             'time': None,
             'turnover': None,
             'volume': '2222200'}
        )
