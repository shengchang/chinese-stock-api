
Library to get Chinese stock price

Supported Engines:
 - Hexun API
 - Sina Finance API
 - Yahoo Finance API

Usage:
    
```
from cstock.request import Requests
from cstock.hexun_engine import HexunEngine

engine = HexunEngine()
requester = Requester(engine)

stock = requester.request('000626')
print stock.as_dict()
```

* [Download the latest release](https://github.com/godsarmy/chinese-stock-api/zipball/master).
* Clone the repo: `git clone git://github.com/godsarmy/chinese-stock-api.git`.
* [Download from pypi](https://pypi.python.org/pypi/chinesestockapi).
