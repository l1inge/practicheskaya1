
print("Выберите действие:\n 1)Сложение\n2)Вычитание\n3)Умножение\n4)Деление\n")
action = input()
if (action == "1"):
    count = int(input("Введите нужное кол-во чисел:" ))
    x = 0
    while x < count:
        numb = int(input())
        if x == 0:
            answer = numb +0
        else:
            answer = answer + numb
        x+=1
    print (answer)
if (action == "2"):
    count = int(input("Введите нужное кол-во чисел:" ))
    x = 0
    while x < count:
        numb = int(input())
        if x == 0:
            answer = numb - 0
        else:
            answer = answer-numb
        x+=1
    print (answer)
if (action == "3"):
    count = int(input("Введите нужное кол-во чисел:" ))
    x = 0
    answer = 0
    while x < count:
        numb = int(input())
        if x == 0:
            answer = numb*1
        else:
            answer = answer*numb
        x+=1
    print (answer)
if (action == "4"):
    count = int(input("Введите нужное кол-во чисел:" ))
    x = 0
    while x < count:
        numb = int(input())
        if x == 0:
            answer = numb/1
            x+=1
        else:
            if numb == 0:
                print("На ноль делить нельзя")
                continue
            else:
                answer= answer/numb
                x+=1
    print (answer)