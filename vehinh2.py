import  matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import numpy as np
from abc import ABC, abstractmethod
class shape(ABC):

    @abstractmethod
    def __init__(self,color, x_position,y_position):
        self.color = color
        self.x_position = x_position
        self.y_position = y_position

    def draw(self):
        pass

class Circle(shape):
    def __init__(self,color, x_position, y_position, radius):
        super().__init__(color, x_position,y_position)
        self.radius = radius

    def draw(self):
        figure, axes = plt.subplots()
        Drawing_colored_circle = plt.Circle((self.x_position, self.y_position), self.radius)
       # Drawing_colored_circle = plt.Circle((0.6, 0.6), 0.2, color='green')
        axes.set_aspect(1)
        axes.add_artist(Drawing_colored_circle)
        plt.show()


class Ellip(shape):
    def __init__(self,color, x_position,y_position,height,width,angle):
        super().__init__(color, x_position, y_position)
        self.height = height
        self.width = width
        self.angle = angle

    def draw(self):
        fig, ax = plt.subplots()
        ellipse = Ellipse((self.x_position, self.y_position), self.height, self.width, self.angle,color=self.color)
        ax.add_artist(ellipse)
        plt.show()


class Rectangle(shape):
    def __init__(self, color, x_position, y_position, height, width):
        super().__init__(color, x_position, y_position)
        self.height = height
        self.width = width

    def draw(self):
        figure, axes = plt.subplots()
        Rectangle = plt.Rectangle((self.x_position,self.y_position),self.height,self.width)
       #Rectangle = plt.Rectangle((0.2, 0.3), 0.3, 0.2, color='green')
        axes.add_patch(Rectangle)
        plt.show()


#n1=Circle('',0.6,0.6,0.2)
#n1.draw()

n2=Ellip('green',0.6,0.4,2,0,0.4)
n2.draw()

#n3=Rectangle('',0.3,0.4,0.4,0.3)
#n3.draw()