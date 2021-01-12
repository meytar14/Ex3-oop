# class which represent one dimension range
class Range:
    def __init__(self, mini: float, maxi: float):
        """
        init function for the class
        """
        self.min = mini
        self.max = maxi

    def get_length(self):
        """
        get the length
        """
        return self.max-self.min

    def get_portion(self, x: float):
        """
        the function get float and return the portion of this float
        """
        d1 = x-self.min
        return d1/self.get_length()

    def from_portion(self, p: float):
        """
        the function get float which represent portion and return the float before the portion
        """
        return self.min+p*self.get_length()


# class which represent two dimension range
class Range2D:
    def __init__(self, x_range: Range, y_range: Range):
        """
        init function for the class
        """
        self.x_range = x_range
        self.y_range = y_range

    def get_portion(self, x, y):
        """
        the function get 2 floats and return the portions of both floats
        """
        x1 = self.x_range.get_portion(x)
        y1 = self.y_range.get_portion(y)
        return x1, y1

    def from_portion(self, x, y):
        """
        the function get 2 floats which each one represent portion
        the function return the two floats before the portion
        """
        x1 = self.x_range.from_portion(x)
        y1 = self.y_range.from_portion(y)
        return x1, y1


# class which represent the change from one range to the other
class Range2Range:
    def __init__(self, world: Range2D, frame: Range2D):
        """
        init function for the class
        """
        self.world = world
        self.frame = frame

    def world_to_frame(self, x, y):
        """
        the function get x,y and change the frame by the portion
        """
        x1, y1 = self.world.get_portion(x, y)
        return self.frame.from_portion(x1, y1)
