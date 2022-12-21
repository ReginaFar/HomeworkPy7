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
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f"{self.color} {self.name} начала движение")

    def stop(self):
        if self.speed == 0:
            print(f"{self.color} {self.name} остановилась")

    def turn(self, direction):
        if self.speed > 0:
            print(f"{self.color} {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля = {self.speed} км/ч")

    def police(self):
        if self.is_police:
            print("Едет полиция!")


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость = {self.speed} км/ч')
        if self.speed > 60:
            print(f"{self.color} {self.name} превысила скорость!")


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость = {self.speed} км/ч')
        if self.speed > 40:
            print(f"{self.color} {self.name} превысила скорость!")


class PoliceCar(Car):
    def police_car(self):
        print(f"{self.color} {self.name} - полицейская машина")


class SportCar(Car):
    def sport_car(self):
        (f"{self.color} {self.name} - спортивная машина")


car = Car(50, 'красная', 'subaru', False)
print(car.speed, car.color, car.name, car.is_police)
car.go()
car.stop()
car.turn('налево')
car.show_speed()
car.police()
print()
car_2 = TownCar(80, 'черная', 'toyota', True)
car_2.go()
car_2.stop()
car_2.turn('направо')
car_2.show_speed()
car_2.police()
print()
car_3 = WorkCar(0, 'белая', 'Lada', False)
car_3.go()
car_3.stop()
car_3.turn('направо')
car_3.show_speed()
car_3.police()
print()
car_4 = SportCar(200, 'фиолетовая', 'Lamborghini', True)
car_4.go()
car_4.stop()
car_4.turn('налево')
car_4.show_speed()
car_4.police()
print()
car_5 = PoliceCar(150, 'белая', 'Kia', True)
car_5.go()
car_5.stop()
car_5.turn('налево')
car_5.show_speed()
car_5.police()
print()
