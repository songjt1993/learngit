# /usr/bin/evn Python3
# -*- coding: utf-8 -*-

"""this is blank"""

__author__ = 'Ohayoo'


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return (self.x, self.y).__str__()

    __repr__ = __str__


class Line(object):
    def __init__(self, p1=Point(), p2=Point()):
        self.point1 = p1
        self.point2 = p2

    def __str__(self):
        return (self.point1, self.point2).__str__()

    __repr__ = __str__

    def length(self):
        return ((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)**0.5

    def slope(self):
        if self.point1.x == self.point2.x:
            return None
        return (self.point2.y-self.point1.y)/(self.point2.x-self.point1.y)


def test():
    p1 = Point()
    p2 = Point(1, 2)
    line1 = Line(p1, p2)
    print(line1)
    print(line1.length(), line1.slope())


if __name__ == '__main__':
    test()
