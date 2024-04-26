import numpy as np
import matplotlib.pyplot as plt
import time
#[270, 285, 290, 300, 317]
massX = []                              #ОБЪЯВЛЕНИЕ ПЕРЕМЕННЫХ
massXkv = []
sixcolomnmass = []
sevencolomnmass = []
summX = 0
summXkv = 0
n = 12
countmore = 0
countless = 0
sixcolomn = 0
a = [[0.7071],
     [0.6872, 0.1677],
     [0.6646, 0.2413],
     [0.6431, 0.2806, 0.0875],
     [0.6233, 0.3031, 0.1401],
     [0.6052, 0.3164, 0.1743, 0.0561],
     [0.5888, 0.3244, 0.1976, 0.0947],
     [0.5789, 0.3291, 0.2141, 0.1224, 0.0399],
     [0.5601, 0.3315, 0.2260, 0.1429, 0.0695],
     [0.5475, 0.3325, 0.2347, 0.1586, 0.0922, 0.0303]]

ressummass = []
wmass = []


def norm():
    resmass = []
    resmasss = []
    massX = np.random.normal(10, 10, 12)
    r = str(massX).split(' ')

    for i in range(len(r)):
        if len(r[i]) > 2:
            resmass.append(r[i])

    for j in range(len(resmass)):
        if j == 5:
            lenc = len(resmass[j]) - 1
            c = resmass[j][0:lenc]
            resmasss.append(float(c))
        elif resmass[j][0]=='[':
            a = resmass[j][1::]
            resmasss.append(float(a))
        elif resmass[j][-1]==']':
            lenb = len(resmass[j])-1
            b = resmass[j][0:lenb]
            resmasss.append(float(b))
        else:
            resmasss.append(float(resmass[j]))
    return(resmasss)


flag = int(input("Введите 0, если хотите ввести свою выборку, и 1, если хотите сгенерировать случайные числа с дискретным распределением: "))
if flag == 0:                                                #ЕСЛИ ВЫБОРКА ИЗ ЗАДАННЫХ ЗНАЧЕНИЙ
    n = int(input("Введите объем выборки: "))
    for i in range(0, n):
        number = int(input(f"Введите {i+1} элемент: "))
        massX.append(number)
    summX = sum(massX)
    ares = a[n - 3]
    lenmass = 1
if flag==1:                                                   #ЕСЛИ ВЫБОРКИ ИЗ СЛУЧАЙНЫХ ЗНАЧЕНИЙ
    n = int(input("Введите объем выборки: "))
    leftborder = input("Введите минимальный элемент: ")
    rightborder = input("Введите максимальный элемент: ")
    ares = a[n - 3]
    lenmass = int(input("Введите количество итераций: "))
timer = time.perf_counter()


for i in range(0, lenmass):
    j = n-i                                                   #ЗНАЧЕНИЯ J
    if flag==1:

        summX = sum(massX)
        for k in range(0, n):                                   #ЗНАЧЕНИЯ X
            rnum = (np.random.randint(leftborder, rightborder))
            massX.append(rnum)
            summX += rnum
    massX.sort()
    for g in range(len(massX)):                                 #ЗНАЧЕНИЯ X^2
        kkk = massX[g]**2*10**(-4)
        massXkv.append(kkk)
        summXkv += kkk
    maxim = len(massX) - 1
    minim = 0
    for z in range(0, len(ares)):                               #ЗНАЧЕНИЯ ШЕСТОГО СТОЛБЦА
        sixcolomn = float(massX[maxim]) - float(massX[minim])

        sixcolomnmass.append(sixcolomn)
        maxim -= 1
        minim += 1
    for l in range(0, len(ares)):                                #ЗНАЧЕНИЯ СЕДЬМОГО СТОЛБЦА
        sevencolomn = sixcolomnmass[l] * ares[l]
        sevencolomnmass.append(sevencolomn)
    sevencolomnmass.reverse()
    sumsevencolomn = sum(sevencolomnmass)
    b_kv = sumsevencolomn**2                                      #ЗНАЧЕНИЕ B^2
    fi_kv = summXkv * 10**4 - (summX**2)/n                        #ЗНАЧЕНИЕ Ф^2
    W = b_kv / fi_kv                                               #ЗНАЧЕНИЕ W
    if flag == 1:
        if W < 0.859:
            countless += 1
        else:
            countmore += 1

    sixcolomnmass.reverse()
    """
    print("Первый столбец: ", massX)                                #ВЫВОД РЕЗУЛЬТАТОВ
    print("Сумма по первому столбцу: ", summX)
    print("Второй столбец: ", massXkv)
    print("Сумма по второму столбцу: ", summXkv)
    print("Шестой столбец: ", sixcolomnmass)
    print("Седьмой столбец: ", sevencolomnmass)
    print("Сумма по седьмому столбцу: ", sumsevencolomn)
    print("b_kv: ", b_kv)
    print("fi_kv: ", fi_kv)
    print("W: ", W)
    print('')
    """
    wmass.append(W)                                               #МАССИВ ЗНАЧЕНИЙ КРИТЕРИЯ W
    summXkv = 0
    if flag == 1:
        massX = []
        summX = 0
    massXkv = []
    sixcolomnmass = []
    sevencolomnmass = []
    sevencolomn = 0

if flag == 1:
    respercent = countless/(countless+countmore) * 100
    print("Процент значений меньше критического: ", respercent, "%")
    averageW = sum(wmass)/len(wmass)
    print("Среднее W: ", averageW)
massres = [i for i in range(0, lenmass)]

restime = time.perf_counter() - timer
print("Время на работу программы (в секундах): ", restime)

plt.axis([0,lenmass,0,1])                                                  #РАБОТА С ГРАФИКОМ
plt.title('График W-критерия при нормальном распределении')
plt.scatter(massres, wmass, s=3, label = "W-критерий")
plt.axhline(y = 0.859, color = "red", label = "Критическое значение W-критерия")
if flag == 1:
    plt.axhline(y = averageW, color = "yellow", label = "Среднее наблюдаемое значение W-критерия")
plt.legend(loc='best')
plt.show()



#Подсчитать выпадающие (в процентах), найти средний процент выпадающих и для него интервалы (на большом значении выборки)
