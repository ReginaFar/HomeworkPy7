# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police(булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула(куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
#  скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, speed, max_speed, color, name, is_police):
        self.speed = speed
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f"{self.name} начала движение")

    def stop(self):
        if self.speed == 0:
            print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {self.direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля = {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.max_speed == 60:
            print("Это семейный автомобиль")
            if self.speed > 60:
                print(f"{self.name} превысил скорость!")


class WorkCar(Car):
    def show_speed(self):
        if self.max_speed == 40:
            print("Это семейный автомобиль")
            if self.speed > 40:
                print(f"{self.name} превысил скорость!")


class PoliceCar(Car):
    def watching(self):
        if self.is_police:
            print("Едет полиция!")

# class SportCar(Car):
   # def sport_car(self):
      #  if self.speed


car = Car(50, 60, 'red', 'subaru', False)
print(car.speed, car.color, car.name, car.is_police)
car.go()
car.stop()
car.turn('налево')
car.show_speed()
