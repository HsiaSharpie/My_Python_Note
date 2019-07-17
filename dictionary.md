在`Python`內建的資料結構中，`dictionary`是很棒且很有用的容器，它能夠將物件直接對應到其他物件，
被儲存的物件稱作值(value)，作為索引的物件稱為鍵(key)。
```bash
字典對於以鍵查詢值時非常有效率，所以當我們想用某個物件尋找另個物件時，dictionary是很好的選擇！
```
前面有提到，`dictionary`能夠將一個鍵對應到一個值，其中：
1. 鍵是一個`hashable value`。
2. 值是一個任意的物件。

而關於`hashable`，我覺得這篇寫得非常棒，很值得參考參考。
-> https://ithelp.ithome.com.tw/articles/10208884

`dictionary`的建構實在非常的簡單！我們以字典簡單建構一個股票名稱價格查詢表：
```python
stocks = {
  'GOOG': (613.30, 625.86, 610.50),
  'MSFT': (30.25, 30.70, 30.19)
}
```

在`Iterator`那篇中，有提到可對`dictionary`使用 `for` 迴圈去迭代。所以到底有哪些方式可取得初始化後的資料？
1. for loop with items()
2. get method
3. setdefalut method

-> 1.for loop with items()
Example :
```bash
for stock, values in stocks.items():
  print('{} last value is {}'.format(stock, values[0]))

GOOG last value is 613.3
MSFT last value is 30.25
```
