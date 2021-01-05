import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        while True:
            t = TrafficLight
            print(t.__color[0])
            time.sleep(7)
            print(t.__color[1])
            time.sleep(2)
            print(t.__color[2])
            time.sleep(7)


t = TrafficLight()
t.running()
