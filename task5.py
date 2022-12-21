# 5) Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
#  Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
# класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом
# из классов реализовать переопределение метода draw. Для каждого
# из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery():
    title = "Канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


obj_1 = Stationery()
print(obj_1.title)
obj_1.draw()
obj_2 = Pen()
obj_2.draw()
obj_3 = Pencil()
obj_3.draw()
obj_4 = Handle()
obj_4.draw()
