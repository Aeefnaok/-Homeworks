class Road:

    def __init__(self, length, width):
        self._l = length
        self._w = width

    def weigh_of_asphalt(self):
        weight, height, r = 25, 5, Road
        r.__init__(self, self._l, self._w)
        w_asp = self._l * self._w * weight * height
        print(f'Масса асфальта для покрытия всего дорожного полотна = {int(w_asp / 1000)} т.')


r = Road(20, 5000)
r.weigh_of_asphalt()
