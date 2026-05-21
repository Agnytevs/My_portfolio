from colorama import init, Fore, Back, Style
import math
import string
import time

def slow_print(text): 
    for char in text: 
        for i in char:
            print(char, end='', flush=True)
            time.sleep(0.03) 
    print()
slow_print(Fore.RED + "Введи два числа чтобы начать")
a = float(input(Fore.MAGENTA + "a = "))   
b = float(input("b = "))
print(Fore.CYAN)
c = input("Выбери операцию [+/-/*/**/>а/>б/:/::/:%]: ")
if c == "+":
    print(a + b); slow_print("выше сложение")
if c == "-":
    print(a - b); slow_print("выше вычитание")
if c == "*":
    print(a * b); slow_print("выше умножение")
if c == "**":
    print(a ** b); slow_print("выше степень")
if c == ">а":
    print(math.sqrt(a)); slow_print("выше корень числа a")
if c == ">б":
    print(math.sqrt(b)); slow_print("выше корень числа b")
if b == 0:
    slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
else:
    if c == ":":
        print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
    if c == "::":
        print(a // b); slow_print("выше целое от деления")
    if c == ":%":
        print(a % b); slow_print("выше остаток от деления")
while True:
    c = input(Fore.RED + Back.BLACK + "хочешь продолжить? [да/нет]: ")
    if c == "да":
        print(Fore.GREEN)
        c = input("начнем заново? [да/нет]: ")
        if c == "нет":
            print(Fore.MAGENTA)
            c = input("тогда что выберем?(выбирай, ту операцию которую недавно выполнил. иначе выйдет другой ответ) [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
            if c == "сложение":
                print(Fore.MAGENTA)
                a = a + b
                print("a =", a)
                b = float(input("b = "))
                print(Fore.CYAN)
                c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
                if c == "сложение":
                    print(a + b); slow_print("выше сложение")
                if c == "вычитание":
                    print(a - b); slow_print("выше вычитание")
                if c == "умножение":
                    print(a * b); slow_print("выше умножение")
                if c == "степень":
                    print(a ** b); slow_print("выше степень")
                if c == "корень числа а":
                    print(math.sqrt(a)); slow_print("выше корень числа a")
                if c == "корень числа б":
                    print(math.sqrt(b)); slow_print("выше корень числа b")
                if b == 0:
                    slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
                else:
                    if c == "деление":
                        print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
                    if c == "целое от деления":
                        print(a // b); slow_print("выше целое от деления")
                    if c == "остаток от деления":
                        print(a % b); slow_print("выше остаток от деления")
            if c == "вычитание":
                print(Fore.MAGENTA)
                a = a - b
                print("a =", a)
                b = float(input("b = "))
                print(Fore.CYAN)
                c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
                if c == "сложение":
                    print(a + b); slow_print("выше сложение")
                if c == "вычитание":
                    print(a - b); slow_print("выше вычитание")
                if c == "умножение":
                    print(a * b); slow_print("выше умножение")
                if c == "степень":
                    print(a ** b); slow_print("выше степень")
                if c == "корень числа а":
                    print(math.sqrt(a)); slow_print("выше корень числа a")
                if c == "корень числа б":
                    print(math.sqrt(b)); slow_print("выше корень числа b")
                if b == 0:
                    slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
                else:
                    if c == "деление":
                        print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
                    if c == "целое от деления":
                        print(a // b); slow_print("выше целое от деления")
                    if c == "остаток от деления":
                        print(a % b); slow_print("выше остаток от деления")
            if c == "умножение":
                print(Fore.MAGENTA)
                a = a * b
                print("a =", a)
                b = float(input("b = "))
                print(Fore.CYAN)
                c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
                if c == "сложение":
                    print(a + b); slow_print("выше сложение")
                if c == "вычитание":
                    print(a - b); slow_print("выше вычитание")
                if c == "умножение":
                    print(a * b); slow_print("выше умножение")
                if c == "степень":
                    print(a ** b); slow_print("выше степень")
                if c == "корень числа а":
                    print(math.sqrt(a)); slow_print("выше корень числа a")
                if c == "корень числа б":
                    print(math.sqrt(b)); slow_print("выше корень числа b")
                if b == 0:
                    slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
                if c == "деления":
                    print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
                if c == "целое от деления":
                    print(a // b); slow_print("выше целое от деления")
                if c == "остаток от деления":
                    print(a % b); slow_print("выше остаток от деления")
            if c == "степень":
                print(Fore.MAGENTA)
                a = a ** b
                print("a =", a)
                b = float(input("b = "))
                print(Fore.CYAN)
                c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
                if c == "сложение":
                    print(a + b); slow_print("выше сложение")
                if c == "вычитание":
                    print(a - b); slow_print("выше вычитание")
                if c == "умножение":
                    print(a * b); slow_print("выше умножение")
                if c == "степень":
                    print(a ** b); slow_print("выше степень")
                if c == "корень числа а":
                    print(math.sqrt(a)); slow_print("выше корень числа a")
                if c == "корень числа б":
                    print(math.sqrt(b)); slow_print("выше корень числа b")
                if b == 0:
                    slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
                else:
                    if c == "деление":
                        print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
                    if c == "целое от деления":
                        print(a // b); slow_print("выше целое от деления")
                    if c == "остаток от деления":
                        print(a % b); slow_print("выше остаток от деления")
            if c == "корень числа а":
                print(Fore.MAGENTA)
                a = math.sqrt(a)
                print("a =", a)
                b = float(input("b = "))
                print(Fore.CYAN)
                c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
                if c == "сложение":
                    print(a + b); slow_print("выше сложение")
                if c == "вычитание":
                    print(a - b); slow_print("выше вычитание")
                if c == "умножение":
                    print(a * b); slow_print("выше умножение")
                if c == "степень":
                    print(a ** b); slow_print("выше степень")
                if c == "корень числа а":
                    print(math.sqrt(a)); slow_print("выше корень числа a")
                if c == "корень числа б":
                    print(math.sqrt(b)); slow_print("выше корень числа b")
                if b == 0:
                    slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
                else:
                    if c == "деление":
                        print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
                    if c == "целое от деления":
                        print(a // b); slow_print("выше целое от деления")
                    if c == "остаток от деления":
                        print(a % b); slow_print("выше остаток от деления")
            if c == "корень числа б":
                print(Fore.MAGENTA)
                a = math.sqrt(b)
                print("a =", a)
                b = float(input("b = "))
                print(Fore.CYAN)
                c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
                if c == "сложение":
                    print(a + b); slow_print("выше сложение")
                if c == "вычитание":
                   print(a - b); slow_print("выше вычитание")
                if c == "умножение":
                    print(a * b); slow_print("выше умножение")
                if c == "степень":
                    print(a ** b); slow_print("выше степень")
                if c == "корень числа а":
                    print(math.sqrt(a)); slow_print("выше корень числа a")
                if c == "корень числа б":
                    print(math.sqrt(b)); slow_print("выше корень числа b")
                if b == 0:
                    slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
                else:
                    if c == "деление":
                        print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
                    if c == "целое от деления":
                        print(a // b); slow_print("выше целое от деления")
                    if c == "остаток от деления":
                        print(a % b); slow_print("выше остаток от деления")
            if c == "деление":
                if b == 0:
                    print(Fore.RED + Back.YELLOW + "воспроизвести невозможно")
                    print(Back.BLACK)
                else:
                    print(Fore.MAGENTA)
                    a = a / b
                    print("a =", a)
                    b = float(input("b = "))
                    print(Fore.CYAN)
                    c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
                    if c == "сложение":
                        print(a + b); slow_print("выше сложение")
                    if c == "вычитание":
                        print(a - b); slow_print("выше вычитание")
                    if c == "умножение":
                        print(a * b); slow_print("выше умножение")
                    if c == "степень":
                        print(a ** b); slow_print("выше степень")
                    if c == "корень числа а":
                        print(math.sqrt(a)); slow_print("выше корень числа a")
                    if c == "корень числа б":
                        print(math.sqrt(b)); slow_print("выше корень числа b")
                    if b == 0:
                        slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
                    else:
                        if c == "деление":
                            print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
                        if c == "целое от деления":
                            print(a // b); slow_print("выше целое от деления")
                        if c == "остаток от деления":
                            print(a % b); slow_print("выше остаток от деления")
            if c == "целое от деления":
                if b == 0:
                    print(Fore.RED + Back.YELLOW + "воспроизвести невозможно")
                    print(Back.BLACK)
                else:
                    print(Fore.MAGENTA)
                    a = a // b
                    print("a =", a)
                    b = float(input("b = "))
                    print(Fore.CYAN)
                    c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
                    if c == "сложение":
                        print(a + b); slow_print("выше сложение")
                    if c == "вычитание":
                        print(a - b); slow_print("выше вычитание")
                    if c == "умножение":
                        print(a * b); slow_print("выше умножение")
                    if c == "степень":
                        print(a ** b); slow_print("выше степень")
                    if c == "корень числа а":
                        print(math.sqrt(a)); slow_print("выше корень числа a")
                    if c == "корень числа б":
                        print(math.sqrt(b)); slow_print("выше корень числа b")
                    if b == 0:
                        slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
                    else:
                        if c == "деление":
                            print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
                        if c == "целое от деления":
                            print(a // b); slow_print("выше целое от деления")
                        if c == "остаток от деления":
                            print(a % b); slow_print("выше остаток от деления")
            if c == "остаток от деления":
                if b == 0:
                    print(Fore.RED + Back.YELLOW + "воспроизвести невозможно")
                    print(Back.BLACK)
                else:
                    print(Fore.MAGENTA)
                    a = a % b
                    print("a =", a)
                    b = float(input("b = "))
                    print(Fore.CYAN)
                    c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
                    if c == "сложение":
                        print(a + b); slow_print("выше сложение")
                    if c == "вычитание":
                        print(a - b); slow_print("выше вычитание")
                    if c == "умножение":
                        print(a * b); slow_print("выше умножение")
                    if c == "степень":
                        print(a ** b); slow_print("выше степень")
                    if c == "корень числа а":
                        print(math.sqrt(a)); slow_print("выше корень числа a")
                    if c == "корень числа б":
                        print(math.sqrt(b)); slow_print("выше корень числа b")
                    if b == 0:
                        slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
                    else:
                        if c == "деление":
                            print(a / b); slow_print(Fore.CYAN + Back.BLACK + "выше деление")
                        if c == "целое от деления":
                            print(a // b); slow_print("выше целое от деления")
                        if c == "остаток от деления":
                            print(a % b); slow_print("выше остаток от деления")
        else:
            a = float(input(Fore.MAGENTA + "a = "))
            b = float(input("b = "))
            print(Fore.CYAN)
            c = input("Выбери операцию [сложение/вычитание/умножение/степень/корень числа а/корень числа б/деление/целое от деления/остаток от деления]: ")
            if c == "сложение":
                print(a + b); slow_print("выше сложение")
            if c == "вычитание":
                print(a - b); slow_print("выше вычитание")
            if c == "умножение":
                print(a * b); slow_print("выше умножение")
            if c == "степень":
                print(a ** b); slow_print("выше степень")
            if c == "корень числа а":
                print(math.sqrt(a)); slow_print("выше корень числа a")
            if c == "корень числа б":
                print(math.sqrt(b)); slow_print("выше корень числа b")
            if b == 0:
                slow_print(Fore.RED + Back.YELLOW + "На ноль делить нельзя!!!")
            else:
                if c == "деление":
                    print(a / b); slow_print("выше деление")
                if c == "целое от деления":
                    print(a // b); slow_print("выше целое от деления")
                if c == "остаток от деления":
                    print(a % b); slow_print("выше остаток от деления")
    else:
        slow_print("хорошего дня!!!")
        break        