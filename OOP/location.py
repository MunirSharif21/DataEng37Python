class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):  # overriding representation
        return f"Location(Latitude= {self.latitude}, Longitude={self.longitude})"

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"
    # whenever you print something, it will look for this sting representation
    # and if that doesn't exist, it will look for repr.


bham_academy = Location(latitude=.488647, longitude=-1.887249)
print(bham_academy)
print(f"The bham academy is located at {bham_academy}")
print(repr(bham_academy))
