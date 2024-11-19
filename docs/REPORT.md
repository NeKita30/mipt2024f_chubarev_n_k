# Отчет

## Результат
Декодер - класс `BarcodeDecoder` (в модуле [BarcodeDecoder](../BarcodeDecoder)).
Результат его работы - список namedtuple `DecodedBarCode`.

## API
У класса один метод - `decode`, который используется для расшифровки штрих-кодов. 
### Входные значения
Аргументы `decode` - изображение и (опционально) тип штих-кода.

- Изображение - `numpy.array`
- Тип штрих-кода - строка; 
- названия типов взяты из [общей разметки](https://github.com/CD7567/mipt2024f-4-common-knowledge/blob/BarcodeClassificator/BarcodeTypes/README.md). Без указанного типа декодер будет угадывать его сам. 

### Выходное значение
На выходе - список namedtuple `DecodedBarCode`.

`DecodedBarCode` имеет следующие поля:

- `type` - тип штрих-кода (название планируется привести к формату из общей разметки)
- `data` - расшифрованная информация (`bytes`)

## Пример использования

```python
from BarcodeDecoder import BarcodeDecoder

decoder = BarcodeDecoder()
res1 = decoder.decode(img_arr1)
res2 = decoder.decode(img_arr2, "data_matrix")
```

### Запуск примера
В файле [`tests/decoder_test.py`](../tests/decoder_test.py) приведен пример использования 
декодера. Запускать скрипт нужно с `workdir` в корне проекта.

## Дополнительно
Используемые библиотеки: 
- pyzbar: библиотека расшифровки одномерных штрих-кодов и QR-кодов
- pylibdmtx: библиотека расшифровки дата матриц
- pyzxing: библиотека расшифровки широкого диапозона штрих-кодов

Работа библиотеки pyzbar проверенна [отдельно](https://colab.research.google.com/drive/1x_BnHwUhyHBJ7L5jDWW-krYTr8L_1RY-?usp=sharing) (ноутбук с картинками), 
выявленны диапозоны допустимых значений параметров качества входных картинок (поворот, контрастность и др.).
