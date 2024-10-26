# Класс Rectangle, описывающий объект - прямоугольник
class Rectangle:

 # Выполняется каждый раз при создании нового прямоугольника
    def __init__(self, width, height):
        # выполняются команды задания высоты и ширины
        self.__setWidth__(width)
        self.__setHeight__(height)

# Метод задания ширины. Если она не положительная, то создаётся ошибка
    def __setWidth__(self, width):
        if(width <= 0):
            raise Exception('Длина не может быть меньше 0')
        self.__width = width
# Метод задания высоты. Логика аналогична методы задания ширины
    def __setHeight__(self, height):
        if(height <= 0):
            raise Exception('Ширина не может быть меньше 0')
        self.__height = height
# Метод вычисления периметра
    def get_perimeter(self):
        return 2 * self.__width + 2 * self.__height
# Метод задания площади
    def get_square(self):
        return self.__width * self.__height
# Все объекты имеют строковое представление, которое задаётся встроенным методом __str__. Его можно настроить
    def __str__(self):
        return 'Rectangle\nwidth = ' + str(self.__width) + '\nheight = ' + str(self.__height)
# Метод, рисующий прямоугольник в консоли символами *
    def drawRectangle(self):
        print('*' * self.__width)
        for i in range(self.__height - 2):
            print('*' + ' ' * (self.__width - 2) + '*')
        print('*' * self.__width)