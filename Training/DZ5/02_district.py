# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as csh1r1
from district.central_street.house1 import room2 as csh1r2
from district.central_street.house2 import room2 as csh2r2
from district.soviet_street.house1 import room1 as ssh1r1
from district.soviet_street.house1 import room2 as ssh1r2
from district.soviet_street.house2 import room1 as ssh2r1
from district.soviet_street.house2 import room2 as ssh2r2

print('На районе живут', ', '.join(csh1r1.folks), ', '.join(csh1r2.folks), ', '.join(csh2r2.folks),
      ', '.join(ssh1r1.folks), ', '.join(ssh1r2.folks), ', '.join(ssh2r1.folks), ', '.join(ssh2r2.folks))
