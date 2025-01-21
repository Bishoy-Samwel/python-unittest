class Car:
    def __init__(self):
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    def car_speed(self):
        if self.speed < 0:
            return "Level shall be Invalid"
        elif 0 <= self.speed <= 40:
            return "Level shall be Low"
        elif 41 <= self.speed <= 120:
            return "Level shall be Normal"
        elif 121 <= self.speed <= 200:
            return "Level shall be High"
        elif 201 <= self.speed < 220:
            return "Level shall be V.High"
        else:  # self.speed >= 220
            return "Level shall be Invalid"
