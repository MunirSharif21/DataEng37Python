# Create a class to represent Spartans

class Spartan:
    def __init__(self, name, stream, course, client=None):  # initialise
        self.name = name
        self.stream = stream
        self.course = course
        self.client = client  # None by default


munir = Spartan(
    "Munir",
    "Data Engineering",
    "Data 37",
    "Home Office"  # variable with default must be at the end
)


