# 2) Реализовать класс Road (дорога), в котором определить атрибуты:
#  length (длина), width (ширина). Значения данных атрибутов должны
#  передаваться при создании экземпляра класса. Атрибуты сделать
#  защищенными. Определить метод расчета массы асфальта, необходимого
#  для покрытия всего дорожного полотна. Использовать формулу:
#  длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
#  толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight_per_meter = 25
        self.thickness = 5

    def find_weight(self):
        weight = self._length * self._width * self.weight_per_meter * self.thickness
        print(weight)


r = Road(5000, 20)
r.find_weight()
