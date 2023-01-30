print ("Добрый день, вас приветствует программа подсчета дней в году")
selectyear = int(input ("Выберите нужный вам год: "))

if(selectyear > 0):

    def SumValueMonth(onemonthcount):
        i = 1
        onemonthcount += 1
        value = 0
        for i in range(onemonthcount):
            if (onemonthcount < 10):
                value += i
            else: value += (i // 10) + (i % 10)
        return value

    january = 31
    march = 31
    april = 30
    may = 31
    june = 30
    july = 31
    august = 31
    september = 30 
    october = 31
    november = 30
    december = 31

    if (selectyear % 4 == 0):
        february = 29
        print('Год високосный')
    else: 
        february = 28
        print('Год не високосный')

    allmonths = [january, february, march, april, may, june, july, august, september, october, november, december]
    i = 0
    value = 0

    for i in range(len(allmonths)):
        value += SumValueMonth(allmonths[i])
    
    print(f"Итоговое значение: {value}")
else:
    print('Введите Положительное Число')







