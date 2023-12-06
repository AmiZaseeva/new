while True:
    try:
        import random
        n=int(input("Введите количество элементов в:"))
        if n > 0:
            m=int(input("Введите количество строк :"))
            if m > 0:
                a = [[random.randint(0,10) for j in range(n)] for i in range(m)]
                b=[]
                for l in a:
                    count=0
                    for k in l:
                        count+=k
                    b.append(count)
                print("Исходная строка ",a)
                print("Новый список" ,b)
                break
            else:
                print('Ошибка!!!Введите положительно число')
        else:
            print('Ошибка!!!Введите положительно число')
    except ValueError:
        print('Ошибка!!! Введите число')