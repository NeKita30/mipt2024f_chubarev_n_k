# Отчет

## Результат
Декодер - класс `BarcodeDecoder` (в модуле [BarcodeDecoder](../BarcodeDecoder)).

## API
У класса один метод - `decode`, который используется для расшифровки штрих-кодов. 
### Входные значения
Аргументы `decode` - изображение и (опционально) тип штих-кода.

- Изображение - `numpy.array`
- Тип штрих-кода - строка; 
- названия типов взяты из [общей разметки](https://github.com/CD7567/mipt2024f-4-common-knowledge/blob/BarcodeClassificator/BarcodeTypes/README.md). Без указанного типа декодер будет угадывать его сам. 

### Выходное значение


## Пример использования

```python
from BarcodeDecoder import BarcodeDecoder

decoder = BarcodeDecoder()
res1 = decoder.decode(img1)
res2 = decoder.decode(img2, "data_matrix")
```