while True:
    try:
        import random
        n=int(input('Введите количество элементов :'))
        if n > 0 :
            m = int(input('Введите количество строк :'))
            if m > 0:
                a = [[random.randint(-100000,100000) for j in range(n)] for i in range(m)]
                mmm=0
                b = []
                bb=[]
                for l in a:
                    count = 0
                    for num in l:
                        count+=num
                    b.append(count)
                    for sumel in b:
                        if sumel>mmm:
                            mmm=sumel
                            bb=l
                print("Исходная строка ", a)
                print('Строка с наибольше суммой ', bb)
                print('Наибольшая сумма - ', mmm , ', в строке ' , bb)
                break
            else:
                print('Ошибка!!!Введите положительно число')
        else:
            print('Ошибка!!!Введите положительно число')
    except ValueError:
        print('Ошибка!!! Введите число')