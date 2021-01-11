class Range:
    def __init__(self, min : float , max : float):
        self.min=min
        self.max=max

    def get_length(self):
        return self.max-self.min

    def get_portion(self, x : float):
        d1=x-self.min
        return d1/self.get_length()

    def from_portion(self, p : float):
        return self.min+p*self.get_length()


class Range2D:
    def __init__(self, x_range : Range, y_range: Range):
        self.x_range=x_range
        self.y_range=y_range

    def get_portion(self,x,y):
        x1=self.x_range.get_portion(x)
        y1=self.y_range.get_portion(y)
        return(x1,y1)

    def from_portion(self, x, y):
        x1 = self.x_range.from_portion(x)
        y1 = self.y_range.from_portion(y)
        return (x1, y1)

class Range2Range:
    def __init__(self, world : Range2D, frame : Range2D):
        self.world=world
        self.frame=frame

    def world_to_frame(self, x, y):
        x1, y1= self.world.get_portion(x, y)
        return self.frame.from_portion(x1,y1)








