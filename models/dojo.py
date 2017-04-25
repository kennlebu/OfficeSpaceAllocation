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
            self.add_occupant_to_office()


        elif person_type.upper() == 'FELLOW':
            # Create a new fellow and add them to the Dojo
            self.people.append(Fellow(person_name))
        else:
            print("A person can only be staff or a fellow")


    def add_occupant_to_office(self):
        # Get offices available in the Dojo
        offices = []
        for room in self.rooms:
            if room.room_type == 'office':
                offices.append(room)

        if len(offices) < 1:    # No office in the Dojo
            print("There are no offices in the Dojo yet. Create one using",
                    "create_room office <room_name>")
        else:
            # Get offices with spaces left in them
            unfilled_offices = []
            for office in offices:
                if office.occupants < office.max_occupants:
                    unfilled_offices.append(office)
            
            if len(unfilled_offices) < 1:   # All offices are full
                print("All offices are full. Create a new one using",
                        "create_room office <room_name>")
            else:
                # Pick an office at random
                selected_office = random.choice(unfilled_offices)
                # Add an occupant to the office
                selected_office.occupants += 1


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