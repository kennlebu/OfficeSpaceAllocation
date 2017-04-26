import random

from models.room import Room
from models.office import Office
from models.living_space import LivingSpace
from .staff import Staff
from .fellow import Fellow

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

        if person_type.upper() == 'STAFF':
            # Create a new staff and add them to the Dojo
            self.people.append(Staff(person_name))
            # Add an occupant to a random Office
            self.add_occupant('office')


        elif person_type.upper() == 'FELLOW':

            if wants_accommodation.upper() == 'Y':
                # Create a new fellow and add them to the Dojo
                # and allocate them a living space
                self.people.append(Fellow(person_name, 'Y'))
                # Add an occupant to a living space
                self.add_occupant('livingspace')

            else:
                # Create a new fellow and add them to the Dojo
                self.people.append(Fellow(person_name))
                # Add an occupant to a random living space
                self.add_occupant('office')

        else:
            print("A person can only be staff or a fellow")


    def add_occupant(self, room_type):
        """ Adds an occupant to a random room of type <room_type> """

        # Get spaces available in the Dojo
        spaces = []
        for room in self.rooms:
            if room.room_type == room_type:
                spaces.append(room)

        if len(spaces) < 1:    # No space in the Dojo
            print("There are no {} in the Dojo yet. Create one using".format(room_type + 's'),
                  "create_room {} <room_name>".format(room_type))
        else:
            # Get rooms with space left in them
            unfilled_spaces = []
            for space in spaces:
                if space.occupants < space.max_occupants:
                    unfilled_spaces.append(space)

            if len(unfilled_spaces) < 1:   # All spaces are full
                print("All {} are full. Create a new one using".format(room_type + 's'),
                      "create_room {} <room_name>".format(room_type))
            else:
                # Pick a space at random
                selected_space = random.choice(unfilled_spaces)
                # Add an occupant to the space
                selected_space.occupants += 1




    def list_rooms(self):
        """ Lists the rooms that are existing in the Dojo """
        pass


    def create_room(self, room_type, *room_name):
        """ Creates a room of type <room_type> called <room_name>.
        If more than one name is passed, it creates as many rooms
        with the different names of type <room_type>.
        """

        if len(room_name) >= 1:
            for name in room_name:
                new_room = Office(name) if room_type.upper() == 'OFFICE' else LivingSpace(name)
                self.rooms.append(new_room)



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
        