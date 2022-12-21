# 3) Реализовать базовый класс Worker (работник), в котором определить
#  атрибуты: name, surname, position (должность), income (доход).
#  Последний атрибут должен быть защищенным и ссылаться на словарь,
#  содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#  Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
#  (get_full_name) и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры
# класса Position, передать данные, проверить значения атрибутов,
#  вызвать методы экземпляров).

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Имя работника: {self.name} {self.surname}")


    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        print(f"Полная зарплата = {total_income}")


obj = Position("Петр", "Михайлов", "Менеджер", 100000, 30000)
obj.get_full_name()
obj.get_total_income()
print(obj.name, obj.surname, obj.position, obj._income)
