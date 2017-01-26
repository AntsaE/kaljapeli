class Player:

    def __init__(self, name, gender, weight):
        self.name = name
        self.gender = gender
        self.weight = weight

def addPlayer(disp):
    name = Input_field(disp, "Name", False)
    gender = Select_field(disp, "Gender", ["Man","Woman"])
    weight = Input_field(disp, "Weight in kg", True)
    disp.fill((0, 0, 0))
    return Player(name,gender,weight)