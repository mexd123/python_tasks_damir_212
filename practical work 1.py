

#1
export = float(input("введите экспорт :"))
imporT = float(input("введите импорт :"))

saldo = export - imporT
if saldo >= 1:
	print("ваш доход состовляет," + str(saldo))
else:
	print("ваш убыток состовляет," + str(saldo)) 

#2 
a = float(input("введите число a :"))
b = float(input("введите число b :"))
c = float(input("введите число c :"))

if a < b < c or c < b < a:
	print("число b среднее")
elif b < a < c or c < a < b:
	print("число a среднее")
elif a < c < b or b < c < a:
	print("число с среднее")
else:
	print("ошибка,числа совпадают")

#3 
a = int(input("введите число 1 :"))
b = int(input("введите число 2 :"))
if a % 2 == 0  and b % 2 ==0:
	print(True)
else:
	print(False)


