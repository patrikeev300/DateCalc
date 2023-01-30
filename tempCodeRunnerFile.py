print ("Добрый день, вас приветствует программа подсчета дней в году")
finalValue = 0
selectyear = int(input ("Выберите нужный вам год: "))

if (selectyear % 4 == 0 and selectyear % 100 != 0 or selectyear % 400 == 0):
    february = 29
    print('Год високосный')
else: 
    february = 28
    print('Год не високосный')

ArrayMonths = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(len(ArrayMonths)):
    for value in range(ArrayMonths[i]):
       value += 1
       finalValue += sum(map(int, str(value)))
print(finalValue)








