class Room():
    """ Defines a room in the Dojo. """

    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = 0  # Number of people in the room currently

