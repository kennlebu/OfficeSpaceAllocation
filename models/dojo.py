from room import Rooms
from office import Office
from living_space import LivingSpace

class Dojo():
    """ Dojo is a facility that accommodates Andelans in Kenya.

    A Dojo has many rooms and new fellows and staff are assigned 
    rooms at random. A new fellow is assigned an office and can 
    opt for living space too.
    New staff can only be allocated office space.
    """

    def __init__(self):
        self.rooms = []
        self.people = []

    def add_person(self, person_name, person_type, wants_accommodation='N'):
        """ Randomly adds a person to a room.
        Staff can only be added to offices. Fellows can be added to offices
        and living spaces. Living spaces however, are optional. A fellow is 
        only added to a living space if they opt in by passing 'Y' as an
        argument on <wants_accommodation>
        """
        pass


    def list_rooms(self):
        """ Lists the rooms that are existing in the Dojo """
        pass


    def create_room(self, room_type, *room_name):
        """ Creates a room of type <room_type> called <room_name>.
        If more than one name is passed, it creates as many rooms 
        with the different names of type <room_type>.
        """
        pass


    def print_room(self, room_name):
        """ Prints the names of all the people in the room """

        pass


    def print_allocations(self, filename=None):
        """ Prints a list of room allocations. If filename is specified,
        the list of allocations are outputted to the specified txt file.
        """
        pass


    def print_unallocated(self, filename=None):
        """ Prints a list of unallocated people. If filename is specified,
        the list is outputted to the specified txt file.
        """
        pass


    def reallocate_person(self, person_identifier, new_room_name):
        """ Reallocates the person identified by <person_identifier>
        to a new room specified by <room_name>
        """
        pass


    def load_people(self, filename):
        """ Adds people to rooms from the specified txt file. """

        pass