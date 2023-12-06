color={'red': "красный" , 'blue': 'голубой' ,'yellow': 'желтый' , 'white': 'белый', 'black': 'черный', 'green': 'зеленый', 'brown': 'коричневый', 'pink': 'розовый' , 'orange': 'оранжевый', 'purple': 'фиолетовый'}
for key, value in color.items():
   print(key,'-', value)
newcolor=list(color.values())[-1]
print('Перевод последнего слова -' , newcolor)