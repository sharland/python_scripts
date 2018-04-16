class Bug(object):  #blueprint for an object
    legs = 0
    distance = 0

    def __init__(self, name, legs): #this begins the class constructor which is first method which runs when class is instantiated
        self.name = name
        self.legs = legs

    def Walk(self):
        self.distance += 1

    def ToString(self):
        return self.name + " has " + str(self.legs) + " legs" + " and taken " + str(self.distance) + "steps."


Bug("spider",8)

Bug.Walk("Spider",8)
