class Rectangle:

    def __init__(self, width, height):
        self.__setWidth__(width)
        self.__setHeight__(height)

    def __setWidth__(self, width):
        if(width <= 0):
            raise Exception('Длина не может быть меньше 0')
        self.__width = width

    def __setHeight__(self, height):
        if(height <= 0):
            raise Exception('Ширина не может быть меньше 0')
        self.__height = height

    def get_perimeter(self):
        return 2 * self.__width + 2 * self.__height

    def get_square(self):
        return self.__width * self.__height

    def __str__(self):
        return 'Rectangle\nwidth = ' + str(self.__width) + '\nheight = ' + str(self.__height)

    def drawRectangle(self):
        print('*' * self.__width)
        for i in range(self.__height - 2):
            print('*' + ' ' * (self.__width - 2) + '*')
        print('*' * self.__width)