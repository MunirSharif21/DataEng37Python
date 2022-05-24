class Car:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self._speed = 0
        # underscore in front of variable name
        # so use the provided getter for it

    def accelerate(self, mph):
        self._speed = min(self._speed + mph, self.top_speed)
        '''
        if self.speed + mph > self.top_speed:
            self.speed = self.top_speed
        else:
            self.speed += mph
        '''

    def brake(self, mph):
        self._speed = max(self._speed - mph, 0)
        '''
        if self.speed - mph < 0:
            self.speed = 0
        else:
            self.speed -= mph
        '''

    # getter
    def get_speed(self):
        return self._speed

mycar = Car("Toyota", "Yaris", 100)

mycar.accelerate(110)
print(mycar.get_speed())
mycar.brake(110)
print(mycar.get_speed())

# mycar._speed = 9999
# I can still do this despite using an underscore
# make it a dun-der (double underscore)
