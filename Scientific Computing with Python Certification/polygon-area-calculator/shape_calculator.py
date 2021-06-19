class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, n):
        self.width = n

    def set_height(self, n):
        self.height = n

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            lines = []
            for n in range(self.height):
                lines.append('*' * self.width)
            lines = '\n'.join(lines) + '\n'
            return lines

    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width, width)


    def set_side(self, n):
        self.set_width(n)
        self.set_height(n)

    def set_height(self, n):
        self.height = n
        self.width = n

    def set_width(self, n):
        self.width = n
        self.height = n

    def __str__(self):
        return f"Square(side={self.height})"
