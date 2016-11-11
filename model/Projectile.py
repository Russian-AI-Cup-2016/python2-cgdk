from model.CircularUnit import CircularUnit


class Projectile(CircularUnit):
    def __init__(self, id, x, y, speed_x, speed_y, angle, faction, radius, type, owner_unit_id, owner_player_id):
        CircularUnit.__init__(self, id, x, y, speed_x, speed_y, angle, faction, radius)

        self.type = type
        self.owner_unit_id = owner_unit_id
        self.owner_player_id = owner_player_id
