from abc import ABC, abstractmethod
from matplotlib.patches import Ellipse
import  matplotlib.pyplot as plt

class Shape(ABC):
    @abstractmethod
    def __init__(self, color, x_position, y_position):
        self.color = color
        self.x_position = x_position
        self.y_position = y_position

    def draw(self):
        pass


class Circle(Shape):
    def __init__(self,color, x_position, y_position,radius):
        super().__init__(color, x_position, y_position)
        self.__radius = radius

    def draw(self):
        fig,ax = plt.subplots()
        #figure, axes = plt.subplots()
        Drawing_colored_circle = plt.Circle((self.x_position, self.y_position), self.__radius, color=self.color)
        ax.set_aspect(1)
        ax.add_artist(Drawing_colored_circle)
        plt.title('Hình Tròn')
        plt.show()


class ellipse(Shape):
    def __init__(self,color, x_position, y_position,angle,height,width):
        super().__init__(color,x_position, y_position)
        self.__angle = angle
        self.__height = height
        self.__width  = width


    def draw(self):
        fig,ax = plt.subplots()
        ellipse= Ellipse((self.x_position, self.y_position),self.__angle, self.__height, self.__width, color=self.color)
        #el = Ellipse((0.4, 0.6), 0.6, 0.4, facecolor='pink', angle=0.1)
        #ax.set_aspect(1)
        ax.add_artist(ellipse)
        plt.title('Hình ellip')
        plt.show()


       # ax.set(xlim=[-1, 10], ylim=[-1, 10])

class Rectangle(Shape):
    def __init__(self,color, x_position, y_position,height,width):
        super().__init__(color, x_position, y_position)
        self.__height = height
        self.__width = width

    def draw(self):
        fig, ax = plt.subplots()
        Rectangle = plt.Rectangle((self.x_position,self.y_position),self.__height,self.__width,color=self.color)
        ax.add_artist(Rectangle)
        plt.title('Hình Chữ Nhật')
        plt.show()



n1=Circle('lightgreen', 0.5, 0.5, 0.3)
n1.draw()

n2=ellipse('salmon', 0.5, 0.5, 0.6, 0.4, 0.6)
n2.draw()
#0.5, 0.5, 0.6, 0.4, 0.6)
#('pink', 0.5, 0.5, 0.2, 0.3, 60)

n3=Rectangle('plum',0.3,0.4,0.4,0.3)
n3.draw()

