# Создайте файл, в котором вы импортируете встроенные в модуль
# функции под псевдонимами. (3-7 строк импорта).

import sys
from random import randint as rd
import math
from datetime import datetime as dt

print(sys.path)

for i in range(2):
    print(rd(1, 10))

print(dt.now())