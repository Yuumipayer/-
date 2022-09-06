class Mas:

    def __init__(self):
        self.list = []

    def add_h(self, h):
        if len(self.list) >= 5:
            self.list.pop(0)
        else:
            self.list.append(h)

    def view(self):
        return self.list


ms = Mas()


# ft = input("Введите операцию : ")
# ans = eval(ft)
# ms.add_h(ft)
# print(ans)


while 1:
    way = input("Введите P чтобы добавить оперцию \nВведите C чтобы ввести новые данные\nВведите H Чтобы увидеть историю\nВведите S Чтобы вычислить корень\nВведите : ")

    if way.upper() in "PР":
        sc = input("Введит доп операцию: ")
        ans = str(ans) + str(sc)
        ms.add_h(ans)
        print(eval(ans))

    elif way.upper() in "CС":
        ft = input("Введите операцию : ")
        ans = eval(ft)
        ms.add_h(ft)
        print(ans)

    elif way.upper() in "HН":
        h = ms.view()
        # print(h)
        print("\nИстория расчётов ")
        for i in h:
            print(i, "=", eval(i))

    elif way.upper() in "S":
        ft = input("Введите число для вычисления корня : ")
        ans = float(float(ft)**(1/2))
        print(ans)
        ms.add_h(str(ans))

    else:
        ans = eval(way)
        print(ans)
        ms.add_h(ans)
