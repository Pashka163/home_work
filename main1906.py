#1

class CountDistance:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @staticmethod
    def dist_count(start, finish):
        dist = ((finish.x - start.x) ** 2 + (finish.y - start.y) ** 2) ** 0.5
        print(round(dist))

class Point(CountDistance):
    pass

p1 = Point(10, 20)
p2 = Point(20, 30)
CountDistance.dist_count(p1, p2)

#2

class Kondratiy:
    status = "Дедушка"

class Vasya(Kondratiy):
    status = "Отец"

class Masha(Vasya):
    status = "Дочь"

Kondratiy.status = "Дедушка"
Vasya.status = "Отец"
Masha.status = "Дочь"

masha = Masha()
vasya = Vasya()
print(masha.status)
print(vasya.status)