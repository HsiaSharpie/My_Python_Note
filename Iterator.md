平常在寫程式的時候，經常都會使用到 `for` 迴圈去完成一系列的事情。
1. 經常先使用 `list` `tuple` `dictionary` 等型態去保存資料。
2. 再使用 `for` 迴圈去迭代，取出裡面的 value 以完成一些事。

Example :
```python
names = ['Jay Park', 'Simon Dominic', 'Loco']
for name in names:
  print(name)
```
在上面的例子中，使用了 `for... in...`去迭代 `list` ，並把 `list`  裡的 value 取出後印出來。
這些可以被 `for... in...` 進行迭代的物件，即為「可迭代物件」。
因此，可以猜到上面提到的`list` `tuple` `dictionary` 也一定是「可迭代物件」。
(根本廢話..........)

而「可迭代物件」其實被定義如下：
```bash
具有 __iter__() 與 __getitem__() 方法的物件，為可迭代物件。
```
我們來使用內建的 `hasattr()` 驗證一下：
```bash
hasattr(object, name)
1. object：被檢查的物件。
2. name：是否具有之屬性。
```
```bash
>>> hasattr([], '__iter__')
True
>>> hasattr([], '__getitem__')
True
```
由上面結果，`list`即為「可迭代物件」。
`tuple` `dictionary` `string` 等等皆可用相同方式去驗證為可迭代物件，就由大家自行去驗證了XD


終於理解了什麼是可迭代物件，終於可以來講迭代器( Iterator ) 了！
`Python` 的迭代其實是有協定的，也就是「迭代器」即為滿足迭代器協定( `Iterator Protocol` ) 之物件。
定義如下：
```bash
迭代器為遵守 Iterator Protocol 的物件。
```
Iterator Protocol:
```bash
物件要能夠實行 __iter__() 與 __next__() 方法。
```
現在你應該等不及想要查看前面提到的`list` `tuple` `dictionary`等等到底是不是迭代器了吧 XD，那就同樣地使用`hasattr()` 來驗證吧：
```bash
>>> hasattr([], '__iter__')
True
>>> hasattr([], '__next__')
False
```
由上面的例子，可以很清楚的知道 `list` 本身並沒有 `__next__` 屬性。
同樣地，你可以去檢驗其他資料型態：

> 陣列、元組、字典等等雖然都是可迭代對象，但他們都不是迭代器。

對於這些迭代器物件，我們可使用 `Python` 內建的 `iter()` 函數來對迭代器物件進行作用：
```python
names = ['Jay Park', 'Simon Dominic', 'Loco']
>>> from collections import Iterator
>>> isinstance(iter(names), Iterator)
True
>>> isinstance(next(names), Iterator)
TypeError: 'list' object is not an iterator

>>> iter_names = iter(names)
>>> isinstance(iter_names, Iterator)
True
>>> next(iter_names)
'Jay Park'
```
事實上，我們平常在使用 `for` 迴圈去進行迭代時，即為先透過 `iter()` 去取得迭代器`(Iterator)` ，然後再依序使用 `next()` 函數。

在上面的例子：  
1. 透過 `iter()` 取得 Iterator。
2. 使用 `next()` 取得 Iterator 中的第一個元素。
3. 再下一次使用 `next()` 時，取得第二個元素：`Simon Dominic`

好！現在我們充分了解什麼是 `可迭代物件` 、`迭代器` 後，回到最一開始的例子：
```python
names = ['Jay Park', 'Simon Dominic', 'Loco']
for name in names:
  print(name)
```
如果我們把它拆解成一個 `function` 該怎麼轉換？
```python
names = ['Jay Park', 'Simon Dominic', 'Loco']
iter_names = iter(names)
while True:
  try:
    name = next(iter_names)
    print(name)
  except StopIteration:
    break
```
```bash
Note:
迴圈的每一個步驟，它都會對該物件去呼叫 next()，它會委託給 __next__()方法，
每次回傳一個，直到沒有元素則會出現StopIteration Exception 提醒 Python。
```

優點：
除了內建的可迭代物件， for 迴圈也可用來處理其他物件，
這些物件當然可以是我們自己定義的，用我們邏輯去設計一套屬於自己的迴圈，
這樣是不是更方便了呢？
