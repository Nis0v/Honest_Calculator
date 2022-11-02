msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
mojno = False

memory = 0
memory = float(memory)
while True:
    calt = input(f"{msg_0}")
    x, oper, y = calt.split()
    yes_oper = ['-', '+', '/', '*', ':']
###Проверка памяти###
    memory = str(memory)
    if x == 'M':
        x = memory

    if y == 'M':
        y = memory
    
        
###Проверка условий, для адекватного функционирования###
    if x.isalpha() or y.isalpha():
        print(msg_1)
        continue
    x = float(x)
    y = float(y)

    if oper not in yes_oper:
        print(msg_2)
        continue
    #if y == 0:
        #print(msg_3)
        #continue
###СОХРАНЯЙ КОД, В ПРОШЛЫЙ РАЗ ОБНОВИЛ СТРАНИЦУ И НЕ СОХРАНИЛОСЬ###
    def check(v1, v2, v3):
        msg = ""
        
        def is_one_digital(v):
            if (v > -10 and v < 10 and v.is_integer()) == True:
                return True
            else:
                return False
        
        if (is_one_digital(v1) and is_one_digital(v2)) == True:
            msg = msg + msg_6
        if (v1 == 1 or v2 == 1) and v3 == "*":
            msg = msg + msg_7
        if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
            msg = msg + msg_8
        if msg != "":
            msg = msg_9 + msg
            print(msg)
    check(x, y, oper)





        
###Решение уравнений, исходя их оператора###

    if oper == '-':
        result = x-y
        print(result)

    if oper == '+':
        result = x+y
        print(result)

        
    if oper == '/' or oper == ':':
        if y != 0:
            result = x/y
            print(result)
        if y == 0:
            print(msg_3)
            continue

        
    if oper == '*':
        result = x*y
        print(result)
        
###Финальный опрос###
    otvet1 = input(msg_4)
    if otvet1 == 'y':
        ###Memory ###
        def is_one_digit():
            global mojno 
            activ = True
            msg_index = 10
            if result % 1 == 0 and result < 10 :
                while activ == True : 
                    if msg_index == 10:
                        print(msg_10)
                    if msg_index == 11:
                        print(msg_11)
                    if msg_index == 12:
                        print(msg_12)
                    answer = input()
                    if answer == "y":
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        else:
                            mojno = False
                            break
                    else:
                        mojno = True
                        return
                        break
            return
        is_one_digit()

        if mojno != True:
            memory = result
    otvet2 = input(msg_5)
    if otvet2 == 'y':
            continue
    else: break