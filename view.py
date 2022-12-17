import controller
def input_number():
    number = int(input('введите число:  '))
    return number

def input_operation():
    operation = input('введите операцию(+, -, *, /, =) :  ')
    return operation

def print_result(smth):
    print(smth)

def input_string():
    calc_example = input('Введите варажение:  ')
    calc_example = calc_example.replace(' ', '')
    if '=' in calc_example:
        calc_example = calc_example[:calc_example.find('=')]
    return calc_example

def selection():
    a = input('Выберите  калькулятор: \n 1. Строчный \n 2. Консольный \n')
    while a not in ['0', '1']:
        a = input('Ввод не коректен: \n 1. Строчный \n 2. Консольный \n')
    return int(a)
