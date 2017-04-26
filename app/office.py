from .room import Room

class Office(Room):
    """ An office can be allocated to either staff or
    fellows. An office can accommodate a maximum of 6
    people.
    """

    def __init__(self, room_name):
        super().__init__(room_name)
        self.max_occupants = '6'
        self.room_type = 'office'
