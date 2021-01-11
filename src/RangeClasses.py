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
        


