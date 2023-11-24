try:
    a=[]
    n=int(input('Введите количество слов :'))
    for i in range(n):
        ne=input()
        a.append(ne)
    b=''
    maxcount=0
    for slovo in a:
        count=0
        for l in slovo:
            if l in "аоиыуэАОИУЫЭ" :
                count+=1
            elif l in 'aeiouyAEIOUY':
                count+=1
        if count>maxcount:
            maxcount=count
            b=slovo
    print('Слово с наибольшим количеством гласных букв : ', b)
except:
    print('Ошибка!Введите число')