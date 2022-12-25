#calc
import numexpr
from colorama import init
from colorama import Fore, Back, Style

init()
def convert():

    print(Fore.RED)
    print("Введите математическое выражение:")
    expr = input()

    result = numexpr.evaluate(expr)

    print(Fore.YELLOW)
    print("Результат:")
    print(result)

convert()
while True:
    flag = input("Посчитать еще раз? [Да/Нет]:   ")

    if flag == "Да" or "да":
        convert()
    else:
        break

