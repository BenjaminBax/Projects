from Chapter12GeoObj import GeometricObject
import math

class Triangle(GeometricObject): 
    def __init__(self, side1=1.0, side2=1.0, side3=1.0): 
        super().__init__()  
        self.__side1 = side1 
        self.__side2 = side2 
        self.__side3 = side3 
    
    def getSide1(self): 
        return self.__side1

    def getSide2(self): 
        return self.__side2
    
    def getSide3(self): 
        return self.__side3

    def getArea(self): 
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
        return area

    def getPerimeter(self): 
        return (self.__side1 + self.__side2 + self.__side3)
    
    def __str__(self): 
        return super().__str__() + " Triangle: side 1 = " + str(self.__side1) + " side 2 = " + str(self.__side2) + " side3 = " + str(self.__side3)


def main(): 
    side1, side2, side3 = eval(input("Please enter three sides: "))
    color = input("enter a color: ")
    filled = eval(input("Enter 1 if triangle is filled or 0 if triangle is empty: ")) 

    if filled == 1: 
        filled = True
    else: 
        filled = False

    bax = Triangle(side1, side2, side3)
    bax.setColor(color)
    bax.setFilled(filled)
    print(bax)

main()