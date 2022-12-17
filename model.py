first_number = 0
intermediate_result = 0
next_number = 0
calc_example = ''

def summa() -> int:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number + next_number
    first_number = intermediate_result


def difference() -> int:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number - next_number
    first_number = intermediate_result


def multiplication()-> int:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number * next_number
    first_number = intermediate_result


def division()-> int:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number / next_number
    first_number = intermediate_result


def check_operation(sm_operation: str):
    if sm_operation == '+':
        summa()
    elif sm_operation == '-':
        difference()
    elif sm_operation == '*':
        multiplication()
    elif sm_operation == '/':
        division()

def get_intermediate_result():
    global intermediate_result
    return intermediate_result

def set_intermediate_result(smth):
    global intermediate_result
    intermediate_result = smth

def set_next_number(smth):
    global next_number
    next_number = smth

def get_next_number():
    global next_number
    return next_number

def get_first_number():
    global first_number
    return first_number

def set_first_number(smth):
    global first_number
    first_number = smth


def calculate_str(my_list: list) -> int:
    my_list = ''.join(my_list.split())
    my_list = list(my_list)
    for i in range(len(my_list)):
        if my_list[i].isdigit():
            my_list[i] = int(my_list[i])
    while ("*" in my_list) or ("/" in my_list):
        i = 0
        while i < len(my_list):
            if my_list[i] == '*':
                my_list[i - 1] = my_list[i - 1] * my_list[i + 1]
                my_list.remove(my_list[i])
                # print(my_list)
                my_list.remove(my_list[i])
                # print(my_list)
            elif my_list[i] == '/':
                my_list[i - 1] = my_list[i - 1] / my_list[i + 1]
                my_list.remove(my_list[i])
                # print(my_list)
                my_list.remove(my_list[i])
                # print(my_list)
            i += 1
    while ("+" in my_list) or ("-" in my_list):
        i = 0
        while i < len(my_list):
            if my_list[i] == '+':
                my_list[i-1] = my_list[i-1] + my_list[i+1]
                my_list.remove(my_list[i])
                # print(my_list)
                my_list.remove(my_list[i])
                # print(my_list)
            elif my_list[i] == '-':
                my_list[i-1] = my_list[i-1] - my_list[i+1]
                my_list.remove(my_list[i])
                # print(my_list)
                my_list.remove(my_list[i])
                # print(my_list)
            i += 1
    return my_list[0]