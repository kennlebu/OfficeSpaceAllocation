from room import Room

class LivingSpace(Room):
    """ Living Space can only be allocated to fellows.
    A living space accommodates a maximum of 4 people.
    """

    def __init__(self, room_name):
        super.__init__(self, room_name)
        self.max_occupants = '4'
        self.room_type = 'livingspace'
