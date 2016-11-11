from model.CircularUnit import CircularUnit


class Bonus(CircularUnit):
    def __init__(self, id, x, y, speed_x, speed_y, angle, faction, radius, type):
        CircularUnit.__init__(self, id, x, y, speed_x, speed_y, angle, faction, radius)

        self.type = type
