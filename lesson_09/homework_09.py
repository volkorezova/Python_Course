# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Romb:
     def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("side_a should be > 0")
            super().__setattr__(name, value)
        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("angle_a should be > 0 and < 180")
            super().__setattr__("angle_a", value)
            super().__setattr__("angle_b", 180 - value)
        else:
            super().__setattr__(name, value)
     def druk(self):
         result_info = (f'side_a = {self.side_a}; angle_a = {self.angle_a}; angle_b = {self.angle_b}')
         return result_info

romb_figure = Romb()
romb_figure.side_a = 10
romb_figure.angle_a = 70

print(f'side_a: {romb_figure.side_a}')
print(f'angle_a: {romb_figure.angle_a}')
print(f'Overal result: {romb_figure.druk()}')