# Дано расстояние между двух точек,
# объем бака, средний расход топлива , остаток топлива в баке на начало пути.
#   через х  км на пути встеряается заправка. Следует арссчитать :
# 1) координату первой заправки
# 2) координаты всех последующих заправок чтоб остановок на заправку было найменьшее количество.

from random import randint
def zadacha():
    global key
    global spisok_zapravok
    # все  данные  для примера
    distance = 4000
    consumption = 9
    bak = 70
    ostatok_na_nachalo = 20
    dist_na_ostatke = ostatok_na_nachalo * 100 / consumption  # расстояние на остатке

    def zapravki():  # рандомно расставляет заправки  в  среднем через каждые 25 км
        ls =[]
        amount_of_stations = round(distance / 25)  # опеделеяем сколько станций надо
        for c in range(amount_of_stations):
            x = randint(1, distance)   # выбираем точку где будет заправка
            ls.append(x)
        ls.sort()   # сортируем точки на маршруте и заносим в список
        ls2 =[ x + 1  for x in range(amount_of_stations)]   # формирируем список , с номерами заправок, кторые потом будут ключами
        global spisok_zapravok
        spisok_zapravok = dict(zip(ls2, ls)) # ключ =  это номер заправки, значение = на каком километре она
    zapravki()
    spisok_pitstopov = []
    for key, val in spisok_zapravok.items():
        if dist_na_ostatke <= val:
            point = key-1, spisok_zapravok[key - 1]  # первая заправка (номер заправки и км, в ввиде кортежа)
            spisok_pitstopov.append(point[0])
            spisok_pitstopov.append(point[1])    # заносим данные по 1ой заправке(на остатке)
            break
    dist_na_poln = bak * 100 / consumption  # расстоян на полн баке
    samaya_dalnjaja_zaprawka = max(spisok_zapravok.values())   # иначе в строке 39 будет ошибка (обращение к несущесвующему ключу))
    summa_do_sled_zapr = 0   # эта сумма всех отрезков маежду заправками от точки заправки
    tochka_otscheta = spisok_pitstopov[1]   # создаем новую переменную, так как старую в цикле использовать нельзя
    for key, value in spisok_zapravok.items():   # Главный алгоритм. если координата запрвки равна или больше точке очередной заправки,
        # то сумма отрезков между запрвками начинает расти , пока не станет больше чем расстояние на полном баке.
        # тогда эта сумма обнуляется  и в результат заносятся данные по максимально удаленной заправке.
        # точка отсчета обнуляется иначе в след цикле выбьет ошибку
        if value >= tochka_otscheta and value <  samaya_dalnjaja_zaprawka:  # чтоб не выбивало ошибку
            summa_do_sled_zapr += spisok_zapravok[key+1] - spisok_zapravok[key] # складывается киломатержа до последующих хаправок
            # и если он больше чем киломаераж на полном баке , то
            if summa_do_sled_zapr > dist_na_poln:
                summa_do_sled_zapr =0
                tochka_otscheta = value
                spisok_pitstopov.append(key)
                spisok_pitstopov.append(value)

    def vyvod():     # красиво выыодит
        print(f' при расстоянии {distance} км,')
        print(f' расходе на 100км равному {consumption} л, ')
        print(f' первоначальном остатке в {ostatok_na_nachalo} , ')
        print(f' с объемом бака равным  {bak} ' )
        print(f' ваш перечень остановок для заправок будет следующим:')
        for c in range(len(spisok_pitstopov)):
            if c % 2 == 0:
                nomer_zapravli = spisok_pitstopov[c]
            if c % 2 == 1:
                km_zapravka = spisok_pitstopov[c]
                print(f' номер заправки {nomer_zapravli}, на каком километре заправка: {km_zapravka}')
    vyvod()
zadacha()