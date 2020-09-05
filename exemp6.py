# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# arg_1 = int(input("insert number 1"));
# arg_2 = int(input("insert number 2"))

def insert_two_number(arg_1, arg_2):
    try:
        result = arg_1/arg_2
    except ValueError:
        print("на ноль делить нельзя")
        return none

    return result
print(insert_two_number(arg_1 = int(input("insert number 1")), arg_2 = int(input("insert number 2"))))